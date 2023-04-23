import sys
with open(sys.argv[1]) as my_file:
    text=my_file.read()
    count=0
    for letter in text: #iterate through word
        if letter == "e": #if "letter" is a vowel, increment
            count += 1
print(count)
sys.exit()