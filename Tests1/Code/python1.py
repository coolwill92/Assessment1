#def helloworld():

#    return ("Hello World")

#def helloworld2():
#    x = "Hello World"
#    return x

#def helloworld3():
#    x = input("Please enter a word:")
#    return x

def helloworld4():
    num1 = int(input("Pick a number: "))
    num2 = int(input("Pick a number: "))
    bool = str("Pick a boolean: ")
    if bool == True:
        return int(num1 + num2)
    elif bool == False:
        return int(num1 * num2)

helloworld4()