def sum_elements(list_input):

    total_sum = 0

    def check_and_sum(total_sum, list_input):

        for item in list_input:
            if isinstance(item, int):
                total_sum += item
            elif isinstance(item, list):
                total_sum = check_and_sum(total_sum, item)
        return total_sum

    return check_and_sum(total_sum, list_input)

if __name__ == '__main__':

    list_1 = [7]
    list_2 = [5, 6, list_1]
    list_3 = [1, 2, 3, list_2 , 4]

    print(sum_elements(list_3))