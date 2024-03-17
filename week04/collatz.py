#A python code based on collatz conjecture
#It prompts the user for a positive integer
#determines if the number is odd or even
#prints off the number sequence using the calculation below
#Author: Ebelechukwu Igwagu

#creates an empty list
numbers = []

#The line below prompts the  user for a number input
number = int(input("Enter a positive number: "))

#ensures that only a positive integer is entered
while number <= 0:
    print ("Please enter a positive integer: ")
    number = int(input("Enter a positive number: "))

#appends the initial number to the list
numbers.append(number) 

#defines the condition statement for generating the collatz sequence
while number != 1:    
    if  number % 2 == 0:    #applies to even numbers
       number = number// 2
    else:                   #applies to odd numbers
        number = (number * 3 + 1)
    numbers.append(number) #appends current number to the list
        
print (numbers)



