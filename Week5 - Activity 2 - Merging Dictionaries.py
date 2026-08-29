# This program builds dictionaries from separate key and value lists,
# then keeps only the key-value pairs where the value is an odd number.

# First set of keys and values
Key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]

# Second set of keys and values
Key2 = ['u', 'b', 'o', 'x', 'e', 'a']
Value2 = [200, 30, 10, 88, 55, 920]

# Pair each key with its value using zip, then keep only the pairs
# where the value is odd (value % 2 != 0)
odd_dict1 = {k: v for k, v in zip(Key1, Value1) if v % 2 != 0}
odd_dict2 = {k: v for k, v in zip(Key2, Value2) if v % 2 != 0}

# Display the results
print("=== Odd Value Pairs from Key1/Value1 ===")
print(odd_dict1)

print("\n=== Odd Value Pairs from Key2/Value2 ===")
print(odd_dict2)
