#Write a Python class for a simple calculator that can perform 
#addition, subtraction, multiplication, and division.

class Math:
    def add(self,num1,num2):
        return num1+num2

    def subtraction(self,num1,num2):
        return num1-num2


math=Math()

print("the addition of this two numbers are ",math.add(2,3))
print("the subtraction of this two numbers are ",math.subtraction(2,2))