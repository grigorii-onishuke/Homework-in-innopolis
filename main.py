numbers1 = 1
numbers2 = 1

N = int(input("ведите номер числа"))
i = 0
while i < N-2:
    numbers3 = numbers1 + numbers2
    numbers1 = numbers2
    numbers2 = numbers3
    i=i + 1
print('значение этого числа:', numbers2)
