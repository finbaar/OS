from block import ExecutedBlock

def FCFS(readyQueue):
    """a function that simulates the FCFS services
       accept a readyQueue and return an exectution record
       the exectution record is just like a Gantt Chart"""
    #count the current time
    timer = 0

    executionRecord = []
    for process in readyQueue:
        #execute the first process in the queue, and put it in the execution record,increase the timer
        executionRecord.append(ExecutedBlock(process, timer, timer + process.getBurstTime()))
        timer += process.getBurstTime()
        
    return executionRecord


def SJF(readyQueue):
    """a function that simulates the SJF services
       accept a readyQueue and return an exectution record
       the exectution record is just like a Gantt Chart"""
    pass


def Priority(readyQueue):
    """a function that simulates the Priority services
    accept a readyQueue and return an exectution record
    the exectution record is just like a Gantt Chart"""
    pass

def RoundRobin(readyQueue):
    """a function that simulates the Round Robin services
       accept a readyQueue and return an exectution record
       the exectution record is just like a Gantt Chart"""
    

