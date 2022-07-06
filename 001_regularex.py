import re

rhand = open("test2.txt")
lhand = open("test.txt", "r", encoding="UTF-8")
# for line in rhand:
#     line = line.strip()
#     if line.startswith("From:"):
#         print(line)

# for line in rhand:
#     line = line.strip()
#     if re.search("^Fr.*:", line):
#         print(line)

# b = []
# for line in lhand:
#     line = line.strip()
#     y = re.findall("[0-9]+", line)
#     for x in y:
#         if x != []:
#             b.append(x)
# b.sort()
# print(b)
# b = []
# for line in rhand:
#     line = line.strip()
#     y = re.findall("\S+@\S+", line)
#     for x in y:
#         if x != []:
#             b.append(x)
#     for j in b:
#         g = " ".join(b)
# k = g.replace("<", "")
# h = k.replace(">", "")
# o = h.split()
# print(o)
#
# rhand = rhand.read()
# y = re.findall('^From .*@([^ ]*)', rhand)
# print(y)

numlist = list()
for line in rhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))



x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)



#Extracting Digits and Summing them
hand = open("regex_sum_1588816.txt")
numlist = []

for line in hand:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(sum(numlist))
