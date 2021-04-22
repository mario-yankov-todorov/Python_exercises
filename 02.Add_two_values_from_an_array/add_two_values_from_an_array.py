def check_values(list_num, num_z):
    
    new_list = [] 
    n = len(list_num)

    for index in range(n):
        temp = num_z - list_num[index]
        if temp in new_list:
            return f'Yes!'        
        new_list.append(list_num[index])

    return 'No!'

if __name__ == '__main__':
    # User inputs 

    list_length = int(input('Please enter the length ot the list ---> '))
    list_num  = []
    next_number = 1
    for i in range(list_length):        
        x = int(input(f'Value number {next_number} ---------------------------> '))
        next_number += 1
        list_num.append(x)
    num_z = int(input('Integer Z ------------------------------> '))
    # -----------------------------------------------------------------------------------

    the_answer  = check_values(list_num, num_z)

    stars = ' *** ' * 7
    msg_1 = ''' Does the array contain two values for
 which the condition a[x] + a[y] = Z'''
    msg_2 = f' is fulfilled? --------------------------> {the_answer}'


    print(stars, msg_1, msg_2, stars, sep = '\n') 