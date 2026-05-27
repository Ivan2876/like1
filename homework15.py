

with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        split_line = line.split(';')
        # print(split_line)
        if split_line[5] == 'UA':
            print(split_line[2])


