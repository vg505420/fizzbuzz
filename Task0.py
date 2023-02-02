'''
Task0
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
'''
for i in range(1,101):

    a=i%3
    b=i%5
    status =i
    if a==0 and b ==0:
        status = "FizzBuzz"
    elif a==0:
        status = "Fizz"
    elif b==0:
        status = "Buzz"
    
    print(status)