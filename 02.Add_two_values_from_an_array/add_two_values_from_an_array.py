def are_there_two_values_equal_to_Z (list_with_numbers, num_Z):\
    
    list_for_numbers = []   
    for index in range(0, len(list_with_numbers)):
        temp = num_Z - list_with_numbers[index]
        if(temp in list_for_numbers):
            return f'Yes, the values are {temp} and {list_with_numbers[index]}!'        
        list_for_numbers.append(list_with_numbers[index])

    return 'No, there are no such values!'

if __name__ == '__main__':
    # User inputs 

    list_length         = int(input('Please enter the length ot the list ---> '))
    list_with_numbers   = []
    next_number         = 1
    for i in range(list_length):        
        x       = int(input(f'Value number {next_number} ---------------------------> '))
        next_number += 1
        list_with_numbers.append(x)
    num_Z       = int(input('Integer Z ------------------------------> '))
    # -----------------------------------------------------------------------------------

    # Create an empty dictionary

    
    the_answer  = are_there_two_values_equal_to_Z(list_with_numbers, num_Z) 


    print(list_with_numbers)


    print('*** *** *** *** *** *** *** *** *** *** *** ***') 
    print('Does the array contain two values for ')
    print('which the condition a[x] + a[y] = Z')
    print(f'is fulfilled? --------------------------> {the_answer}')
    print('*** *** *** *** *** *** *** *** *** *** *** ***')
    print('--- --- --- --- --- --- --- --- --- --- --- ---') 