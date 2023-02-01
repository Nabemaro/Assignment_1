def is_multifi_table(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f'{i * j:4d}', end='')
        print('\n', end='')


is_multifi_table(12)
