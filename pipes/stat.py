import time

def stat(input_func, output_func):
    values = []
    while True:
        value = input_func()
        if value is not None:
            values.append(value)
            mean = sum(values) / len(values)
            total = sum(values)
            output_func(mean, total)
    
