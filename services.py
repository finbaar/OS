from block import ExecutedBlock

def FCFS(processPoo):
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
    
    #the process arrives will be added to ready queue
    readyQueue = []
    while processPool or readyQueue:
        if processPool:
            currentProcess = processPool.pop(0)
            for slicedProcess in currentProcess.




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




def getkey(ob):
    """sort the ready queue according the burst time"""
    return ob.getBurstTime()


def SJF_Nonpreemptive(processPool):
    """a function that simulates the SJF services with nonpreemptive
       accept a processPool
 and return an exectution record
       the exectution record is just like a Gantt Chart"""
    timer = 0
    executionRecord = []

    processPool.sort(key=getkey)

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

    

