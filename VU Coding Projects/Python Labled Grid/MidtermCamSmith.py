#Input how many rows and numbers the user wants
rowNum = int(input("How many rows do you want to display? " ))
colNum = int(input("How many columns do you want to display? " ))

#just a message to precede the output
print("Here is your table of rows and columns: ")

#Calculating how to center the word "COLUMN"
width = colNum * 4 #colX is 4 digits long

#if we subtract the length of the word we want from the width, it helps us decide how many spaces we need to center it (thanks 10th grade geometry!)
#then dividing the result by 3 gives us the spaces we need on both sides (bear with me on this one)
center = (width - len("COLUMNS")) // 3

#And this is the output for our COLUMN math
print("   " * center + "COLUMNS") #we are multiplying 2 spaces until we reach the center given to use by the previous functions
#and then it prints column, then gives the other half of the spaces

#When testing this, I found that dividing by 3, and adding an extra 2 spaces centered it a tad more than (cont.)
# Dividing by 2 with only 1 space. It kinda depends on the inputs, but oh well. 


#Nested for loops used with the 'in range' function
for i in range(1, rowNum + 1):
    print(f"row {i} ", end="") #prints the row with a space in between i and row
    #since the above function is the outer loop, it will only output once until the loop reiterates

    for j in range(1, colNum + 1):
        print(f"col{j}", end=" ") #same thing as before, but no space between j and col
        #since this function is in the inner loop, it keeps repeating until colNum is reached before going to a new line

    print() #moves to the next line after each row, so everything's not entirely horizontal
 


    

        
