import sys
from newYorkCrawl import newYorkCrawl
from BaseThread import BaseThread
from MyJsonDecoder import MyJsonDecoder
import threading
import json
import time
nYC = newYorkCrawl()
year = sys.argv[1]
month = sys.argv[2]

fileName = "NYC_{}_{}.json".format(year,month)
append_fileName = "NYC_{}_{}.txt".format(year,month)

with open(append_fileName,'r',encoding='utf8') as f:
    data = []
    for line in f:
        data.append(line)

print(len(data))

for line in data:
    test = {}
    tmp = json.loads(line)
    if type(tmp) != type(test):
        print(type(tmp))


# print(len(tmp_data))
# seen = set()
# new_l = []
# for d in data:
#     t = tuple(d.items())
#     if t not in seen:
#         seen.add(t)
#         new_l.append(d)

# print(len(new_l))