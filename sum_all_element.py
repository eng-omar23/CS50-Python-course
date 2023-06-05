def sum_of_element(element):
    result=0
    for e in element:
        result+=e
    return result


my_list=[1,2,3,4,5]
x=sum_of_element(my_list)
print("the sum of all element is :  ",format(x))
