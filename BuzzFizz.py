def checkio(number):
    if number%5 == 0 and number%3 == 0:
        return "Fizz Buzz"
    elif number%5 != 0 and number%3 == 0:
        return "Fizz"
    elif number%5 == 0 and number%3 != 0:
        return "Buzz"
    else:
        return str(number)
print(checkio(15))
print()

