# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
firstMax = data[0]
secondMax = data[1]


def sol1():
    answer = 0
    count = 0
    
    for i in range(m):
        if count >= k:
            count = 0
            answer += secondMax
        else:
            answer += firstMax
            count += 1
    return answer
    
def sol2():
    answer = 0
    
    count = int(m/(k+1)) * k
    count += m % (k+1)
    
    answer += (count) * firstMax
    answer += (m - count) * secondMax
    return answer

print(sol1())
print(sol2())
