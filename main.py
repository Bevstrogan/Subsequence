def get_sequence(n):
    number = 1
    result = []
    while number < n:
        result.extend(str(number) * number)
        number += 1
    return ''.join(result[:n])

n = int(input('Введите n:'))
print(get_sequence(n))

