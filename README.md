
# Hi, I'm Issam C.! 👋


# pands-problem-sheet
The first assignment is straight forward, but will use it to get familiar with Github and using a markup. After doing some reasearch I decided to go with readme **readme.so** Readme is a software easy to use, it offers all kind options when explaining an assignment and we can see the final document at the same time that we are writing our notes.


# Assignment 1: Hello World!

This file contains a python program that displays <tt>"Hello World!"</tt> when it is run.
This assignment was very straight forward. But I have to mention that getting there was a bit complicated. Working with a Macbook Air 2015 I realized that my python software needed an update as it was still running on an outdated version of python 2 and I need to update it to a compatible version. Through https://www.python.org/downloads/macos/ I downloaded the version of Python 3.9.6. Once done I still had two issues:
1.- I had to enable <tt>zsh</tt> instead of <tt>bash</tt> 
2.- Because I still had both versions of python on my computer and the old version was being exectued when executing python, I had to set python 3 as default from my terminal: 
<tt>$ alias python=/usr/bin/python3.9.6</tt>
then checked the version again: 
<tt>$ python --version</tt>
Python 3.9.6
It works!



## Author

- [@yimak](https://www.github.com/yimak)



# **Assignment 2: Create a program named <tt>bank.py</tt>**
a.-The program will prompt the user and read in two money amounts (in cent). 
b.-Add the two amounts.
c.-Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
I assigned <tt>n_1</tt> to the first amount (65) and <tt>n_2</tt> to the second amount (180). 
In order to make it prompt I used the function <tt>input()</tt> and put between quotation marks <tt>amount 1: </tt> and <tt>amount 2: </tt> respectively that will propmt to introduce the amounts. It was necessary to leave a space after the two points to have a space between the number and the two points once we introduce the number.
I was looking for a way to show the word "cents" after adding the amount but it didn't work, I decided to add a new command print <tt>print(f'{n_1} cent')</tt> after <tt>input()</tt>. In this task I also decided to try f-string, I believe this makes the syntax more elegant than using <tt>print(int(n_1), 'cent')</tt>
Because 1€ is 100 cents. We would just need to add <tt>n_1+n_2</tt> and divide by 100. 


## Author

- [@yimak](https://www.github.com/yimak)




# **Assignment 3: Create a program called <tt>accounts.py</tt>** 

#The program should read in a 10 character account number and outputs the account number with only the last 4 digits
replace first 6 digits with 'x'

First we will create a string that will read <tt>'please enter a 10 digit number'</tt> using a built-in <tt>input()</tt> function:
The <tt>input()</tt> function was taken from the previous lecture.
<tt>a = str(input('Please enter a 10 digit account number: '))</tt>
We will use the slicing method to show only the last 4 digits starting to count from the right by putting -4 followed by two dots: 
<tt>numbersshown1 = a[-4:]</tt>

https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
https://docs.python.org/3/reference/expressions.html#

We will replace the values in string <tt>'123456'</tt> by <tt>'xxxxxx'</tt> by multiplying 'X' by 6 and adding the value resulting from leaving the last four digits of value <tt>a</tt>: 
<tt>numbershidden1 = 'X' * 6 + numbersshown1</tt> 
<tt>print(numbershidden1)</tt>

#extra, modify the program to deal with account numbers of any length.
First we will create a string that will read <tt>'please enter the digits of your account number'</tt> using a built-in <tt>input()</tt> function.
Then we will measure the length of 'a' by using <tt>len()</tt> function:
<tt>totalnumbers = len(a)</tt>
We will create a variable <tt>numbershidden</tt>, it will represent all the numbers (that is, of any length) except for the 4 last digits:
<tt>numbershidden = totalnumbers - 4</tt>
Now a variable <tt>numbersshown</tt>  that will make a shallow copy of the array and will be showing all numbers that are not included in <tt>numbershidden</tt>
<tt>numbersshown = b[numbershidden:]</tt>
Now we will multiply(*) X by the digits hidden named <tt>numbershidden</tt> and will add(+) the visible digits or <tt>numbersshown</tt>:
<tt>print("X" * numbershidden + numbersshown)</tt>


## Author

- [@yimak](https://www.github.com/yimak)


#   **Assignment 4: create a program called <tt>collatz.py</tt>**
#write a program that asks the user to input any positive integer and outputs the successive values of the following calculation:
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

First we started this assignmnent by creating an input function, the value introduced after the sentence should be an integer <tt>int()</tt> because we will be conducting math calculations, which can be only done using integers.  
<tt>number=int(input('Please enter a positive integer:'))</tt>

Because we need to do the same calculation on a loop, we used a while function: 
<tt>while number > 1</tt>:
The loop will continue until number reaches 1, once there, the function would then print:
<tt>print("at the end the value is ",number)</tt>
Now we will settle a rule for our loop using if else statement learned in the lecture. So each time number's remainder is 0 (that is, an even number) we will divide by two. 
For that we had to find a way to separate even from odd numbers and we used modulo operator <tt>%</tt>:
https://www.tutorialspoint.com/python-program-to-split-the-even-and-odd-elements-into-two-different-lists#:~:text=Step%201%20%3A%20create%20a%20user,add%20to%20the%20odd%20list.
https://realpython.com/python-modulo-operator/

Any other number that resulted from the loop right before divided by 2 that has a different remainder than 0 (!=0) should be multiplied by 3 plus 1: 

<tt>if(number%2) == 0:</tt>
      <tt>number = number/2</tt>
<tt>else number = number*3+1</tt>

Then we add <tt>print()</tt> to print out each value that resulted from each loop. To print out the values next to each other I used <tt>end=''</tt> 
https://pythonhow.com/how/print-without-a-newline-or-space-in-python/#:~:text=To%20print%20without%20a%20newline%20or%20space%20in%20Python%2C%20you,of%20the%20default%20newline%20character.&text=This%20will%20produce%20the%20same%20output%20as%20the%20previous%20examples.

## Author

- [@yimak](https://www.github.com/yimak)


# **Assignment 5: Create a program named <tt>weekday.py</tt>** 
Write a program that outputs whether or not today is a weekday.
If weekday, program will output <tt>'Yes, unfortunately today is a weekday.'</tt>
If weekend, program will output <tt>'It is the weekend, yay!'</tt>


First I needed to find a way to input today's date. 
For that we need to import date from datetime module, whih means that we will have today's exact date, that is:
<tt>from datetime import date</tt>
https://www.programiz.com/python-programming/datetime/current-datetime

<tt>Date</tt>,date is an object that represents the actual Gregorian date. Every time an object is created a method (method is basically a function that belongs to an object) is called and it's named constructor, in this case we used the constructors <tt>today()</tt> and <tt>weekday()</tt>. 
https://docs.python.org/3/library/datetime.html
https://pythonbasics.org/constructor/
https://docs.python.org/3/tutorial/classes.html#:~:text=A%20method%20is%20a%20function,%2C%20sort%2C%20and%20so%20on. (method defini)

Now we will create a variable that will define the object date:
<tt>today = date.today()</tt>

I decided to use <tt>if -else</tt> statement combined with the boolean operator <tt>'OR'</tt>, so I included the 5 days of the week in the if statement next to the variable today and added the constructor <tt>weekday()</tt>, <tt>weekday</tt> defines the days of the week assigning each day a number that go from 0 (Monday) to 6 (Sunday).
Then I added the numbers next to the <tt>==</tt> operator, that means that today's date will be <tt>True</tt> whenever the number of the weekday is equal to one of the numbers I added which go from 0 to 4 (Mon - Fri)
To define that it can be only one of these days I added the boolean operator <tt>OR</tt>:
https://realpython.com/python-or-operator/#:~:text=In%20short%2C%20the%20Python%20or,regardless%20of%20its%20truth%20value.&text=In%20this%20example%2C%20the%20Python,how%20or%20works%20in%20Python.
Then we added <tt>print()</tt> right after, that means that if any of these values is <tt>True</tt>, then the string that contains <tt>'Yes, unfortunately today is a weekday.'</tt> will be printed.
Otherwise, if all these values are <tt>False</tt>, then we would jump to <tt>-else</tt> statement, which could be Saturday or Sunday, we don't need to define those as we already defined the days Monday to Friday and any value that does not correspond to these will print the string <tt>'It is the weekend, yay!'</tt>
When I finished this program I realised that I could invert it to make it shorter, that means instead of assigning the five days of the week to a number, I could actually just assign Saturday to (5) and Sunday (6). That is:
Instead of:
<tt>if today.weekday()==0 or today.weekday()==1 or today.weekday()=2 or today.weekday()==3 or today.weekday()==4:</tt>
    <tt>print('Yes, unfortunately today is a weekday')</tt>
<tt>else:</tt>
    <tt>print('It is the weekend, yay!')</tt>
<tt>Better:</tt>
<tt>if today.weekday()==5 or today.weekday()==6:</tt>
    <tt>print('It is the weekend, yay!')</tt>
<tt>else:</tt>
    <tt>print('Yes, unfortunately today is a weekday')</tt>

## Author

- [@yimak](https://www.github.com/yimak)



# **Assignment 6: create a program named <tt>squareroot.py</tt>**

Create a function called <tt>sqrt</tt> that takes a positive floating number and outputs an approximation of his square root
This task should be done without using a built in function <tt>x</tt> ** or <tt>math.sqrt(x)</tt>

The first task was to search for the Newton Method to estimate a square root and undertanding how the formula works.
- Newton method calculates a square root using different formulas but I found this one to be the easiest one to represent on our program later:
- <tt>root = 0.5 * (approx + (N / approx))</tt> where approx is any guess which can be assumed to be 1 (a later explanation will follow once we create the program).
 https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  

We will assign a number to the variable <tt>N</tt>. <tt>N</tt> decribes the value we are trying to find the square root of, in this case 14.5:
<tt>N=14.5</tt>
Then we will assign a value to <tt>sqrt</tt>:
<tt>sqrt: 1+N</tt>
We will create a variable called <tt>approx</tt>, this value can be any positive number, in this case I assigned it to 1. <tt>sqrt</tt> and approx must hold different values because they will be used in the while loop parameter as different in order to create a loop:
<tt>approx=1</tt>
If <tt>N</tt> was an integer, we would assign the formula to <tt>sqrt</tt> and <tt>print(sqrt)</tt>. But working with a float number makes it more complicated. 
The reason is that the number resulted from that formula is just an estimated number, but close to the exact square root of <tt>N</tt>. 
In order to get a lower tolerance, that is, a more accurate square root number, we will create a loop, so that everytime we get a value for <tt>sqrt</tt> we will run it through the same formula in a loop decreasing the tolerance of the square root number of <tt>N</tt>. 
The loop will stop once <tt>sqrt</tt> and <tt>approx</tt> will have the same value with an accuracy of 0.0000000000000001 decimals.
To create a loop I used <tt>while()</tt> loop statement: 
<tt>while (squrt!approx):</tt>
https://www.w3schools.com/python/python_while_loops.asp
https://snakify.org/en/lessons/while_loop/
then gave <tt>approx</tt> the same value that will result from calculating <tt>squrt</tt>:
<tt>approx=squrt</tt>
Please bare in mind that this <tt>sqrt</tt> and <tt>approx</tt> created in the while loop statement are independent from the approx and squrt created outside and will represent different numbers.
Approx will alwasys be equal to the value of <tt>sqrt</tt>, that is, approx will be equal to the last value that results from <tt>sqrt</tt>. 
Now we will create the variable <tt>sqrt</tt> that will designate Newton's Method to estimate a square root:
<tt>squrt=0.5 * (approx + (N / approx))</tt>
As long as the result of <tt>sqrt</tt> is dfferent than <tt>approx</tt>, the loop will continue until <tt>sqrt</tt> and <tt>approx</tt> have the same value on a level of 0.0000000000000001 decimals. 
By defining a new parameter <tt>if</tt> <tt>continue</tt> once both values are equal the loop will end and <tt>sqrt</tt> will be printed:
<tt>print(sqrt)</tt> 
I afterwards realised that by taking out <tt>if</tt> <tt>continue</tt> the result would still print, I guess any exception to <tt>approx!=sqrt</tt> will pass the loop and get printed. 
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


# **Assignment 7: create a program named <tt>es.py</tt>**

Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

To understand this assignment I had to make a research on how to read files from a command argument, this article provides all the necessary information on how <tt>import sys</tt> works:
https://www.pythonforbeginners.com/system/python-sys-argv
https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
https://stackoverflow.com/questions/8280250/how-to-open-files-given-as-command-line-arguments-in-python
once we understand that <tt>argv.sys</tt> stores the arguments and file name that we want to read we start creating our program:
<tt>import sys</tt>
<tt>sys.argv[1] = my_file</tt>
the first element that <tt>sys.argv[0]</tt> will read is the script itself, the reason why we will write it at index 1, remember that the arguments in the command line will follow this order:
<tt>python es.py tiktok.txt</tt>
Now we need to find a function to open and close the file, python has two build-in fucntions:
https://www.w3schools.com/python/python_file_open.asp 
After some research I found an elegant way to open and close files using the with statement:
<tt>with open(sys.argv[1]) as my_file:</tt>
https://builtin.com/software-engineering-perspectives/what-is-with-statement-python
Apart of opening and closing the file, we need to read the file, that's why we will use <tt>read()</tt>. I have to recognize that this method has been added to the script after finishing it, I was getting value 0 when running the script:
<tt>text=my_file.read()</tt> 
Now we will wwork on the second part of the task, which is counting the number of times the letter "e" will appear in our text:
https://www.programiz.com/python-programming/if-elif-else#:~:text=The%20syntax%20of%20if%20statement,body%20of%20if%20is%20skipped.
For that we will use the for loops combined with an <tt>if</tt> statement, basically each time we have the letter "e" in <tt>my_file</tt> the body count will add one.  
<tt>count=0</tt> 
    <tt>for letter in my_file:</tt> 
        <tt>if letter == "e":</tt> 
            <tt>count += 1</tt> 
Of course at the end we need to print count, wich will represent be the number of times "e" appears in the text.
Something that is very important to mention is, the document added should be added to the same directory where the script is running.

## Author

- [@yimak](https://www.github.com/yimak)



# Assignment 8: Create a program named <tt>plottask.py</tt>
This program should display a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.
And a plot of the function h(x)=x3 in the range [0, 10], 
on the one set of axes.

First we will import numpy and matplotlib and will assign them to np and plt respectively:
<tt>import numpy as np</tt> 
<tt>import matplotlib.pyplot as plt</tt> 
Through the article logistic distribution in W3Schools we could find a script to create a histogram with the 1000 values (<tt>size</tt> ) , mean=5 (that is, <tt>loc</tt> ), and standard deviation(<tt>scale</tt> ) of 2:
https://www.w3schools.com/python/numpy/numpy_random_logistic.asp
<tt>data = np.random.normal(loc=5, scale=2, size=1000)</tt> 
Now we will create the a plot of the function  h(x)=x3 in the range [0, 10], becasue the range is so small, the line will be dashed. But the more we increase the range the line the more the line will look continuous: 
<tt>xpoint=np.random.normal(range(0,10))</tt> 
<tt>ypoint= xpoint ** 3</tt> 
I didn't add a reference for this part because I used the lecture as a reference. I just assigned <tt>Y</tt>  axis to <tt>X</tt> cubed and assigned the range to the X axis.

To make my presentation more clear, I changed the colour of the plot, added a legend, and separated the bars by adding the edges a white colour:
<tt>plt.hist(data,edgecolor='white')</tt> 
<tt>plt.plot(xpoint,ypoint,color='red', label='plotfunction')</tt> 
https://stackoverflow.com/questions/70416097/adding-data-labels-ontop-of-my-histogram-python-matplotlib

This task was very straight forward, most of the points have been treated in the lectures, the reason why I didn't add many references.

## Author

- [@yimak](https://www.github.com/yimak)


