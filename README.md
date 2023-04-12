
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




# Assignment 5: Create a program named weekday.py 
Write a program that outputs whether or not today is a weekday.
If weekday, program will output 'Yes, unfortunately today is a weekday.'
If weekend, program will output 'It is the weekend, yay!'


First I needed to find a way to input today's date. 
For that we need to import date from datetime module, whih means that we will have today's exact date, that is:
from datetime import date
https://www.programiz.com/python-programming/datetime/current-datetime

from datetime import date
Date,date is an object that represents the actual Gregorian date. Every time an object is created a method (method is basically a function that belongs to an object) is called and it's named constructor, in this case we used the constructors today() and weekday(). 
https://docs.python.org/3/library/datetime.html
https://pythonbasics.org/constructor/
https://docs.python.org/3/tutorial/classes.html#:~:text=A%20method%20is%20a%20function,%2C%20sort%2C%20and%20so%20on. (method defini)

Now we will create a variable that will define the object date:
today = date.today()

I decided to use if -else statement combined with the boolean operator 'OR', so I included the 5 days of the week in the if statement next to the variable today and added the constructor weekday(), weekday defines the days of the week assigning each day a number that go from 0 (Monday) to 6 (Sunday).
Then I added the numbers next to the == operator, that means that today's date will be True whenever the number of the weekday is equal to one of the numbers I added which go from 0 to 4 (Mon - Fri)
To define that it can be only one of these days I added the boolean operator OR:
https://realpython.com/python-or-operator/#:~:text=In%20short%2C%20the%20Python%20or,regardless%20of%20its%20truth%20value.&text=In%20this%20example%2C%20the%20Python,how%20or%20works%20in%20Python.
Then we added print() right after, that means that if any of these values is True, then the string that contains 'Yes, unfortunately today is a weekday.' will be printed.
Otherwise, if all these values are False, then we would jump to -else statement, which could be Saturday or Sunday, we don't need to define those as we already defined the days Monday to Friday and any value that does not correspond to these will print the string 'It is the weekend, yay!'
When I finished this program I realised that I could invert it to make it shorter, that means instead of assigning the five days of the week to a number, I could actually just assign Saturday to (5) and Sunday (6). That is:
Instead of:
if today.weekday()==0 or today.weekday()==1 or today.weekday()=2 or today.weekday()==3 or today.weekday()==4:
    print('Yes, unfortunately today is a weekday')
else:
    print('It is the weekend, yay!')
Better:
if today.weekday()==5 or today.weekday()==6:
    print('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday')

## Author

- [@yimak](https://www.github.com/yimak)



# Assignment 6: create a program named squareroot.py

Create a function called <tt>sqrt</tt> that takes a positive floating number and outputs an approximation of his square root
This task should be done without using a built in function x ** or math.sqrt(x)

The first task was to search for the Newton Method to estimate a square root and undertanding how the formula works.
- Newton method calculates a square root using different formulas but I found this one to be the easiest one to represent on our program later:
- root = 0.5 * (approx + (N / approx)) where approx is any guess which can be assumed to be 1 (a later explanation will follow once we create the program).
 https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  

We will assign a number to the variable N. N decribes the value we are trying to find the square root of, in this case 14.5:
N=14.5
Then we will assign a value to <tt>sqrt</tt>:
<tt>sqrt: 1+N</tt>
We will create a variable called <tt>approx</tt>, this value can be any positive number, in this case I assigned it to 1. <tt>sqrt</tt> and approx must hold different values because they will be used in the while loop parameter as different in order to create a loop:
<tt>approx=1</tt>
If N was an integer, we would assign the formula to <tt>sqrt</tt> and <tt>print(sqrt)</tt>. But working with a float number makes it more complicated. 
The reason is that the number resulted from that formula is just an estimated number, but close to the exact square root of N. In order to get a lower tolerance, that is, a more accurate square root number, we will create a loop, so that everytime we get a value for <tt>sqrt</tt> we will run it through the same formula in a loop decreasing the tolerance of the square root number of N. 
The loop will stop once <tt>sqrt</tt> and <tt>approx</tt> will have the same value with an accuracy of 0.0000000000000001 decimals.
To create a loop I used while() loop statement: 
<tt>while (squrt!approx):</tt>
https://www.w3schools.com/python/python_while_loops.asp
https://snakify.org/en/lessons/while_loop/
then gave <tt>approx</tt> the same value that will result from calculating squrt:
<tt>approx=squrt</tt>
Please bare in mind that this <tt>sqrt</tt> and <tt>approx</tt> created in the while loop statement are independent from the approx and squrt created outside and will represent different numbers.
Approx will alwasys be equal to the value of <tt>sqrt</tt>, that is, approx will be equal to the last value that results from <tt>sqrt</tt>. 
Now we will create the variable <tt>sqrt</tt> that will designate Newton's Method to estimate a square root:
<tt>squrt=0.5 * (approx + (N / approx))</tt>
As long as the result of <tt>sqrt</tt> is dfferent than <tt>approx</tt>, the loop will continue until <tt>sqrt</tt> and <tt>approx</tt> have the same value on a level of 0.0000000000000001 decimals. 
By defining a new parameter <tt>if</tt> <tt>continue</tt> once both values are equal the loop will end and <tt>sqrt</tt> will be printed:
<tt>print(sqrt)</tt> 
I afterwards realised that by taking out <tt>if</tt> <tt>continue</tt> the result would still print, I guess any exception to approx!=sqrt will pass the loop and get printed. 
This assignment took me a while to understand, especially the way <tt>while()</tt>  operated. 
The key for me to understand how it works was by adding <tt>print()</tt> right after <tt>approx=sqrt</tt>, this way I could see how the function works and the result of each loop:
2
4.625
3.8800675675675675
3.8085579457341536
3.8078866121102966
3.8078865529319543
3.8078865529319543 

## Author

- [@yimak](https://www.github.com/yimak)

# Assignment 7: create a program named es.py

Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

To understand this assignment I had to make a research on how to read files from a command argument, this article provides all the necessary information on how import sys works:
https://www.pythonforbeginners.com/system/python-sys-argv
https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
once we understand that argv.sys stores the arguments and file name that we want to read we start creting our program:
import sys
sys.argv[1] = my_file 
the first element that sys.argv[0] will read is the script itself, the reason why we will write it at index 1, remember that the arguments in the command line will follow this order:
python es.py tiktok.txt
Now we need to find a function to open and close the file, python has two build-in fucntions:
https://www.w3schools.com/python/python_file_open.asp 
After some research I found an elegant way to open and close files using the with statement:
with open(sys.argv[1]) as my_file:
https://builtin.com/software-engineering-perspectives/what-is-with-statement-python
Apart of opening and closing the file, we need to read the file, that's why we will use read(). I have to recognize that this method has been added to the script after finishing it, I was getting value 0 when running the script:
text=my_file.read() 
Now we will wwork on the second part of the task, which is counting the number of times the letter "e" will appear in our text:
https://www.programiz.com/python-programming/if-elif-else#:~:text=The%20syntax%20of%20if%20statement,body%20of%20if%20is%20skipped.
For that we will use the for loops combined with an if statement, basically each time we have the letter "e" in my_file the body count will add one.  
count=0
    for letter in my_file:
        if letter == "e":
            count += 1
Of course at the end we need to print count, wich will represent be the number of times "e" appears in the text.
Something that is very important to mention is, the document added should be added to the same directory where the script iis running.
