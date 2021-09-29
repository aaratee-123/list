a=[[4,5,6],8,[6,7,9],7,[4,16,8]]
for i in range(len(a)):
    n=a[i]
    if type(n)==list:
        for j in range(len(n)):
                t=n[j]
                if t%2==0:
                    print(t,"even")
                else:
                    print(t,"odd")
    else:
        if n%2==0:
            print(n,"even")
        else:
            print(n,"odd")
# for i in range(len(a)):
#     n=a[i]
#     if type(n)==list:
#         for j in range(len(n)):
#             t=n[j]
#             max=n[0]
#             if t>max:
#                 max=t
#             print(max)
            

