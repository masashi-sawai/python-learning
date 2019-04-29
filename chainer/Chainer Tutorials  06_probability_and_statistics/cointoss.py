from random import randint
from decimal import Decimal
from prettytable import PrettyTable
import numpy as np


def tossBiasedCoin():
    """ Returns 0 or 1 with 0 having 2/3 chance """
    return randint(0, 2) % 2

# Make a 2x2 array
counts = [[0 for j in range(2)] for i in range(2)]

# Toss a coin many times to get counts
sampleCount = 500000
for num in range(sampleCount):
    first = tossBiasedCoin()
    second = tossBiasedCoin()
    counts[first][second] += 1

# Conert all counts to perentage
TWOPLACES = Decimal(10) ** -2
for i in range(2):
    for j in range(2):
        value = counts[i][j]
        counts[i][j] = (100 * Decimal(counts[i][j]) /
                        Decimal(sampleCount)).quantize(TWOPLACES)
        print("Converted the value {} to percentage {}".format(
            value, counts[i][j]))

# Make summaries of number of heads.
keys = np.arange(3)
values = [counts[0][0],
          counts[0][1] + counts[1][0],
          counts[1][1]]

# Add row descriptions
counts[0].insert(0, '1st tail')
counts[1].insert(0, '1st head')

# Create table with column descriptions, add rows, then show it.
table = PrettyTable(["", "2nd tail", "2nd head"])
table.padding_width = 1
table.add_row(counts[0])
table.add_row(counts[1])
print(table)

# Draw a bar chart
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
rects = plt.bar(keys,
                values,
                0.5,
                alpha=0.4,
                align="center",
                color='b')

plt.xlabel('Number of heads')
plt.ylabel('Probability (%)')
plt.title('Probabilities heads with a biased coin')
plt.xticks(keys, np.arange(3))

plt.tight_layout()
plt.show()
