from random import randint, sample


class Process():
    """A class represents a process, including attributes like id, burst time,
       arrive time and priority if provided"""

    def __init__(self, name, burstTime, arriveTime, priority=0):
        self.name = name
        self.burstTime = burstTime
        self.priority = priority
        self.arriveTime = arriveTime

    def setPriority(self, nums):
        self.priority = nums

    def __str__(self):
        stringBuilder = "Process " + self.name + " " + str(self.burstTime)
        stringBuilder += (" " + str(self.arriveTime) + " " + str(self.priority))
        return stringBuilder



def generateProcesses(nums, needPrioiry):
    """randomly generate n processes without priority,
       if priority is needed, the priority would be given randomly"""

    processList = []

    for i in range(nums):
        processList.append(Process(str(chr(65+i)), randint(0,20), i, 0))
    
    if needPrioiry:
        #randomly chose number from the set
        temp = sample(range(nums), nums)
        #set each process's priority accordingly
        for i in range(nums):
            processList[i].setPriority(temp[i])
    
    return processList



prompt = "1.FIFO\n2.Preemtive SJF\n3.Nonpreemtive SJF\n4.preemtive Priority\n5.Nonpreemtive priority\n6.Round Robin\n"
choiceOfAlgorithm = int(input(prompt))
numberOfProcesses = int(input("Please enter how many processes\n"))
isRandom = input("Enter y/Y to reandomly generat processes or other keys to continue\n")

theReadyQueue = []

if choiceOfAlgorithm == 4 or choiceOfAlgorithm == 5:
    requirePriority = True
else:
    requirePriority = False

if isRandom == 'y' or isRandom == 'Y':
    #randomly generate the processes and put them into the ready queue
    theReadyQueue = generateProcesses(numberOfProcesses,requirePriority)
else:
    for i in range(numberOfProcesses):
        ProcessId = str(chr(65+i))
        print("Processes " + ProcessId + ": (burst time, arrive time, priority(if required) )")
        temp = input().split(",")
        if len(temp) == 2:
            theReadyQueue.append(Process(ProcessId, int(temp[0]), int(temp[1])))
        else:
            theReadyQueue.append(Process(ProcessId, int(temp[0]), int(temp[1]), int(temp[2])))


for item in theReadyQueue:
    print(item)