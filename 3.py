old_lst = [1,2,3,4,5,6,7]
# beginAt = len(old_lst)-1
# endAt = -1
# ChangeI = -1
# for i in range( beginAt , endAt , changeI):
#     print(i,":",old_lst[i])


lst = [item for item in reversed(old_lst) if item%2==0]
print(lst)


lst = ["t","h","o","i","o","n"]
lst = ["*" + item + "*" for item in lst]

lst.insert(0,1)
lst.insert(4,2)
lst.insert(3,3)
lst.insert(6,4)
lst.insert(60,4)
print(lst[7])
print(lst[6:8])
print(lst[0:6])

deletedItem = lst.pop(7)


middle = int(len(lst)/2)
firstPartOfLst = lst[:middle]
secondPartOfLst = lst[middle:]
print(firstPartOfLst)
print(secondPartOfLst)

lst.remove("*t*")
print(lst)



