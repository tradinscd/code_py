# Functions 101

# Create a function called printMax with the paramaters x and y.
def printMax(x, y):
    # if a is larger than b
    if x > y:
        # then print this
        print(x, 'is maximum')
    # if a is equal to b
    elif x == y:
        # print this
        print(x, 'is equal to', y)
    # otherwise
    else:
        # print this
        print(y, 'is maximum')

# Run the function with two arguments
printMax(3,4)

# Note: By default, variables created within functions are local to
# the function. But you can create a global function that IS defined outside
# the function.

# Create a variable called x
x = 50

# Create a function called func()
def func():
    # Create a global variable called x
    global x

    # Print this
    print('x is', x)
    # Set x to 2.
    x = 2
    # Print this
    print('Changed global x to', x)

# Run the func() function
func()

# Print x
print(x)
