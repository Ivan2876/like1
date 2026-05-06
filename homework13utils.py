def get_sume (numbner1: int , numbner2: int) -> int | float:
    sume = numbner1 + numbner2
    difference = numbner1 - numbner2 / 2
    operation = "sum"
    if operation == "sub":
        return difference
    else:
        return sume

def get_accepts_string(line: str ,upper: bool = True) -> str:
    if upper:
        line = line.upper()
        return line
    else:
        line = line.lower()
        return line

def get_list_numbers_as_string (list_of_numbers_as_string: str , separator: str = "," ) -> int | float | str:
    list_of_numbers_as_string = "11,26,32"
    break_line = list_of_numbers_as_string.split(separator)
    sume = 0
    for number in break_line:
        sume += int(number)
    return sume
