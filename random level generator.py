import gd
from gd.api import Object
from gd.api import Editor
import random
dieobjs = [14, 37, 42, 79, 100, 102, 104, 108, 112, 189, 191, 214, 221, 262, 276, 288, 290, 292, 298, 300, 302, 306, 308, 310, 312, 316, 318, 322, 330, 332, 334, 338, 340, 344, 346, 350, 352, 354, 356, 359, 379, 400, 415, 423, 717, 743, 746, 748, 750, 760, 776, 834, 849, 851, 858, 860, 864, 875, 879, 892, 897, 912, 922, 962, 978, 993, 1008, 1023, 1072, 1119, 1121, 1128, 1211, 1321, 1323, 1335, 1396, 1465, 1474, 1497, 1508, 1541, 1570, 1822]
stinky = []
# the object generation
for i in range(100):
    poo_stinker = random.randint(1, 420)
    if poo_stinker in dieobjs:
        continue
    randomx = random.randint(0,10000)
    randomy = random.randint(0,300)
    obj = Object(id=poo_stinker, x=randomx, y=randomy, groups={0})
    string = obj.dump()
    stinky.append(";"+string)


print("".join(stinky))

