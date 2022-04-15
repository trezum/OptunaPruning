print('Starting')

import time

from AckleyProblem import Ackley

start = time.time()

end = time.time()
print('Imported {}'.format(end-start))

start = time.time()
p1 = Ackley()
end = time.time()
print('Ackley created {}'.format(end-start))

start = time.time()
p1.draw()
end = time.time()
print('Done {}'.format(end-start))