# Four Squares (BOJ 17626)

n = int(input())

def find_four_squares():
    square_root = n**0.5
    # if n == a * a:
    #     return 1
    if (n ** 0.5).is_integer():
        return 1
    
    for i in range(1, int(square_root)+1):
        if i**2 > n:
            break
        if ((n-i**2)**0.5).is_integer():
            return 2
    for i in range(1, int(square_root)+1):
        if i**2 > n:
            break
        for j in range(1, int((n-i**2)**0.5)+1):
            if i**2 + j**2 > n:
                break
            #if ((n - i ** 2 - j ** 2) ** 0.5).is_integer():
                # print(i ** 2 - j ** 2)
                # print(n**0.5)
                # print((n - i ** 2))
                # print((n - i ** 2 - j ** 2))
                # print((n - i ** 2 - j ** 2) ** 0.5)
                #return 3
            if ((n-(i**2 + j**2))**0.5).is_integer():
                #print((n-(i**2 + j**2)**0.5))
                return 3
            
    return 4

print(find_four_squares())