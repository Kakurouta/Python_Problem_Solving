import math

def minTime(machines, goal):
    minday = (math.ceil(goal/len(machines)))*min(machines)
    maxday = (math.ceil(goal/len(machines)))*max(machines)
    while minday < maxday:
        output = 0
        est = (minday + maxday)//2

        for j in machines:
            output += est//j
        if output >= goal:
            maxday = est
        else:
            minday = est + 1
    return minday