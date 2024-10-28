def has_sequence(lst, seq=[0, 1]):
    for i in range(len(lst) - len(seq) + 1):
        if lst[i:i + len(seq)] == seq:
            return True
    return False

# Example usage
lst = [3, 0, 1, 2, 4, 0, 1]
print(has_sequence(lst))  # Output: True