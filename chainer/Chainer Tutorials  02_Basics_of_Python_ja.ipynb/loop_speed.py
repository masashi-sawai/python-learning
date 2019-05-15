import time

start = time.time()
i=0
sumation=0
while(i<1000000):
    sumation += i
    i+=1
elapsed_time = time.time() - start
print ("while_time:{0}".format(elapsed_time) + "[sec]")

start = time.time()
i=0
sumation=0
for i in range(1000000):
    sumation+=i
elapsed_time = time.time() - start
print ("for_time:{0}".format(elapsed_time) + "[sec]")