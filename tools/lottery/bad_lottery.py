import csv
import random

list_lottery = []
csv_file = open("./sample.csv", "r", encoding="ms932",
                errors="", newline="")
f = csv.reader(csv_file, delimiter=",", doublequote=True,
               lineterminator="\r\n", quotechar='"', skipinitialspace=True)
for row in f:
    list_lottery.append([row[0], row[1]])
list_win = random.sample(list_lottery, 5)
print(list_win)
