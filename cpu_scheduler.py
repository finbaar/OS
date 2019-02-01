from process import Process
import process
import services
from block import calculateBlocks, showResult
from copy import deepcopy


#ask the users for the type of services
prompt = "1.FIFO\n2.Preemtive SJF\n3.Nonpreemtive SJF\n4.preemtive Priority\n5.Nonpreemtive priority\n6.Round Robin\n"
choiceOfAlgorithm = int(input(prompt))

#ask for how many processes will be in the ready queue
numberOfProcesses = int(input("Please enter how many processes\n"))
#ask for users wehter or not they would like to type those processes themselves
isRandom = input("Enter y/Y to reandomly generat processes or other keys to continue\n")

theProcessPool = []

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
    burstRange = int(input("Please specify the CPU burst range from 0 to ?\n"))
    theProcessPool = process.generateProcesses(numberOfProcesses,requirePriority, burstRange)
else:
    for i in range(numberOfProcesses):
        ProcessId = str(chr(65+i))
        print("Processes " + ProcessId + ": (burst time, arrive time, priority(if required) )")
        temp = input().split(",")
        if len(temp) == 2:
            theProcessPool.append(Process(ProcessId, int(temp[0]), int(temp[1])))
        else:
            theProcessPool.append(Process(ProcessId, int(temp[0]), int(temp[1]), int(temp[2])))


#establish a dict for accesting the servicesses
processPool = deepcopy(theProcessPool)
askForServices = {1:services.FCFS,2:services.SJF_Preemptive}
askForServices.update({3:services.SJF_Nonpreemptive})
askForServices.update({4:services.Priority_Preemptive})
askForServices.update({5:services.Priority_Nonpreemptive})
askForServices.update({6:services.RoundRobin})

#execute the process pool:
if choiceOfAlgorithm != 6:
    executedRecord = askForServices[choiceOfAlgorithm](theProcessPool)
else:
    executedRecord = askForServices[choiceOfAlgorithm](theProcessPool,timeQuantum)
#dubug
#executedRecord = services.Priority_Preemptive(theProcessPool)

result = calculateBlocks(executedRecord,numberOfProcesses)

showResult(processPool, executedRecord, result)

