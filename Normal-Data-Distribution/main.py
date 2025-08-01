#Three lines to make our compiler able to draw:
import sys
import matplotlib

matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

#Two  lines to make our compiler able to draw:
# use sys.stdout.buffer to display
# not work in replit
# plt.savefig(sys.stdout.buffer)

# use filename to save it, and after you can display it
# in the files, on the left
plt.savefig("matplotlib.png")
sys.stdout.flush()
