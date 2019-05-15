import time
import numpy

image = numpy.ones((100000000), dtype=numpy.float32)
sumation = 0
length = len(image)
start = time.time()
for i in range(length):
    image[i] = int(image[i])
elapsed_time = time.time() - start
print("1_time:{0}".format(elapsed_time) + "[sec]")

list1 = None

start = time.time()
list(map(int, image))
elapsed_time = time.time() - start
print("2_time:{0}".format(elapsed_time) + "[sec]")
