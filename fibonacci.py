def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci_numbers = [fibonacci(i) for i in range(50)]
sum_fibonacci = sum(fibonacci_numbers)
print("Sum of first 50 Fibonacci numbers:", sum_fibonacci)
