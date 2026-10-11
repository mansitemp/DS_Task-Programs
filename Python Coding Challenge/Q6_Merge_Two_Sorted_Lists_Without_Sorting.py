a=[1,4,7,10]
b=[2,3,8,11,15]
sorted_list=[]
if len(a)>=len(b):
    for i in range(len(a)-1):
        if a[i]>b[i]:
            sorted_list.append(b[i])
            sorted_list.append(a[i])
        else:
             sorted_list.append(a[i])
             sorted_list.append(b[i])

else:
    for i in range(len(b)-1):
            if a[i]>b[i]:
                sorted_list.append(b[i])
                sorted_list.append(a[i])
            else:
                 sorted_list.append(a[i])
                 sorted_list.append(b[i])

print("Sorted List:" ,sorted_list)