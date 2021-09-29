# max without max function
list=[45,6,78,56,45,23]
max = list[0]
for x in list:
    if x > max:
        max = x
print (max)


numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=numbers[0]
i=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print("max",max)

#second maximum
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=numbers[0]
sec_max=numbers[0]
i=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    if numbers[i]>sec_max and numbers[i]!=max:
        sec_max=numbers[i]
    i=i+1
print("sec_max",sec_max)

