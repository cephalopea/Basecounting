###explain a few things: different basic python operators, data types
#Let's start by making a function that can find the indices of a binary number.
#We'll start with five (or, in binary, 101), just because we have to start with something
#This will be easiest if we represent 101 in a list, like this: (1,0,1)
#This makes binary numbers into a list as described above.
###explain this bit
def make_list(binary):
    number = map(int,str(binary))
    return number

#First, we'll make the list. Let's call it five, because the binary number it represents equals 5.
five = make_list(101)

#Now, we'll start writing the function.
def find_indices_of_five():
    #First, we'll find the length of our list using len(). We'll name that length.
    length = len(five)
    #Next, we'll make a counter to keep track of how far into the list we are.
    counter = 1
    #Don't worry about this next bit just yet.
    indices = []
    #Next, we'll use a for each loop.
    #It does something with each piece of a list.
    #Here, it's going through each digit in our list called five we just made up there ^^^
    for digit in five:
        #We already have the length of our list and how far into the list we've gone: length and counter.
        #To get the index we need, we'll subtract counter from length.
        realSpot = (length - counter)
        #This is where "indices" from up there ^^^ comes in.
        #Right now, it's just an empty list, so we'll start adding stuff to it.
        #We'll use it to hold all the realSpots we make in the loop.
        indices.append(realSpot)
        #Each piece of the list will add its own realSpot to indices.
        #Last, we need to increase our counter, so that it'll stay the right size.
        counter = (counter + 1)
    #Printing something allows us to see it. It's a tool to see what your code is doing.
    #Take out the hashtag on (just) the next line to see the output of the function.
    #print(indices)
    #At the end of the loop, this function will return the finished list indices
    #This allows us to use indices later.
    return indices
    
#This line is what tells the function we made to actually run.
find_indices_of_five()

#That's good, but what if we want to find the indices of any number?
#We can make a function that's almost exactly like find_indices_of_five(), with a couple tweaks.
#We'll need to use arguments- these are basically variables you can plug in later.
#Add an argument by putting your variable name in the parentheses at the end of your function name.
def find_indices_of_number(number):
    #Add all the code we used in find_indices_of_five(), but replace 'five' with 'number'.
    length = len(number)
    counter = 1
    indices = []
    for digit in number:
        realSpot = (length - counter)
        indices.append(realSpot)
        counter = (counter + 1)
    #Take out the hashtag on (just) the next line to see the output of the function.
    #print(indices)
    return indices

#Let's try this out with eight and four:
eight = make_list(1000)
four = make_list(100)

find_indices_of_number(eight)
find_indices_of_number(four)
    

#Now we can use this function to write our last function- the one that actually does most of the math.
#This one will be much more straightforward, surprisingly.
#We need it to multiply each number by 2 to the power of its corresponding index.
#Exponents are written as 2**3 = 8 in Python.
def find_base_ten(binary):
    #First, we need the binary number and its indices.
    number = make_list(binary)
    indices = find_indices_of_number(number)
    #We'll also need something to keep track of how far into the lists we are, so let's make a new counter.
    #We'll set it to 0, because Python starts counting from 0 instead of 1.
    #That means the first thing in a list is thing 0, the second thing is thing 1, and so on.
    counter = 0
    #Last, we'll need a number to add on to.
    adder = 0
    #Next, we need to multiply each part of the number by its index- we can use a for each loop for that.
    for part in number:
        #This is the index of the number we're using
        index = indices[counter]
        #This multiplies a digit of the number by 2^index
        toAdd = part * 2**index
        #Add that total onto 'adder'
        adder = adder + toAdd
        #Don't forget to add to counter.
        counter = counter + 1
    print("Your binary number written in base ten is: ")
    print(adder)
    return adder

find_base_ten(1001)

#Okay, so that was a lot more work than doing one of these problems by hand.
#Unless you give it a number like 100010101001000101010010001010100010011111010101100101...

find_base_ten(100010101001000101010010001010100010011111010101100101)
    

