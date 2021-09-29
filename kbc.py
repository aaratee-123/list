year=int(input("enter the year"))
month=int(input("enter the month"))
day=int(input("enter the day"))

# if  year and (month==4 or month==6 or month==9 or month==11) and(day>=1 or year<=30):
#     print(year,month ,day)

# elif year and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==11)and (day>=1 or day<=31):
#     print(year,month,day)
month1=0
if (year%4==0 or year%400==0):
    year=True
    month1=29
    print("yes")
else:
    year=False
    print("no")
if month1 in [1,3,5,7,8,10,12] :
    days=31
elif month1 in [4,6,9,11]:
    day=30
a=(year,month,day+1)
print("the next date is ",a)

# user=input("enter the name")
# i=0
# k='_'
# while i<len(user):
#     j=0
#     while j<1:
#         print(user.upper()[i]+user.lower()[i]*(i),k*(i),end="")
#         if i==0:
#             print(k,end="")
#         j=j+1
#     i=i+1

num_list=[1,2,3,4,5]
d=dic={}
# dic={}
for i in num_list:
    dic[i] = {}
    dic = dic[i]
print(d)

 
