#author: Issam Chaaraddine
#Write a python program called accounts.py 
#the program should read in a 10 character account number and outputs the account number with only the last 4 digits
#replace first 6 digits with 'x'
#first we will create a string that will read 'please enter a 10 digit number' using a built-in input() function
a = int(input('Please enter a 10 digit account number: '))
#we will give the variable 'b' the string value '1234567890'
b = "1234567890"
#we will replace the values in string '123456' by 'xxxxxx' using the built-in replace() function
x = b.replace('123456','xxxxxx')
print(x)
#extra, modify the program to deal with account numbers of any length
#first we will measure the length of variable 'b'
totalnumbers = len(b)
#we will create a variable 'numbershidden', it will represent all the numbers except the 4 last digits
numbershidden = totalnumbers - 4
#now a variable 'numbersshown'  that will make a shallow copy of the array and will be showing all numbers that are not included in 'numbershidden'
numbersshown = b[numbershidden:]
#now we will multiply(*) X by the digits hidden named variable 'numbershidden' and will add(+) the visible digits or 'numbersshown'
print("X" * numbershidden + numbersshown)
#I remplaced 'x' by 'X' to see the difference when running both programms 
