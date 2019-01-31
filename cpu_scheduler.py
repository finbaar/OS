from random import randint, sample
from process import Process

def generateProcesses(nums, needPrioiry, burstRange):
    """randomly generate n processes without priority,
       if priority is needed, the priority would be given randomly"""
    processList = []

    for i in range(nums):
        processList.append(Process(str(chr(65+i)), randint(1,burstRange), i, 0))
    
    if needPrioiry:
        #randomly chose number from the set
        temp = sample(range(nums), nums)
        #set each process's priority accordingly
        for i in range(nums):
            processList[i].setPriority(temp[i])
    
    return processList

#ask the users for the type of services
prompt = "1.FIFO\n2.Preemtive SJF\n3.Nonpreemtive SJF\n4.preemtive Priority\n5.Nonpreemtive priority\n6.Round Robin\n"
choiceOfAlgorithm = int(input(prompt))

#ask for how many processes will be in the ready queue
numberOfProcesses = int(input("Please enter how many processes\n"))
#ask for users wehter or not they would like to type those processes themselves
isRandom = input("Enter y/Y to reandomly generat processes or other keys to continue\n")

theReadyQueue = []

#setting the parameters resulting from the users' choices
if choiceOfAlgorithm == 4 or choiceOfAlgorithm == 5:
    requirePriority = True
else:
    requirePriority = False
if choiceOfAlgorithm == 6:
    timeQuantum = int(input("Please spcify the time quantum"))


#randomly generate those processes or colleting them from users
if isRandom == 'y' or isRandom == 'Y':

    #randomly generate the processes and put them into the ready queue
    burstRange = int(input("Please specify the CPU burst range from 0 to ?"))
    theReadyQueue = generateProcesses(numberOfProcesses,requirePriority, burstRange)
else:
    for i in range(numberOfProcesses):
        ProcessId = str(chr(65+i))
        print("Processes " + ProcessId + ": (burst time, arrive time, priority(if required) )")
        temp = input().split(",")
        if len(temp) == 2:
            theReadyQueue.append(Process(ProcessId, int(temp[0]), int(temp[1])))
        else:
            theReadyQueue.append(Process(ProcessId, int(temp[0]), int(temp[1]), int(temp[2])))


