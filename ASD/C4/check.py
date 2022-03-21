import sys
import os
# import psutil
from zad3       import  SortTab
from time       import  time

def check_program(path):
    file_in     =   open(f"{path}.in", "r")
    file_out    =   open(f"{path}.out", "r")
    k, n, P, T = 0, 0, [], []
    flag_k, flag_n = True, True
    counter_k, counter_n = 0, 0
    # make input

    for line in file_in:
        if flag_k:
            k = line
            k = int(k)
            flag_k = False
        elif counter_k < k:
            P.append(line)
            counter_k += 1

            P[-1] = P[-1].rsplit(" ")
            P[-1][0] = int(P[-1][0])
            P[-1][1] = int(P[-1][1])
            P[-1][2] = float(P[-1][2])
        elif flag_n:
            n = line
            n = int(n)
            flag_n = False
        else:
            T.append(float(line))

    # make an anwser
    output_file = []
    for line in file_out:
        output_file.append(line)
        output_file[-1] = float(output_file[-1])

    # check program
    # start_m     =   psutil.Process().memory_full_info().rss
    start_t         =   time()
    output_prog     =   SortTab(T, P)
    end_t           =   time()
    # end_m       =   psutil.Process().memory_full_info().rss

    # check output
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

