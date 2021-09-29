values = 'This is a sentence'
split_values = []
tmp  = ''
for words in values:
    if words == ' ':
        split_values.append(tmp)
        tmp = ''
    else:
        tmp += words
if tmp:
    split_values.append(tmp)
print(split_values)
