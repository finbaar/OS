from block import ExecutedBlock, mergeIdenticalBlock
from process import slicesProcesses



def getBursTime(ob):
    """sort the ready queue according to the burst time"""
    return ob.getBurstTime()

def getPriority(ob):
    """sort the ready queue according to the priority"""
    return ob.getPriority()

def FCFS(processPool):
    """a function that simulates the FCFS services
       accept a processPool
 and return an exectution record
       the exectution record is just like a Gantt Chart"""
    #count the current time
    timer = 0

    executionRecord = []
    for process in processPool:
        #execute the first process in the queue, and put it in the execution record,increase the timer
        executionRecord.append(ExecutedBlock(process, timer, timer + process.getBurstTime()))
        timer += process.getBurstTime()
        
    return executionRecord


def SJF_Preemptive(processPool):
    """a function that simulates the SJF services with preemptive
       accept a processPool
 and return an exectution record
       the exectution record is just like a Gantt Chart"""
    timer = 0
    executionRecord = []

    #the process arrives will be added to ready queue
    readyQueue = []
    while processPool or readyQueue:
        if processPool:
            readyQueue.append(processPool.pop(0))

        readyQueue.sort(key=getBursTime)

        #filt the process whose burst tiem is 0
        while readyQueue[0].getBursTime() == 0:
            del readyQueue[0]

        currentProcess = readyQueue[0]
        #add its chiled process into the record
        currentRecord = ExecutedBlock(currentProcess.getChildProcess(),timer, timer +1)    
        executionRecord.append(currentRecord)
        #decrease the burst time 
        currentProcess.decreaseBurstTime()
    
    return mergeIdenticalBlock(executionRecord)


def Priority_Preemptive(processPool):
    """a function that simulates the Priority services with preemptive
    accept a processPool and return an exectution record
    the exectution record is just like a Gantt Chart"""
    pass


def RoundRobin(processPool):
    """a function that simulates the Round Robin services
       accept a processPool
 and return an exectution record
       the exectution record is just like a Gantt Chart"""
    pass



def SJF_Nonpreemptive(processPool):
    """a function that simulates the SJF services with nonpreemptive
       accept a processPool
 and return an exectution record
       the exectution record is just like a Gantt Chart"""
    timer = 0
    executionRecord = []

    processPool.sort(key=getBursTime)

    for process in processPool:
        #execute the first process in the queue, and put it in the execution record,increase the timer
        executionRecord.append(ExecutedBlock(process, timer, timer + process.getBurstTime()))
        timer += process.getBurstTime()
        
    return executionRecord   


def Priority_Nonpreemptive(processPool):
    """a function that simulates the Priority services with nonpreemptive
    accept a processPool and return an exectution record
    the exectution record is just like a Gantt Chart"""
    #same as SJF_Nonpreemptive but sort the queue using priority
    pass

    

