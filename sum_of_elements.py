def sum_of_element(numbers, exclude_negatives=False):
    if exclude_negatives:
        numbers=[num for num in numbers if num>=0]
    return sum(numbers)
if __name__=="__main__":
    user_input=input("enter numbers: ")
    number_list = [int(x) for x in user_input.split()]
    exclude=input("exclude negatives? yes or no? ").strip().lower()
    exclude_negatives=exclude=="yes"
    final_sum=sum_of_element(number_list, exclude_negatives)
    if exclude_negatives:
        print("sum is: ", final_sum)
    else:
        print("sum is: ", final_sum)
