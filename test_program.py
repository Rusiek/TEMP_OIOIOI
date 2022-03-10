import sys
import os
import re
from check  import  check_program

MAX_TIME        =   1
MAX_MEMORY      =   1
RAPORT_WRONG    =   5


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


def raport(tab):
    output  =   f"TEST OK:          {tab[0]}\n"
    output  +=  f"TEST ERROR:       {tab[1]}\n"
    output  +=  f"MAX TIME:         {round(tab[2], 3)}s\n"
    # Add Memory Raport: tab[3]
    output += list_error(tab[4], 'WRONG OUTPUT:     ')
    output += list_error(tab[5], 'TIME EXCEEDED:    ')
    output += list_error(tab[6], 'MEMORY EXCEEDED:  ')
    print(output)


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
    for path in os.walk(sys.argv[1]):
        if sys.argv[1] != path[0] and os.path.isdir(sys.argv[1]):
            output  =   check_dir(path[0])
            if output[0] + output[1]:
                print(f"RAPORT FOR:       {path[0]}")
                raport(output)
                
