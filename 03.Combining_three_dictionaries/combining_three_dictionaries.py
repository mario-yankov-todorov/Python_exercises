# Merged three dictionaries
if __name__ == '__main__':

    Bulgarian_mountain_peaks_01 = {
        'Рила'              :   'Мусала',
        'Пирин'             :   'Вихрен',
        'Стара планина'     :   'Ботев',
        'Витоша'            :   'Черни връх',
        'Осоговска планина' :   'Руен'
    }

    Bulgarian_mountain_peaks_02 = {
        'Славянка'          :   'Гоцев връх',
        'Родопи'            :   'Голям Перелик',
        'Беласица'          :   'Радомир',
        'Влахина планина'   :   'Кадийца',
        'Малешевска планина':   'Ильов връх'
    }

    Bulgarian_mountain_peaks_03 = {
        'Кървав камък'      :   'Било',
        'Милевска'          :   'Милевец',
        'Руй'               :   'Руй',
        'Огражден'          :   'Билска чука',
        'Средна гора'       :   'Богдан'
    }

    The_three_dictionaries_together = {
        **Bulgarian_mountain_peaks_01,
        **Bulgarian_mountain_peaks_02,
        **Bulgarian_mountain_peaks_03
    }

    print('*** *** *** *** *** *** *** *** *** *** *** ***')     
    for item in The_three_dictionaries_together.items():            
        key, value = item
        # To align the output data
        n = 20 - len(key)
        number_of_characters = '-' * n
        # Print output data
        print(f'{key} {number_of_characters}> {value}')
    print('*** *** *** *** *** *** *** *** *** *** *** ***') 