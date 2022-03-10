import sys
import os
import re
from time           import time
from program        import funkcja

MAX_TIME        =   1
MAX_MEMORY      =   1
RAPORT_WRONG    =   5


def raport(tab):
    output  =   f"TEST OK:          {tab[0]}\n"
    output  +=  f"TEST ERROR:       {tab[1]}\n"
    output  +=  f"MAX TIME:         {round(tab[2], 3)}s\n"
    # Add Memory Raport:
    if tab[4] != []:
        output  +=  f"WRONG OUTPUT:     "    
        for test in range(min(len(tab[4]), RAPORT_WRONG)):
            output  +=  f"{tab[4][test]} "
        output  += "\n"
    if tab[5] != []:
        output  +=  f"TIME EXCEEDED:    "    
        for test in range(min(len(tab[5]), RAPORT_WRONG)):
            output  +=  f"{tab[5][test]} "
        output  += "\n"
    # Add memory exceeded

    print(output)

def check_program(path, test):
    MEMORY  =   0

    file_in     =   open(f"{path}/{test}.in", "r")
    file_out    =   open(f"{path}/{test}.out", "r")

    # Add function use
    start   =   time()
    output  =   funkcja(3)
    end     =   time()

    str(output)
    OK      =   output == file_out
    TIME    =   end - start

    file_out.close()
    file_in.close()

    return OK, TIME, MEMORY


# Test directory
def check_dir(path):
    OK              =   0
    ERROR           =   0
    MAX_U_TIME      =   0
    MAX_U_MEMORY    =   0
    OUTPUT_LIST     =   []
    TIME_LIST       =   []
    MEMORY_LIST     =   []

    for root, subdirs, files in os.walk(path):
        for file in files:
            pattern     =   '\.in$'
            if re.search(pattern, file):
                test, temp          =   os.path.splitext(file)
                prog_ok, prog_time, prog_mem  =   check_program(path, test)
                if (not prog_ok) or prog_time > MAX_TIME or prog_mem > MAX_MEMORY:
                    ERROR   +=  1
                    if not prog_ok:                     OUTPUT_LIST.append(test)
                    if prog_time    >   MAX_TIME:       TIME_LIST.append(test)
                    if prog_mem     >   MAX_MEMORY:     MEMORY_LIST.append(test)
                else:
                    OK  +=  1

                MAX_U_TIME      =   max(MAX_U_TIME, prog_time)
                MAX_U_MEMORY    =   max(MAX_U_MEMORY, prog_mem)

    return [OK, ERROR, MAX_U_TIME, MAX_U_MEMORY, OUTPUT_LIST, TIME_LIST, MEMORY_LIST]

# Find all .in/.out files in subdirectories
if __name__ == "__main__":
    for path in os.walk(sys.argv[2]):
        if sys.argv[2] != path[0] and os.path.isdir(sys.argv[2]):
            output  =   check_dir(path[0])
            if output[0] + output[1] != 0:
                print(f"RAPORT FOR:       {path[0]}")
                raport(output)
                
