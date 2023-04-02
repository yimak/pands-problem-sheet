
# Hi, I'm Issam C.! 👋


# pands-problem-sheet
The first assignment is straight forward, but will use it to get familiar with Github and using a markup. After doing some reasearch I decided to go with readme **readme.so** Readme is a software easy to use, it offers all kind options when explaining an assignment and we can see the final document at the same time that we are writing our notes.


# Assignment 1: Hello World!

This file contains a python program that displays "Hello World!" when it is run.
This assignment was very straight forward. But I have to mention that getting there was a bit complicated. Working with a Macbook Air 2015 I realized that my python software needed an update as it was still running on an outdated version of python 2 and I need to update it to a compatible version. Through https://www.python.org/downloads/macos/ I downloaded the version of Python 3.9.6. Once done I still had two issues:
1.- I had to enable zsh instead of bash 
2.- Because I still had both versions of python on my computer and the old version was being exectued when executing python, I had to set python 3 as default from my terminal: 
$ alias python=/usr/bin/python3.9.6
then checked the version again: 
$ python --version
Python 3.9.6
It works!



## Author

- [@yimak](https://www.github.com/yimak)



# Assignment 2: Create a program named bank.py
a.-The program will prompt the user and read in two money amounts (in cent). 
b.-Add the two amounts.
c.-Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
I assigned n_1 to the first amount (65) and n_2 to the second amount (180). 
In order to make it prompt I used the function input() and put between quotation marks "amount 1: " and "amount 2: " respectively that will propmt to introduce the amounts. It was necessary to leave a space after the two points to have a space between the number and the two points once we introduce the number.
I was looking for a way to show the word "cents" after adding the amount but it didn't work, I decided to add a new command print print(f'{n_1} cent') after input. In this task I also decided to use the f-string, I believe this makes the syntax more elegant than using print(int(n_1), 'cent')
Because 1€ is 100 cents. We would just need to add n_1+n_2 and divide by 100. 


## Author

- [@yimak](https://www.github.com/yimak)



#Assignment 5: weekday.py

# Create a program named weekday.py 
Write a program that outputs whether or not today is a weekday.
If weekday, program will output 'Yes, unfortunately today is a weekday.'
If weekend, program will output 'It is the weekend, yay!'


First I needed to find a way to input today's date. 
For that we need to import date from datetime module, whih means that we will have today's exact date, that is:
from datetime import date
https://www.programiz.com/python-programming/datetime/current-datetime

Now we will create a variable that will define the date:
today = date.today()

I decided to use if -else statement combined with the boolean operator 'OR', so I included the 5 days of the week in the if statement next to the variable today and the == operator, that means that each time the day of the week 
To define that it can be any of these days I added the operator OR. Then we added print() right after, that means that if it's any of these values is True, then the string 'Yes, unfortunately today is a weekday.' will be printed.
Otherwise, if all these values are False, then we would jump to -else statement, which could be for Saturday or Sunday, we don't need to define those as we already defined the days Monday to Friday and any value that does not correspond to these will print the string 'It is the weekend, yay!'


## Author

- [@yimak](https://www.github.com/yimak)
