# Functions
def addition():
    return num_1 + num_2

def subtrction():
    return num_1 - num_2

def multiplication():
    return num_1 * num_2

def division():
    return num_1 / num_2

def floor_division():
    return num_1 // num_2

def quit_app():
    print('*** *** *** *** *** *** *** *** *** *** *** ***') 
    print('Quit Editor!')
    print('*** *** *** *** *** *** *** *** *** *** *** ***') 
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

    # User inputs
    num_1   = float(input('Please enter the first number ---> '))
    num_2   = float(input('Second number -------------------> '))
    operand =       input('Operand(+,-,*,/,//) or quit(q) --> ')
    # -----------------------------------------------------------------------------------

    if operand in actions:
        result = actions[operand]()
    else:
        result = (f'Unknown Command: {operand}')


    print('*** *** *** *** *** *** *** *** *** *** *** ***') 
    print(f'Result is equal to --------------> {result}')
    print('*** *** *** *** *** *** *** *** *** *** *** ***')
    print('--- --- --- --- --- --- --- --- --- --- --- ---') 