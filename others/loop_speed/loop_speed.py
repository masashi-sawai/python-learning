import time
from tqdm import tqdm

start = time.time()
cnt = 0
sumation = 0
LIMIT = 1000000

print("-------------------------------")

with tqdm() as pbar:
    while(cnt < LIMIT):
        sumation += cnt
        pbar.update(1)
        cnt += 1

elapsed_time = time.time() - start
print("while_time:{0}".format(elapsed_time) + "[sec]")

start = time.time()
cnt = 0
sumation = 0

print("-------------------------------")

for cnt in tqdm(range(LIMIT)):
    sumation += cnt

elapsed_time = time.time() - start
print("for_time:{0}".format(elapsed_time) + "[sec]")
