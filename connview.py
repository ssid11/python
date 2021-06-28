import sys, os.path as op


if not len(sys.argv) == 2:
    print("Неверное число аргументов!")
    exit(1)
with (open(sys.argv[1],'r')) as infile:
    while True:
        instr = infile.readline()
        if not instr:
            break
        inlst = instr.strip().split()
        print(inlst)

