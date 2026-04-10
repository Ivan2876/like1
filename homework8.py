numbers = [3, 7, 2, 9, 4, 6, 1, 8]
even_numbers = []
for number in numbers:
 if number % 2 == 0:
     even_numbers.append(number)
print(even_numbers, '-всі парні')

doubled_even =[]
for number in even_numbers:
    doubled_even.append(number * 2)


print(even_numbers,'-числа помножені на 2')

who_have_eight = 8 in even_numbers
if 8 in even_numbers:
    even_numbers.remove(8)
print(even_numbers,'-фінальна версія')

words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]
unique_words = set(words)
print(unique_words,'-унікальні слова')

long_words = []
for word in words:
    if len(word) > 4:
        long_words = long_words + [word]
print(long_words,'-слова які мають більш ніж 4 символи')

upeer_words = []
for word in long_words:
    upeer_words.append(word.upper())
print(upeer_words,'всі в верхньому реістрі')
is_banana_in_upper_words = "BANANA" in upeer_words
print(is_banana_in_upper_words,'-так є')
print(upeer_words,'-фінальна версія')
