# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# for i in numbers:
#     count=count+1
# print(count)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
count=0
while i<len(numbers):
    if numbers[i]<20 and numbers[i]>40:
        print(numbers[i])
        # count=count+1
        # print(count)
    
    i=i+1
