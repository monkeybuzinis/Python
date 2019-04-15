#7
for c in s:
    if c==" ":
        s=s.replace(c,"")
if s==s[::-1]:
    print("your sentence or word is a palindrome")
else:
    print("not")