def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def gcd_three(a, b, c):
    gcd_ab, x1, y1 = gcd_extended(a, b)
    gcd_abc, x2, y2 = gcd_extended(gcd_ab, c)
    return gcd_abc, x1 * x2, y1 * x2, y2

def find_solution(A, B, C, D):
    gcd, x1, y1, z = gcd_three(A, B, C)
    
    if D % gcd != 0:
        return None
    
    scale = D // gcd
    a = x1 * scale
    b = y1 * scale
    c = z * scale
    
    return a, b, c

def main():
    A = int(input("Enter value for A: "))
    B = int(input("Enter value for B: "))
    C = int(input("Enter value for C: "))
    D = int(input("Enter value for D: "))
    
    solution = find_solution(A, B, C, D)
    
    if solution:
        a, b, c = solution
        print(f"Solution: a = {a}, b = {b}, c = {c}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
