def factorial(n):

   if n == 1:
       return n
   else:
       return n * factorial(n - 1)

if __name__ == '__main__':

    n = int(input('Please enter your number: '))

    if n < 0:
        print('Sorry, factorial does not exist for negative numbers')
    elif n == 0:
        print('The factorial of 0 is 1')
    else:
        result = factorial(n)
        print(f'The factorial of {n} is {result}')