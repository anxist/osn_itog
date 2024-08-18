def filter_short_strings(input_array):
    result = []
    
    for item in input_array:
        if len(item) <= 3:
            result.append(item)
    
    return result

def main():
    print("Введите строки, разделенные пробелами. Введите 'стоп' для завершения ввода.")
    input_array = []
    
    while True:
        line = input()
        if line.lower() == 'стоп':
            break
        input_array.append(line)
    
    filtered_array = filter_short_strings(input_array)
    
    print("Отфильтрованный массив:")
    print(filtered_array)

if __name__ == "__main__":
    main()