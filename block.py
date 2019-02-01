

class ExecutedBlock():
    """a class represent the process which has been executed"""
    def __init__(self, process, startTime, finishTime):
        self.process = process
        self.startTime = startTime
        self.endTime = finishTime

    def setStartTime(self, time):
        self.startTime = time
    
    def setEndTime(self, time):
        self.endTime = time

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime



def mergeIdenticalBlock(record):
    """merge the same block """

    mergedRecord = []

    pointer = 0
    while pointer < len(record):
        if pointer < len(record) - 1:
            currentBlock = record[pointer]
            nextBlock = record[pointer+1]
            #if the current block's process is same as next one, merge them
            if currentBlock.process == nextBlock.process:
                #merge the burst time
                mergedBurstTime = currentBlock.process.getBurstTime() + nextBlock.process.getBurstTime()
                currentBlock.process.setBurstTime(mergedBurstTime)
                #change the end Time of the current record
                currentBlock.setEndTime(nextBlock.getEndTime())
                #delete the next block and the index should remain unchanged
                del record[pointer+1]
                pointer -= 1
            else:
                mergedRecord.append(currentBlock)       
        else:
            #the last block is lost 
            mergedRecord.append(record[-1])

        pointer += 1

    return mergedRecord



def calculateBlocks(record, numberOfProcess):
    """evalute the average time for the executed blocks"""
    #indicaing how long the interval is since exectued last time
    lastExecutionTime = {}
    waitingTime = {}
    for i in range(numberOfProcess):
        processName = str(chr(65 + i))
        lastExecutionTime[processName] = i
        #keep tracing how long does each process waits
        waitingTime[processName] = 0

    for block in record:
        cureentProcess = block.process.getName()
        #add the waiting time 
        waitingTime[cureentProcess] += (block.getStartTime() - lastExecutionTime[cureentProcess])
        #update the interval's start Time
        lastExecutionTime[cureentProcess] = block.getEndTime()
    
    averageWaitingTime = sum(waitingTime.values()) / numberOfProcess  
    
    return (averageWaitingTime, waitingTime)


def showResult(processPool,record, result):
    """show the executed block in Gannt Char form"""
    #extract the result
    averageTime = result[0]
    waitingTimeDict = result[1]

    print("\n\n----------------------------------")

    print("         Name    BT  AT  priority ")
    for item in processPool:
        print(item)
    print("----------------------------------")

    print("\nThe calculation is shown below\n\n")
    #print out the Gannt char
    for item in record:
        print("|",end = '')
        print(item.startTime,end='--- ')
        print(item.process.getName(),end=' ---')
        print(item.endTime,end='')
        print("|",end = '')
    
    #print out the waiting time for each process
    print('\n')
    for process in waitingTimeDict.keys():
        print("The waiting time for " + process + " is " + str(waitingTimeDict[process]))
    
    print("The average watiting time is " + str(averageTime))

    