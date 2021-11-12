# 상하좌우

n = int(input())
data = list(input().split())

print(n, data)

currentLocation = [1, 1]  
def sol():  
    for loc in data:
        if loc == 'U':
            if currentLocation[0] - 1 <= 0:
                print("U fail")
            else:
                currentLocation[0] -= 1
        elif loc == 'D':
            if currentLocation[0] > n:
                print("D fail")
            else:
                currentLocation[0] += 1
        elif loc == 'L':
            if currentLocation[1] <= 0:
                print("L fail")
            else:
                currentLocation[1] -= 1
        elif loc == 'R':
            if currentLocation[1] > n:
                print("R fail")
            else:
                currentLocation[1] += 1
            
sol()
print(currentLocation)