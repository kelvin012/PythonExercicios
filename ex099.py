from time import sleep


def maior(*nums):
    index = maior_elemento = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for num in nums:
        sleep(0.4)
        print(f'{num} ', end='')
        if index == 0:
            maior_elemento = num
            index += 1
        else:
            if num > maior_elemento:
                maior_elemento = num
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maior_elemento}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(6)
maior()
maior(-9, -5, -12, -2)
