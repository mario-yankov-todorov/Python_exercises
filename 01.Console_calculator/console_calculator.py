# Functions
def addition(num_1, num_2):
    return num_1 + num_2

def subtrction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

def floor_division(num_1, num_2):
    return num_1 // num_2

def quit_app(*args):
    msg = '''*** *** *** *** *** *** *** *** *** *** *** ***
Quit Editor 
*** *** *** *** *** *** *** *** *** *** *** ***'''
    ('') 
    print(msg)
    quit()
# -----------------------------------------------------------------------------------

if __name__ == '__main__':

    actions = {
        '+' : addition,
        '-' : subtrction,
        '*' : multiplication,
        '/' : division,
        '//': floor_division,
        'q' : quit_app
    }

    operand = ''
    stars = ' *** ' * 7
    while True:
        # User inputs
        operand =       input('Operand(+,-,*,/,//) or quit(q) --> ')
        if 'q' in operand: quit_app()
        
        num_1   = float(input('Please enter the first number ---> '))
        num_2   = float(input('Second number -------------------> '))
        # -----------------------------------------------------------------------------------

        if operand in actions:
            result = actions[operand](num_1, num_2)
            print(stars, f' Result is equal to ----> {result}', stars, sep = '\n')
        else:
            print(f'Unknown Command: {operand}')