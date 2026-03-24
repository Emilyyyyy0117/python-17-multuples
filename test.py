def find_multiples_of_17(start, end):
    # Ensure start is less than end
    if start > end:
        start, end = end, start
    
    multiples = [num for num in range(start, end + 1) if num % 17 == 0]
    total_sum = sum(multiples)
    
    print(f"Multiples of 17 between {start} and {end}: {multiples}")
    print(f"Sum of multiples: {total_sum}")

try:
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    find_multiples_of_17(a, b)
except ValueError:
    print("Invalid input! Please enter integers only.")
