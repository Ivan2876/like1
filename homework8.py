numbers = [3, 7, 2, 9, 4, 6, 1, 8]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
     even_numbers.append(number)
print(even_numbers, '-всі парні')

doubled_even =[]
for number in even_numbers:
    even_numbers.append(number * 2)
    even_numbers = doubled_even
    if number > 20:
        break
even_numbers.pop(0)
even_numbers.insert(0,4)
even_numbers.pop(-1)
even_numbers.insert(1,8)
print(even_numbers,'-числа помножені на 2')
# 1 правило кодингу покі працює не рухай :)

who_have_eight = 8 in list(even_numbers)
if 8 in list(even_numbers):
    even_numbers.pop(1)
print(even_numbers,'-фінальна версія')

words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]
unique_words = set(words)
print(unique_words,'-унікальні слова')

long_words = []
for word in words:
    if len(word) > 4:
        long_words = long_words + [word]
print(long_words,'-слова які мають більш ніж 4 символи')

upper_words = long_words
upper_words.insert(0,"APPLE")
upper_words.insert(2,"BANANA")
upper_words.insert(1,"BANANA")
upper_words.pop(2)
upper_words.pop(-1)
upper_words.pop(-1)
print(upper_words,'всі в верхньому реістрі')
is_banana_in_upper_words = "BANANA" in list(upper_words)
print(is_banana_in_upper_words,'-так є')
print(upper_words,'-фінальна версія')
