def get_max_min(lst):
    print(f"The list of numbers {lst}")
    if len(lst) < 0 :
        return None
    else :
        smallest=min(lst)
        largest=max(lst)
        result ="the smalllest number is ", smallest ,
        "and the largest numbers is ", 
        largest
    return result
list_of_number=[1,2,3,4,4,5,9] 
result=get_max_min(list_of_number)
print("The Result",result)
