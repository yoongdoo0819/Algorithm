# 스택

n = int(input())
inst_set = []
stack = []
for i in range(n):
    inst_set.append(input())
    
for i in range(n):
    inst = inst_set[i].split()
    if inst[0] == 'push':
        stack.append(int(inst[1]))
    elif inst[0] == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif inst[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif inst[0] == 'size':
        print(len(stack))
    elif inst[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

