def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Starting values for the Fibonacci sequence
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def sum_fibonacci_sequence(n):
    fib_sequence = fibonacci_sequence(n)
    return sum(fib_sequence)

# Sum the first 50 Fibonacci numbers
n = 50
sum_of_fibonacci = sum_fibonacci_sequence(n)
print(f"Sum of the first {n} Fibonacci numbers: {sum_of_fibonacci}")

