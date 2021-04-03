# Count by 5's

# for x in range(5,1000,1) # start at 5 go till 1000 and count every number


# for x in range(5, 101, 5): # start at 5 go till 1000 and add 5 each iteration
    # print(x)

# for y in range(5, 101, 1):
#     if y % 5 == 0:
#         print(y)


def flexCount(lowNum, hiNum, mult):
    for i in range(lowNum, hiNum +1):
        if i % mult == 0:
            print(i)

# flexCount(2,9,3)

# l = 2
# h = 10
# m = 3

# for i in range(2,10):
#     if i % m == 0:
#         print(i)

def add(a,b):
    x = a + b
    print(x)
    return x

# add(2,4)

def a():
    return 5

# print(a())

def a():  
    return 5

# print(a()+a())

def a(b,c):
    print(b + c)
    # return b + c # adding in this line would allow it to actually concatonate the print 

# print(a(1,2) + a(2,3))

# Return statement means STOP no more instructions will follow me

def a():
    return 5
    print(10)

# print(a())

# if we change the above to the following it will print 10 and 5
def a():
    print(10)
    return 5

# print(a())

def dojoWay():
    for i in range(1, 101):
        if i % 10 == 0: # if true follow my instructions if false move on
            print("Coding Dojo")
        elif i % 5 == 0: # if true follow my instructions if false move on
            print("Coding")
        else: # if all else fails just follow me
            print(i)

dojoWay()