def fizz_buzz(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
  
print(fizz_buzz(6))
print(fizz_buzz(10))
print(fizz_buzz(30))
print(fizz_buzz(4))
