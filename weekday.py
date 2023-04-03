#Author: Issam Chaaraddine
#Weekly task 5
#Write a program that outputs whether or not today is a weekday.
from datetime import date
today = date.today()
if today.weekday()==5 or today.weekday()==6:
    print('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday')