m=input("Enter the message")
k=input("Enter the key")
l=len(k)
n=[ord(i) for i in k]
mn=[ord(i) for i in m]
d=''
for i in range(len(mn)):
        x = (mn[i] + n[i % l]) % 26
        d = d+ chr(x + 65)
print(d)