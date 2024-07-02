# program1.py

def gcd_on(a, b):
   
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd_euclidean(a, b):

    while b:
        a, b = b, a % b
    return a

def main():
   
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    gcd_on_result = gcd_on(a, b)
    gcd_euclidean_result = gcd_euclidean(a, b)

    print(f"GCD of {a} and {b} using O(N) approach is: {gcd_on_result}")
    print(f"GCD of {a} and {b} using Euclidean approach is: {gcd_euclidean_result}")

if __name__ == "__main__":
    main()
