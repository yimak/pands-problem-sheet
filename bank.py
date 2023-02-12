#bank.py
#author: Issam Chaaraddine
#prompt the user and read two money amounts in cent
n_1 = int(input('amount 1: '))
#is there a way to create a command where the amount populates plus the word "cent"?
#I tried different things on the same command, ended up adding a second command
print(f'{n_1} cent')
n_2 = int(input('amount 2: '))
print(f'{n_2} cent')
#add both and get results in euro
ameuro = print('The sum of these is 'f'{(n_1+n_2)/100} €')