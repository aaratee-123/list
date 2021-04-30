# ek code likho jo kisi bhi list ke liye output karta hai ki us list me kitne 
# odd numbers or kitne even number hai.
# element=[23,14,56,12,19,9,15,25,31,42,43]

element=[23,14,56,12,19,9,15,25,31,42,43]
even=0
odd=0
i=0
while i<len(element):
    m=element[i]
    if m%2==0:
        print("even=",element[i])
        even=even+1
    else:
        print("odd=",element[i])
        odd=odd+1
    i=i+1
print("even numbers=",even)
print("odd numbers=",odd)
    