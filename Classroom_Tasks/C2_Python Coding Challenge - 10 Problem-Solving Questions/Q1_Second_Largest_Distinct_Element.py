numbers=[12,35,1,10,34,35]
highest= None
second_highest= None

for num in numbers:
    if highest==None:
        highest=num
        continue

    if num>highest:
        second_highest=highest
        highest=num
    elif num!=highest and (second_highest==None or num>=second_highest):
            second_highest=num
            
if second_highest==None:
    print("No second-largest distinct value found!")
    
print("Second highest:", second_highest)