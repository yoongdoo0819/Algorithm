# 선분 위의 점 (BOJ 11663)

from bisect import bisect_left, bisect_right
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
points = list(map(int, sys.stdin.readline().rstrip().split()))
points.sort()

for _ in range(M):
    point = list(map(int, sys.stdin.readline().rstrip().split()))
    point.sort()
    
    left_idx = bisect_left(points, point[0])
    right_idx = bisect_right(points, point[1])
    
    print(right_idx - left_idx)
    
"""
아래 코드는 bisect를 사용하지 않은 경우

def getNum(point):
    left, right = point[0], point[1]
    
    s, e = 0, len(points)-1
    while s <= e:
        mid = (s + e) // 2
        
        if points[mid] == left:
            s = mid
            break
        elif points[mid] > left:
            e = mid - 1
        else:
            s = mid + 1
    left_idx = s

    s, e = 0, len(points)-1
    while s <= e:
        mid = (s + e) // 2
        
        if points[mid] == right:
            e = mid
            break
        elif points[mid] < right:
            s = mid + 1
        else:
            e = mid - 1
    right_idx = e + 1
    
    print(right_idx - left_idx)

for _ in range(M):
    point = list(map(int, sys.stdin.readline().rstrip().split()))
    getNum(point)
    
"""