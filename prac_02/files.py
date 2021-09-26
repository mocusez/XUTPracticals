
name = input("What's your name? ")
# file = file + ".txt"
files = open(name + ".txt", 'w')
print(name, file=files)
files.close()

files = open(name + ".txt", 'r')
print("Your name is "+files.readline())
files.close()

total = 0
with open("numbers.txt", 'r') as files:
    for i in range(2):
        total = total+int(files.readline())
print(total)
