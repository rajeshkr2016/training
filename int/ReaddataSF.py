from collections import defaultdict
import re

def searchData(**txt):
    empl = defaultdict(list)
    with open("input.data") as data:
        for line in data.readlines():
            output = line.split(":")
            if re.match(r'idx', line):
                ocol=re.sub(r'\n','', output[1].strip())
                colnames=ocol.split(",")
                continue
            outputidx = output[0].strip()
            output1 = output[1].strip()
            output2 =output1.split(",")
            #print(colnames[0]+":"+ output2[0])
            if outputidx in empl[outputidx]:
                empl[outputidx].append({colnames[0].strip():output2[0].strip(),colnames[1].strip():output2[1].strip(),colnames[2].strip():output2[2].strip(),colnames[3].strip():output2[3].strip(),colnames[4].strip():output2[4].strip()})
            else:
                empl[outputidx]={colnames[0].strip(): output2[0].strip(), colnames[1].strip(): output2[1].strip(), colnames[2].strip(): output2[2].strip(), colnames[3].strip(): output2[3].strip(),colnames[4].strip(): output2[4].strip()}
    #print(empl)
    count=0
    for i in range(1,len(empl)+1):
        #print(empl[str(i)])
        for skey, svalue in txt.items():
            if skey in empl[str(i)] and svalue==empl[str(i)][skey]:
                count+=1
    if (count > 0):
        print("Value is present")
    else:
        print("value is not present")

searchData(fname="John")