def fizzBuzz(intValue):

    returnValue = ""

    if intValue % 3 == 0:
        if intValue %5 == 0:
            returnValue = "Fizz Buzz"
        else:
            returnValue = "Fizz"
    elif intValue % 5 == 0:
        returnValue = "Buzz"
    else:
        returnValue = f"{intValue}"

    return returnValue