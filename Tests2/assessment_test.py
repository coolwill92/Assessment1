from Tests1.Code import python1


# def test_one():
#    assert python1.helloworld()== "Hello World"

#def test_two():
#    assert python1.helloworld2() == "Hello World"

#def test_three():
#    assert python1.helloworld3() == "HelloWorld"
#    assert python1.helloworld3() == "Williamiscool"
#    assert python1.helloworld3() == " "

def test_four():
    assert python1.helloworld4(True, num1, num2) == (num1 + num2)
    assert python1.helloworld4(False, num1, num2) == (num1 * num2)



