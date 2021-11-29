# 괄호

t = int(input())
ps_list = []

for i in range(t):
    ps_list.append(input())
    
def check_vps(ps):

    stack = []
    for s in ps:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False    
            
    if not stack:
        return True
    else:
        return False
    
def all_check_vps():
    
    for i in range(t):
        ps = ps_list[i]
        if check_vps(ps) == True:
            print("YES")
        else:
            print("NO")
     
all_check_vps()   