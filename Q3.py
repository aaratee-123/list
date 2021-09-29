# a = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# n=a[0]
# i=0
# while i<len(a):
#   if a[i]>a[0]:
#     print(a[i])
#   i=i+1

name=input("enter the name")
i=0
for i in name:
      if i=="a" or i=="e" or i=="o" or i=="i" or i=="u":
            print(name[i],end="")
      else:
            print("cosonat")
