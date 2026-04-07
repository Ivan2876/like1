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
    sume_numbers = sume_number + 0
print(sume_numbers,'сума всіх чисел')
#task2
snows = [10, 8, 12, 7, 9]
sume_number2 = 0
for snow in snows:
    sume_number2 = sume_number2 + snow
sume_number3 = sume_number2 / 5
print(sume_number3,'-середній бал')
snows.sort()
numbers_bigger_normal = snows[3:5]
print(numbers_bigger_normal,'-оцінки вище середього')
