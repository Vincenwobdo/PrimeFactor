def name_triangle(input):
    k = 2 * len(input) - 2
    for index, letter in enumerate(input): #here we start with index[0] and letter "m"
        print(letter)
        for j in range(0, k):
            print(end=" ")

            # decrementing k after each loop
        k = k - 1

        for i in range(0, index +1):
            print( f'{letter}',end=" ")


            #ending line after each row
            #print("\r")

name_triangle('madagascar')

"""
So first we want to get make sure we get from the string that we are passing to the function an index and value .
- How can we do the above on a string?
Next for every index we want to print the value contained in that index location and the value(s) in indexes before it.
- How can we do this? 

"""