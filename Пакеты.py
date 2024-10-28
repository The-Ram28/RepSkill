# Пакеты
# программу, которая будет обрабатывать полученные пакеты и выведет на экран итоговое сообщение
# для декодирования, а также количество ошибок в нём и количество необработанных пакетов.


ack = []
decode = []
error_count = 0

num = int(input('Количество пакетов: '))
for i_packs in range(num):
    print('\nПакет номер', i_packs + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end=' ')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) > 1:
        print('Много ошибок в пакете.')
        error_count += 1
    else:
        decode.extend(pack)
    pack = []

print('\nПолученное сообщение:', decode)
print('Количество ошибок в сообщении:', decode.count(-1))
print('Количество потерянных пакетов:', error_count)