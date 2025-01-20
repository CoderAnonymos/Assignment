import os

#Open the file

with(open('Sample_file.txt', 'w') as Sample):

    Sample.write("Hi! My name is Mayo and I'm 10 yrs old. I was born on the 29th of November 2014. My favourite color is purple and my favourite food is pizza!")

#Split Content
with(open('Sample_file.txt', 'r') as Sample):

    words = Sample.read()
    splitting = words.split()

    print(splitting) #Print the list

#Printing if exists or not
if os.path.exists('My_File.txt'):
    print("'My_File.txt' exists")

else:
    print("'My_File.txt' does not exist")

#Appending file
with(open('Sample_File.txt', 'a')as Sample):

    Sample.write("PS: I'm RRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLLLLLLLLLLLYYYYYYYYYYYYYYYYYYYYYY SMART :)!")
    