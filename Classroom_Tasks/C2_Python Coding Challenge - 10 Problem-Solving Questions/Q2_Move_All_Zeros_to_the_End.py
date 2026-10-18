numbers=[0,1,0,3,12,0,5]
modified_list=[]
zero_count=0

for num in numbers:
    if num==0:
        zero_count +=1
    else:
        modified_list.append(num)

for i in range (zero_count):
    modified_list.append(0)

print("Original list:", numbers)
print ("Modified list:", modified_list)