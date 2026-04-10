#task1
numbers = [1, 5, 2, 8, 3, 7]
numbers.sort(reverse=True)
largest_number = numbers[0]
print(largest_number, '-найбільше число')
smallest_number = numbers[-1]
print(smallest_number, '-найменше число ')
sume_number = 0
for number in numbers:
    sume_number = sume_number + number

print(sume_number,'сума всіх чисел')
#task2
snows = [10, 8, 12, 7, 9]
sume_number2 = 0
for snow in snows:
    sume_number2 = sume_number2 + snow

average = sume_number2 / len(snows)
print(average,'-середній бал')

numbers_bigger_normal = []
for snow in snows:
    if snow > average:
        numbers_bigger_normal.append(snow)
print(numbers_bigger_normal,'-оцінки вище середього')
