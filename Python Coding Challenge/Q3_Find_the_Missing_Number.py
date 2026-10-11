numbers=[1,2,4,6,3,7,8]
last_num=0
expected_sum=0
numbers_sum=0

for n in numbers:
    numbers_sum +=n
    if n>=last_num:
        last_num=n
print("Entered elements include distinct numbers from 1 to", last_num)

for i in range(1,last_num+1):
    expected_sum +=i
if expected_sum==numbers_sum:
    print("No number is missing")
else:
    missing_num= expected_sum-numbers_sum
    print("Missing number:", missing_num)
