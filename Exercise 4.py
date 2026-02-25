def sum_calculator(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
def main():
    print("Enter your numbers separated by spaces (e.s: 5 10 15):")
    try:
        user_input = input("> ")
        string_list = user_input.split()
        integer_list = [int(item) for item in string_list]
        total = sum_calculator(integer_list)
        print(f"The sum of your numbers is: {total}") 
    except ValueError:
        print("Error: Please only enter integer numbers separated by spaces.")
if __name__ == "__main__":
    main()