def fibonacci(n):
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < n:
        next_num = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_num)
    
    return fibonacci_series[:n]

a = int(input("Enter till where you want to generate the Fibonacci series...\n"))

gen = fibonacci(a)
print(gen)

