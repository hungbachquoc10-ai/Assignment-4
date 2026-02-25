import math
def prime_number():
    try:
        x = int(input("Enter an integer to check: "))
        if x <= 1:
            print(f"{x} is not a prime number.")
            return
        prime_value = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                prime_value = False
                break
        if prime_value:
            print(f"{x} is a prime number!")
        else:
            print(f"{x} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")
prime_number()