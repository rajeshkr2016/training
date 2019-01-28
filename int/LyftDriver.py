# Input:
# 3 # No of drivers (100k) - 24 hours
# 8,10
# 9,11
# 15,19
#
# 2 # Queries (m)
# 15.5 # Time1
# 9.5 # Time2
# Output
# 1
# 2
from collections import defaultdict

drivers_avail = [[8, 10], [9, 11], [15, 19]]

new_drivers_avail_dict = {}

query_list = [15.5, 9.5]

for hour in range(0,24, 1):
    #print(hour)
    count=0
    for drv in drivers_avail:
        print(hour,"-",str(drv))
        if  drv[0] <= hour <= drv[1]:
            count+=1
            print(count)
            if hour in new_drivers_avail_dict:
                new_drivers_avail_dict[str(hour)].append(count)
            else:
                new_drivers_avail_dict[str(hour)]=count

print(new_drivers_avail_dict)

# for query in query_list: # m
#     print("Query:",query)
#     count=0
#     for drv in drivers_avail.: # n
#         if drv[0] < query and drv[1] > query:
#             count+=1
#     print(count)

# m*n