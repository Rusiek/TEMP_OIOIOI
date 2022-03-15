import sys
import os
# import psutil
from zad2       import  depth
from time       import  time

def check_program(path):
    file_in     =   open(f"{path}.in", "r")
    file_out    =   open(f"{path}.out", "r")

    # make input
    L = []
    for line in file_in:
        L.append(line)
        if (L[-1][-1] == '\n'):
            L[-1] = L[-1][:-1]
        L[-1] = L[-1].rsplit(" ")
        for i in range(len(L[-1])):
            L[-1][i] = int(L[-1][i])
    
    L = L[1:]

    # make an anwser
    output_file = 0
    for line in file_out:
        output_file = line
        output_file = int(output_file)

    # check program
    # start_m     =   psutil.Process().memory_full_info().rss
    start_t         =   time()
    output_prog     =   depth(L)
    end_t           =   time()
    # end_m       =   psutil.Process().memory_full_info().rss

    # check output
    str(output_prog)
    OK      =   output_prog  ==  output_file
    TIME    =   end_t   -   start_t
    MEMORY  =   0 # end_m   -   start_m 

    file_out.close()
    file_in.close()

    print(OK)
    print(TIME)
    print(MEMORY)

path    =   os.path.splitext(sys.argv[1])[0]
check_program(path)

