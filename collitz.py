#Author: Issam Chaaraddine
#write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
number=int(input('Please enter a positive integer:'))
while number > 1:
   if(number%2) == 0:
      number = number/2
   else:
      number = number*3+1
   print(number, end=' ')
print ("at the end the value is ",number)