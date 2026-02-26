def sum_of_odd_squares(total_squares):
    # quantidade de quadrados ímpares
    n = total_squares // 2
    
    # fórmula matemática
    return n * (2*n - 1) * (2*n + 1) // 3


result = sum_of_odd_squares(972000)
print(result)