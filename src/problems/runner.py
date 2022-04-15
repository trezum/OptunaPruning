print('Starting')

import time

start = time.time()
import Ackley as Ackley
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