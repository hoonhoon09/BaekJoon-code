num=input()
num= num.split()
num=list(map(int,num))

print((num[0]+num[1])%num[2])
print(((num[0]%num[2]) + (num[1]%num[2]))%num[2])
print((num[0]*num[1])%num[2])
print(((num[0]%num[2]) * (num[1]%num[2]))%num[2]) 