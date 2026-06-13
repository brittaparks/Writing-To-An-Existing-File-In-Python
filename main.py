#I am adding a new line character at the beginning, because I remmeber not adding a 
#new line character to the end of the last line when I created the file.

with open("Python_code_1.txt", "a") as candy:
    candy.write("\nThis should make the third line")

#I used the word "candy" to demonstrate the lack of importannce of the chosen word for variable, 
#rather the importance of consistency in its use.
