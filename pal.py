def palindrome(number):
    original_no=number

    print(f"The original Number is {original_no}")
    reverse_num=0
        
    while number > 0:
        reminder=reverse_num % 10
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
    if original_no== reverse_num:
        print(f"This  {reverse_num}  is palindrome")
    else :
        print("it is not palindrome")

print(palindrome(111))