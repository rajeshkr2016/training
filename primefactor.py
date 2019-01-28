
'''
Given int x, determine the set of prime factors
f(5) = [1,5]
f(6) = [2,3]
f(8) = [2,2,2]
f(10) = [2,5]
'''

# def primefactors(n):
#     prime=[]
#     for i in range(1,n):
#         print(i)
#         if (n%i==0):
#             prime.append(int(p1))
#             prime.append(i)
#         #print (p1)
#         #r = n//i
#         #print(r)
#     return prime
#
# primefactors(16)

def prime(integer):
    primelist = []
    integer=int(integer)
    factorlist = []
    for number in range(1,int(integer)+1):
        #factorlist = []
        #for i in range(1, number + 1):
        print(number)
        if (integer % number == 0):
            factorlist.append(number)
            # To see if newp is a prime
        while factorlist:
            if (len(factorlist) > 2):
                if (factorlist[fitem]==integer):
                    factorlist.pop(fitem)
                # if (factorlist[fitem]==1):
                #     factorlist.pop(fitem)

        #if factorlist == [1, number]:
        #   primelist.append(number)


            # print primelist
    # print factorlist
    #print ('The largest prime number of ', integer, 'is ', primelist[-1])
    print ('Prime Factor List:',factorlist)
    # return integer


prime(input('Enter value: '))