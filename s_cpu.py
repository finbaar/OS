from random import randint


numberOfProcesses = int(input("Please enter how many processes"))

isRandom = input("Enter y/Y to randomly generates those processes\nor any keys to type it yourself")
print("if you intend to use priority, spcify the priority like A,25,2")
print("p1 is the process's name and 25 is the cpu burst time, 2 means the priority")
print("if you do not want to use priority,just omit the 2 like A,25")

theReadyQueue = []

if isRandom == 'y' or isRandom == 'Y':
    #randomly generated
    pass
else:
    pass