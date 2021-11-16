# 럭키 스트레이트

n = int(input())

s = str(n)
print(s)

a = list(map(int, s[0:len(s)//2]))
b = list(map(int, s[len(s)//2:]))
print(a, b)
leftSum = sum(a)
rightSum = sum(b)

if leftSum == rightSum:
    print('LUCKEY')
else:
    print('READY')
