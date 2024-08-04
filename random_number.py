import random

# Generate random 4-digit binary number
binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))
base10_number = int(binary_number, 2)
print("Binary:", binary_number, "Base 10:", base10_number)
