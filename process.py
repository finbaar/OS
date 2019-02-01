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

    def setBurstTime(self, time):
        self.burstTime = time
    
    def decreaseBurstTime(self,decreasedTime):
        self.burstTime -= decreasedTime

    def getChildProcess(self):
        #generate a process with the same value but burst time is set to 1
        return Process(self.name,1,self.arriveTime,self.priority)

    def getName(self):
        return self.name

    def getPriority(self):
        return self.priority
    
    def getArriveTime(self):
        return self.getArriveTime

    def getBurstTime(self):
        return self.burstTime
 

    def __str__(self):
        stringBuilder = "Process    " + self.name + " \t" + str(self.burstTime)
        stringBuilder += ("\t" + str(self.arriveTime) + "\t" + str(self.priority))
        return stringBuilder

    def __eq__(self, other):
        """Overrides the default implementation"""
        if self.name == other.name:
            return True
        return False



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


def slicesProcesses(process):
    """slicing a processes into a serial of processes which has the same nema
        priority and arrive time, but the burst time would always be 1"""
    slicedProcesses = []

    while process.getBurstTime != 0:
        process.decreaseBurstTime()
        slicedProcesses.append(process.getChildProcess())
        
    return slicedProcesses
    

   
