d=input("Enter the Secret message")
k=input("Enter the key")
l=len(k)
n=[ord(i) for i in k]
dn=[ord(i) for i in d]
m=''
for i in range(len(dn)):
        x = (dn[i] - n[i % l]) % 26
        m = m+ chr(x + 65)
print(m)