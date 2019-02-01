from block import ExecutedBlock, mergeIdenticalBlock
from process import slicesProcesses



def getBurstTime(ob):
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
    decreaseTime = 1
    while processPool or readyQueue:
        if processPool:
            readyQueue.append(processPool.pop(0))

        readyQueue.sort(key=getBurstTime)

        currentProcess = readyQueue[0]
        #add its chiled process into the record
        currentRecord = ExecutedBlock(currentProcess.getChildProcess(),timer, timer +1)    
        executionRecord.append(currentRecord)
        #decrease the burst time 
        currentProcess.decreaseBurstTime(decreaseTime)
        timer += 1
        #filt the process whose burst tiem is 0
        while readyQueue and readyQueue[0].getBurstTime() == 0:
            del readyQueue[0]

    #return mergeIdenticalBlock(executionRecord)
    return executionRecord


def Priority_Preemptive(processPool):
    """a function that simulates the Priority services with preemptive
        accept a processPool and return an exectution record
        the exectution record is just like a Gantt Chart"""
    timer = 0
    executionRecord = []

    #the process arrives will be added to ready queue
    readyQueue = []
    decreaseTime = 1
    while processPool or readyQueue:
        if processPool:
            readyQueue.append(processPool.pop(0))

        readyQueue.sort(key=getPriority)

        currentProcess = readyQueue[0]
        #add its chiled process into the record
        currentRecord = ExecutedBlock(currentProcess.getChildProcess(),timer, timer +1)    
        executionRecord.append(currentRecord)
        #decrease the burst time 
        currentProcess.decreaseBurstTime(decreaseTime)
        timer += 1
        #filt the process whose burst tiem is 0
        while readyQueue and readyQueue[0].getBurstTime() == 0:
            del readyQueue[0]

    return mergeIdenticalBlock(executionRecord)


def RoundRobin(processPool, timeQuantum):
    """a function that simulates the Round Robin services
        accept a processPool
        and return an exectution record
        the exectution record is just like a Gantt Chart"""
    timer = 0
    executionRecord = []

    readyQueue = processPool
    decreaseTime = timeQuantum

    #pointer refer to which process is currently pointing at
    pointer = 0
    while readyQueue:
        #check if there are any processes left the queue
        queueSizeRemain = True

        currentProcess = readyQueue[pointer]
        currentBurstTime = currentProcess.getBurstTime()
        actualBurstTime = min(currentBurstTime, decreaseTime)
        childProcess = currentProcess.getChildProcess()
        childProcess.setBurstTime(actualBurstTime)
        currentRecord = ExecutedBlock(childProcess,timer,timer + actualBurstTime)
        currentProcess.decreaseBurstTime(actualBurstTime)
        timer += actualBurstTime
        executionRecord.append(currentRecord)

        while readyQueue and readyQueue[pointer].getBurstTime() == 0:
            del readyQueue[pointer]
            queueSizeRemain = False
            break

        #if the size changed, then current pointer will point to next process automaticlly
        if queueSizeRemain:
            pointer += 1

        #if pointer points the end, the go back to the start
        #there is an exception, that's the queue's size changed
        if (pointer == len(readyQueue) and queueSizeRemain) or len(readyQueue) == 1:
            pointer = 0

    return executionRecord


def SJF_Nonpreemptive(processPool):
    """a function that simulates the SJF services with nonpreemptive
        accept a processPool
        and return an exectution record
        the exectution record is just like a Gantt Chart"""
    timer = 0
    executionRecord = []

    processPool.sort(key=getBurstTime)

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
    timer = 0
    executionRecord = []

    processPool.sort(key=getPriority)

    for process in processPool:
        #execute the first process in the queue, and put it in the execution record,increase the timer
        executionRecord.append(ExecutedBlock(process, timer, timer + process.getBurstTime()))
        timer += process.getBurstTime()
        
    return executionRecord   

    

