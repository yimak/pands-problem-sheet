#author: Issam Chaaraddine
#Write a python program called accounts.py 
#the program should read in a 10 character account number and outputs the account number with only the last 4 digits, replace the first 6 digits with 'x'
a = str(input('Please enter a 10 digit account number: '))
numbersshown1 = a[-4:]
numbershidden1 = 'X' * 6 + numbersshown1 
print(numbershidden1)

# Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
a = str(input('Please enter the digits of your account number: '))
totalnumbers = len(a)
numbershidden = totalnumbers - 4
numbersshown = a[numbershidden:]
print("X" * numbershidden + numbersshown)
