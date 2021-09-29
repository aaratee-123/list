list1 = [10, 20, 4, 45, 99]
secondLargest = list1[0]
largest = list1[0]
for i in range(len(list1)):
    if list1[i] > largest:
        largest = list1[i]
 
for i in range(len(list1)):
    if list1[i] > secondLargest and list1[i] != largest:
        secondLargest = list1[i]
print(secondLargest)
 