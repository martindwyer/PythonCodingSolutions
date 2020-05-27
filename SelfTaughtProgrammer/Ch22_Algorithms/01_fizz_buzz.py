
"""
Write a program that prints the numbers from 1 to 100.  For multiples of 3,
print "Fizz" instead of the number, multiples of 5 print "Buzz" and for multipls
of both 3 and 5, print "FizzBuzz"
"""


def fizz_buzz():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz()
