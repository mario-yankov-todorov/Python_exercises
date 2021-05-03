
def check_user_input(g):
    try:
        # Convert it into integer
        g = int(g)
        if 2 <= g < 256:
            return g
        else:
            print('Input is out of range. The number must be between 2 and 255')
    except ValueError:
        print('Input is not a number. It is a string')


def bin_values(g):
    if isinstance(g, int):
        for i in range(g + 1):

            k = bin(i)
            print(f' {i} --> {k}')


if __name__ == '__main__':

    g = input('Please, enter your decimal number: ')

    g = check_user_input(g)

    bin_values(g)

    print('--- ---')