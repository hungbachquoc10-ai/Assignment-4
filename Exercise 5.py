def even_numbers_count(numbers):
    even_list = []
    for x in numbers:
        if x % 2 == 0:
            even_list.append(x)
    return even_list
def main():
    print("Type your numbers separated by spaces (e.s: 1 2 3 4 5):")
    try:
        raw_input = input("> ")
        original_list = [int(x) for x in raw_input.split()]
        cut_down_list = even_numbers_count(original_list)
        print("Results:")
        print(f"Original List: {original_list}")
        print(f"Cut-down List: {cut_down_list}")
    except ValueError:
        print("Error: Please only enter integer numbers and spaces.")
if __name__ == "__main__":
    main()