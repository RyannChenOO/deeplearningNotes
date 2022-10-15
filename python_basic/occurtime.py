
def find_occurTime1(mytuple):
    '''
    找出数字中仅出现一次的数，其余均出现两次
    :param mytuple:
    :return:
    '''
    mylist = []
    max_num = mytuple[0]
    for i in range(1,len(mytuple)):
        max_num = max(max_num,mytuple[i])
    for i in range(max_num+1):
        mylist.append(0)
    for each in mytuple:
        mylist[each] += 1
    for i in range(len(mylist)):
        if mylist[i] == 1:
            return i

def find_occurTime2(mytuple):
    '''
    找出数字中仅出现一次的数，其余均出现两次
    :param mytuple:
    :return:
    '''
    res = []
    mylist = []
    max_num = mytuple[0]
    for i in range(1,len(mytuple)):
        max_num = max(max_num,mytuple[i])
    for i in range(max_num+1):
        mylist.append(0)
    for each in mytuple:
        mylist[each] += 1
    for i in range(len(mylist)):
        if mylist[i] == 1:
            res.append(i)
            if len(res)==2:
                return res
print(find_occurTime2((9,9,8,8,7,7,6,5)))