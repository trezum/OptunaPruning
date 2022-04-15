import time
from AckleyProblem import Ackley
start = None
end = None

def printTimer(message):
    global start
    global end
    if start == None:
        start = time.time()
        print(message)
        return
    else:
        end = time.time()
        print(message+' {}'.format(end-start))
        start = end   
    
printTimer("Starting")
p1 = Ackley()
printTimer("AckleyCreated")
p1.draw()
printTimer("Done")