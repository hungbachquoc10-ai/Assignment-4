def great_numbers():
    numbers = []
    print("Enter numbers one by one(Press Enter on an empty line to finish).")
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            x = float(user_input)
            numbers.append(x)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    numbers.sort(reverse=True)
    top_five = numbers[:5]
    print("--- Results ---")
    if top_five:
        print("The five greatest numbers (descending):")
        for i in top_five:
            print(i)
    else:
        print("No numbers were entered.")       
if __name__ == "__main__":  
    great_numbers()