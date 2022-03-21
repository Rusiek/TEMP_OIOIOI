import pathlib
import sys
import os
import re
from time import time
from subprocess import Popen, PIPE

MAX_TIME        =   1
MAX_MEMORY      =   2 ** 20
RAPORT_WRONG    =   5

def benchmark():
    print("Running benchmark... ")
    def fib():
        start_t = time()
        a = 1
        b = 1
        for _ in range(85000):
            a, b = b, a + b
        end_t = time()
        return end_t - start_t

    iterations = 50
    iteration_time = [fib() for _ in range(iterations)]
    total_time = sum(iteration_time)
    avg_time = total_time / iterations

    print("Finished running benchmark")
    print(f"Normalized time: {round(avg_time, 5)}")
    print("(this is how long \"1 second\" takes on your computer)\n")

    return 5 * avg_time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Change B to KB, MB or GB
def memory_to_human(val):
    unit  =   "B"
    if val > 1024:
        val     /=  1024
        unit  =   "KB"
    if val > 1024:
        val     /=  1024
        unit  =   "MB"
    if val > 1024:
        val     /=  1024
        unit  =   "GB"
    return f"{round(val, 3)}{unit}"

# List some of failed tests
def list_error(tab, string):
    output = ""
    if tab != []:
        output  +=  string    
        for test in range(min(len(tab), RAPORT_WRONG)):
            output  +=  f"{tab[test]}   "
        if len(tab) > RAPORT_WRONG:
            output  +=  f"and {len(tab) - RAPORT_WRONG} more"
        output  += "\n"
    return output

# Generate raport about directory
def raport(tab, benchmark_time):
    output  =   f"TEST OK:          {tab[0]}\n"
    output  +=  f"TEST ERROR:       {tab[1]}\n"
    max_time = tab[2]
    avg_time = tab[7] / (tab[0] + tab[1])
    avg_norm_time = benchmark_time / avg_time
    output  +=  f"MAX TIME:         {round(max_time, 5)}s\n"
    output  +=  f"AVG TIME:         {round(avg_time, 5)}s\n"
    output  +=  f"PERFORMANCE:      {round(avg_norm_time, 7)}s\n"
    # if tab[3] < 10 ** 5:
    #     output  +=  f"MAX MEMORY:       LESS THAN 100KB\n"
    # else:
    #     output  +=  f"MAX MEMORY:       {memory_to_human(tab[3])}\n"
    output  +=  list_error(tab[4], 'WRONG OUTPUT:     ')
    output  +=  list_error(tab[5], 'TIME EXCEEDED:    ')
    # output  +=  list_error(tab[6], 'MEMORY EXCEEDED:  ')
    print(output)

# Check directory
def check_dir(path):
    OK              =   0
    ERROR           =   0
    MAX_U_TIME      =   0
    AVG_U_TIME      =   0
    MAX_U_MEMORY    =   0
    OUTPUT_LIST     =   []
    TIME_LIST       =   []
    MEMORY_LIST     =   []

    # Check all files in subdirs and group by subdir
    for root, subdirs, files in os.walk(path):
        for file in files:
            counter_path    =   str(path).count("\\")
            counter_file    =   str(os.path.join(root, file)).count("\\")
            if counter_path == 0:
                counter_path = str(path).count("/")
            if counter_file == 0:
                counter_file = str(os.path.join(root, file)).count("/")
            if counter_file - counter_path == 1:
                start, end = time(), time()
                while end - start > 1:
                    end = time()

                pattern     =   '\\.in$'
                # If file name is '.in$' 
                if re.search(pattern, file):
                    # Run subprocess and prepare data
                    print(f"TESTING FILE {file}")
                    proc    =   Popen(f'{sys.executable} check.py {str(os.path.join(root, file))}', stdout=PIPE, shell=True)
                    prog  =   proc.communicate()
                    prog  =   str(prog[0])
                    prog  =   prog[2:-1].replace("\\r\\n", "\\n").rsplit("\\n")[:-1]
                    if prog[0] == "False":      prog[0] = False
                    else:                       prog[0] = True
                    prog[1], prog[2] = round(float(prog[1]), 3), int(prog[2])

                    # Make raport
                    if (not prog[0]) or prog[1] > MAX_TIME or prog[2] > MAX_MEMORY:
                        ERROR   +=  1
                        if not prog[0]:                 OUTPUT_LIST.append(file)
                        if prog[1]   >   MAX_TIME:      TIME_LIST.append(file)
                        if prog[2]   >   MAX_MEMORY:    MEMORY_LIST.append(file)
                    else:
                        OK  +=  1

                    MAX_U_TIME      =   max(MAX_U_TIME, prog[1])
                    MAX_U_MEMORY    =   max(MAX_U_MEMORY, prog[2])
                    AVG_U_TIME      +=  prog[1]


    return [OK, ERROR, MAX_U_TIME, MAX_U_MEMORY, OUTPUT_LIST, TIME_LIST, MEMORY_LIST, AVG_U_TIME]

# Core
if __name__ == "__main__":
    normalized_time = benchmark()
    for path in os.walk(sys.argv[1]):
        dir_str = os.path.join(pathlib.Path().resolve(), sys.argv[1])
        if sys.argv[1] != path[0] and os.path.isdir(dir_str):
            dir_str = os.path.join(pathlib.Path().resolve(), path[0])
            output  =   check_dir(dir_str)
            if output[0] + output[1]:
                clearConsole()
                print(f"\nRAPORT FOR:       {path[0]}")
                raport(output, normalized_time)
                print(f"ENTER ANYTHING TO END TESTING {path[0]}: ", end = "")
                temp = input()