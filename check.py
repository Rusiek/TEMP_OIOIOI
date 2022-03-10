#   <Nazwa programu>    <Nazwa funkcji>
from program    import  funkcja
from time       import  time

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
