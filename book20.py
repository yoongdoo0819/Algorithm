# 문자열 재정렬

s = input()
sortedS = sorted(list(s))
print(sortedS)
newS = ""
sum = 0

for idx, char in enumerate(sortedS):
    if sortedS[idx].isdigit():
        sum += int(sortedS[idx])
    else:
        newS = sortedS[idx:]
        break

print(newS, sum)
print("".join(newS) + str(sum))