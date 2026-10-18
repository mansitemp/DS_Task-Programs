numbers=[]
modified_list=[]
sum=0
highest_square=0
total_elements=int(input("Enter total number of elements to be entered:"))

for n in range(total_elements):
    element= int(input("Enter an element:"))
    numbers.append(element)

for i in numbers:
    if i>=0 and i%2==0:
        modified_list.append(i)
print("List after ignoring negatives and keeping even numbers:", modified_list)

for n in modified_list:
    if (n*n)>highest_square:
        highest_square=n*n
        sum +=(n*n)

print("Total:", sum)
print("Count of squared values:", len(modified_list))
print("Largest squared value:", highest_square)
