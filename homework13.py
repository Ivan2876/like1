from homework13utils import get_result, get_accepts_string, get_sume_of_numbers_in_list_string
function1_first = get_result(8,3,'sum')
print(function1_first)
function1_second = get_result(number1=32,number2=11,operation='sub')
print(function1_second)
dictionary_of_function1 = {"number1": 10,
                           "number2": 12,}
function1_third = get_result(**dictionary_of_function1)
print(function1_third)

function2_first = get_accepts_string('hello')
print(function2_first)
function2_second = get_accepts_string(line='hello')
print(function2_second)
dictionary_of_function2 = {'line':'hello'}
function2_third = get_accepts_string(**dictionary_of_function2)
print(function2_third)

function3_first = get_sume_of_numbers_in_list_string("11,23,36")
print(function3_first)
function3_second = get_sume_of_numbers_in_list_string(list_of_numbers_as_string="11,23,36")
print(function3_second)
dictionary_of_function3 = {'list_of_numbers_as_string':'11,23,36'}
function1_third = get_sume_of_numbers_in_list_string(**dictionary_of_function3)
print(function1_third)
