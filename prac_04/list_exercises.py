# 1.Basic list operations
data = []

for i in range(0, 5):
    data.append(float(input("Number: ")))

print("The first number is {}".format(data[0]))
# print("The last number is {}".format(data[len(data) - 1]))  emmm,not good,I forget that

print("The last number is {}".format(data[-1]))
print("The smallest number is {}".format(min(data)))
print("The largest number is {}".format(max(data)))

# sum = 0
# for i in data:
#     sum = sum + i
# sum = sum / 5

print("The average of the numbers is {}".format(sum(data) / len(data)))

# 2.Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']
if input("username: ") in usernames:
    print("Access granted")
else:
    print("Access denied")
