

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

    def getBurstTime(self):
        return self.burstTime
