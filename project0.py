def drawing(number):
    i = 0
    while True:
        if i == 0:
            print('+-+')
            print('| |')
            print('+-+', end='')
            i += 1
        elif i <= number - 1:
            print('-+')
            print(' ' * (i * 2 - 1), '| |')
            if i == number - 1:
                print(' ' * (i * 2 - 1), '+-+', end='\n')
                break
            else:
                print(' ' * (i * 2 - 1), '+-+', end='')
                i += 1


user_input = int(input())
drawing(user_input)
