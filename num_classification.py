def classify_number(numbers):
    even_numbers=[]
    odd_numbers=[]
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers
if __name__== "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list=[int(x) for x in user_input.split()]
    even_numbers, odd_numbers = classify_number(number_list)
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)
