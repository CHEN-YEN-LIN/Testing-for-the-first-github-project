theroundofthenumber=int(input())
for i in range(0,theroundofthenumber):
    inputnumber=list(float(x) for x in input().split())
    thedis=max(inputnumber)-min(inputnumber)
    print("%.2f"%thedis)


# a=[]
# for i in range(1,9):
#     randnumber = random.randrange(0,9)
#     print(randnumber,end="")
#     a.append(str(randnumber))
#     if i == 3:
#         print("-",end="")
#         a.append("-")
#     if i == 5:
#         print("-",end="")
#         a.append("-")
# theanswer=a[0]
# for i in range(1,10):
#     theanswer+=a[i]
# print()
# print(theanswer,type(theanswer))

# firstlist=[]
# secondlist=[]
# thirdlist=[]
# fourthlist=[]

# def c():
#     firstlist.append("  ___  ")
#     secondlist.append(" /   \ ")
#     thirdlist.append("|     |")
#     fourthlist.append(" \___/ ")

# def t():
#     firstlist.append("")

# c()
# print(firstlist)
# print(secondlist)
# print(thirdlist)
# print(fourthlist)