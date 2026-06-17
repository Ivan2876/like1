def get_result (number1: int , number2: int, operation: str="sum") -> int | float:
    sume = number1 + number2
    difference = number1 - number2
    if operation == "sum":
        return sume
    else:
        return difference

def get_accepts_string(line: str ,upper: bool = True) -> str:
    if upper:
        line = line.upper()
        return line
    else:
        line = line.lower()
        return line

def get_sume_of_numbers_in_list_string (list_of_numbers_as_string: str , separator: str = "," ) -> int:
    break_line = list_of_numbers_as_string.split(separator)
    sume = 0
    for number in break_line:
        sume += int(number)
    return sume
