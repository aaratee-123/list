#sort list without sort function

my_list = [23,45,20,2,5,6]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)



# def sort(list):
#     for index in range(1,len(list)):
#         value = list[index]
#         i = index-1
#         while i>=0:
#             if value < list[i]:
#                 list[i+1] = list[i]
#                 list[i] = value
#                 i -= 1
#             else:
#                 break