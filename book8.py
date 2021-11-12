# 시각

n = int(input())
count = 0

for h in range(n+1):
    
    for m in range(60):
        
        for s in range(60):
            
            strH = str(h)
            strM = str(m)
            strS = str(s)
            
            if '3' in strH or '3' in strM or '3' in strS:
                count += 1
            
                
print(count)