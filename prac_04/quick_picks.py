import random

MINNUM = 0
MAXNUM = 45
NUMBERS_PER_LINE = 6

line_number = int(input("How many quick picks? "))
for i in range(line_number):
    line = []
    for j in range(NUMBERS_PER_LINE):
        line.append(random.randint(MINNUM, MAXNUM))
    line.sort()
    # Traditional
    # for j in range(len(line)):
    #     print("{:>2}".format(line[j]),end=' ')
    # print()

    # list_comprehensions
    print(" ".join("{:2}".format(number) for number in line))
