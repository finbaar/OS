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

    def getName(self):
        return self.name

    def getPriority(self):
        return self.priority
    
    def getArriveTime(self):
        return self.getArriveTime

    def getBurstTime(self):
        return self.burstTime
 

    def __str__(self):
        stringBuilder = "Process " + self.name + " " + str(self.burstTime)
        stringBuilder += (" " + str(self.arriveTime) + " " + str(self.priority))
        return stringBuilder



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

   
