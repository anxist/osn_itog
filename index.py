def filter_short_strings(input_array):
    result = []
    for item in input_array:
        if len(item) <= 3:
            result.append(item)
    return result

input_array1 = ["Hello", "2", "world", ":-)"]
input_array2 = ["1234", "1567", "-2", "computer science"]
input_array3 = ["Russia", "Denmark", "Kazan"]

print(filter_short_strings(input_array1))  #  ['2', ':-)']
print(filter_short_strings(input_array2))  #  ['-2']
print(filter_short_strings(input_array3))  #  []