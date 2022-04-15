print('Starting')

import time

start = time.time()
import Ackley as ack
end = time.time()
print('Imported {}'.format(end-start))

start = time.time()
p1 = ack()
end = time.time()
print('Ackley created {}'.format(end-start))

start = time.time()
p1.draw()
end = time.time()
print('Done {}'.format(end-start))