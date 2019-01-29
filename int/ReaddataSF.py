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
def insertData():
    empl = defaultdict(list)
    with open("input.data") as data:
        for line in data.readlines():
            output = line.split(":")
            if re.match(r'idx', line):
                colnames=output[1].split(",")
                continue

            outputidx = output[0]
            output1 = output[1]

            # print(outputidx)
            #print(output1)
            output2 =output1.split(",")
            #print(colnames[0]+":"+ output2[0])
            empl[outputidx]={colnames[0]:output2[0],colnames[1]:output2[1],colnames[2]:output2[2],colnames[3]:output2[3],colnames[4]:output2[4]}

                # print(item)
            # if outputidx in empl[outputidx]:
            #     #empl[outputidx].append(outputidx)
            #     for value in output1.split(","):
            #         if field in empl[outputidx][field]:
            #             empl[outputidx][field].append(value)
            #         else:
            #             empl[outputidx][field]=value
            # else:
                #empl[outputidx] = outputidx
                # for field,value in output1.split(","):
                #     if field in empl[outputidx][field]:
                #         empl[outputidx][field].append(value)
                #     else:
                #         empl[outputidx][field]=value
    print(empl)

def search(**txt):
    for skey, svalue in txt.items():
        if skey in empl and svalue==empl[skey]:
            print("Value is present")

#search(fname="xyz")

insertData()