def check_input(i_list):

    index = 0
    check_var = 0
    char = i_list[index]

    def check_char(index, check_var, char):
            while True:
                if ('(' in char) and (index < len(i_list) - 1):
                   index += 1
                   check_var += 1
                   char = i_list[index]
                   boolean = check_char(index, check_var, char)
                   return boolean

                elif (')' in char) and (check_var > 0):
                    if (len(i_list) -1 == index) and (check_var == 1):                   
                           return True
                    elif (index < len(i_list) - 1):
                       index += 1
                       check_var -= 1 
                       char = i_list[index]
                       boolean = check_char(index, check_var, char)
                       return boolean 
                    else:
                        return False
                else: 
                    return False

    if (len(i_list) > 1):
        boolean = check_char(index, check_var, char)
    else:
        boolean = False

    return boolean


if __name__ == '__main__':

    i_list = list(input('---> '))
    is_input_correct = check_input(i_list)

    if(is_input_correct):
        print ('Yes, the parentheses are properly closed!')
    else:
        print ('No, the parentheses are not closed properly!')