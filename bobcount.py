#parameters
s = 'azcbobobegghakl'
vowelcount = 0
bobcount = 0
letter = 'a'
stringfinal = ''
stringbuild = ''

#vowelcount
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowelcount = vowelcount + 1

print(vowelcount)

#bobcount

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        bobcount = bobcount + 1
print(bobcount)
    
#longestsubsequentletters

for i in range(len(s)):
    if s[i] == 'a':
        stringbuild += letter
        stringfinal = stringfinal + stringbuild
    else:
        stringbuild = ''
    
print(i)