from random import choices

# moda
def moda(*nums):
    nums = list(nums)
    maximo = max(nums.count(x) for x in nums)
    n = [x for x in set(nums) if nums.count(x) == maximo]
    return n

modas = choices([2, 4, 6, 10, 9], k= 8)
print(f'Sua lista de numeros: {modas} e, sua moda(s): {moda(*modas)}')


# media
def avg(*nums):
    return sum(nums) / len(nums)

nums_avg = choices([2, 6, 7, 10], k= 9)

print(f'Sua lista de numeros: {nums_avg} e, sua média: {avg(*nums_avg):.2f}')


# mediana
def mediana(*nums):
    nums_ordenado = sorted(nums)
    n = len(nums_ordenado)
    if n % 2 == 0:
        meio1 = n // 2 - 1
        meio2 = n // 2 
        mediana_lista = (nums_ordenado[meio1] + nums_ordenado[meio2]) / 2
        return mediana_lista
    else:
        meio = n // 2
        mediana_lista = nums_ordenado[meio]

    return mediana_lista


mediana_nums = choices([2, 6, 8, 9, 10], k= 10)

mediana_nums.sort()

print(f'Sua lista de numeros: {mediana_nums} e, sua mediana: {mediana(*mediana_nums)}')

