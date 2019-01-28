from collections import defaultdict
import re
# def readData(sep):
#     with open("input.data") as data:
#          for line in data:
#              print(line)
#              output=line.split(":")
#              output1=output[1]
#              outputidx=output[0]
#              with open("output.data","w") as odata:
#                  odata.write(outputidx+sep+output1)
#
#
# readData("-")


def search(**txt):
    empl = defaultdict(list)
    with open("input.data") as data:
        for line in data.readlines():
            if re.match(r'idx',line):
                continue
            output = line.split(":")
            output1 = output[1]
            outputidx = output[0]
            if outputidx in empl[outputidx]:
                empl[outputidx].append(output1)
            else:
                empl[outputidx] = output1
            print(empl)

    for skey, svalue in txt.items():
        if skey in empl and svalue==empl[skey]:
            print("Value is present")


search(fname="xyz")