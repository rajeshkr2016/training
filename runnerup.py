n = 5
arr = [57,57,-57,57,-57]

a = max(arr)

for x in range(len(arr)-1,-1,-1):
    if arr[x] == a:
            arr.remove(arr[x])
print(max(arr))


# largest = max(arr)
#
# for i in range(n+1):
#     if largest == max(arr):
#         arr.remove(max(arr))
#
# print(max(arr))


# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
#
#     eerunnerup = ""
#     big = max(arr)
#     arr.pop(arr.index(big))
#     # print(big)
#     for i in range(n - 1):
#         if (eerunnerup == ""):
#             eerunnerup = arr[i]
#         # print(big)
#         # print(big)
#         # print(eerunnerup)
#         # if (eerunnerup > arr[i]) and (eerunnerup!=big):
#         if (arr[i] == big):
#             continue
#         if (arr[i] > eerunnerup) and (arr[i] != big):
#             eerunnerup = arr[i]
#
#     print(eerunnerup)
#     # print (arr)