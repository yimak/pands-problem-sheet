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
It worked!


## Author

- [@yimak](https://www.github.com/yimak)



#Assignment 2: bank.py

# Create a program named bank.py
a.-The program will prompt the user and read in two money amounts (in cent). b.-Add the two amounts. c.-Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
I assigned n_1 to the first amount (65) and n_2 to the second amount (180). 
In order to make it prompt I used the function input() and put between quotation marks "amount 1: " and "amount 2: " respectively that will propmt to introduce the amounts. It was necessary to leave a space after the two points to have a space between the number and the two points once we introduce the number.
I was looking for a way to show the word "cents" after adding the amount but it didn't work, I decided to add a new command print print(f'{n_1} cent') after input. In this task I also decided to use the f-string, I believe this makes the syntax more elegant than using print(int(n_1), 'cent')
Because 1€ is 100 cents. We would just need to add n_1+n_2 and divide by 100. 


