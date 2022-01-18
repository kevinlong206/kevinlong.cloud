def is_multiple_of_five(n):
    return not n % 5

def get_multiples_of_5(n):
    return list(filter(is_multiple_of_five, range(n)))

print(get_multiples_of_5(50))
