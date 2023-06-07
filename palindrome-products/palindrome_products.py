def palindrome(number):
    return str(number) == str(number)[::-1]
def validate(max_factor, min_factor):
    if not min_factor <= max_factor:
        raise ValueError("min must be <= max")
def filter_palindromes(palindromes, number):
    return [x for x in palindromes if x[0] * x[1] == number]
def safe_break(found_palindrome, i, j, large):
    return found_palindrome and (
        (large and i * j < found_palindrome) or (not large and i * j > found_palindrome)
    )
def new_palindrome(found_palindrome, i, j, large):
    return palindrome(i * j) and (
        not found_palindrome
        or (large and i * j > found_palindrome)
        or (not large and i * j < found_palindrome)
    )
def make_range(i, j, large):
    if large:
        return reversed(range(i, j + 1))
    return range(i, j + 1)
def find_palindromes(max_factor, min_factor, large):
    found_palindrome = None
    palindromes = []
    for i in make_range(min_factor, max_factor, large):
        for j in make_range(i, max_factor, large):
            if safe_break(found_palindrome, i, j, large):
                break
            if palindrome(i * j):
                palindromes.append((i, j))
            if new_palindrome(found_palindrome, i, j, large):
                found_palindrome = i * j
    if found_palindrome:
        return found_palindrome, filter_palindromes(palindromes, found_palindrome)
    return found_palindrome, palindromes
def smallest(max_factor, min_factor=0):
    validate(max_factor, min_factor)
    return find_palindromes(max_factor, min_factor, False)
def largest(max_factor, min_factor=0):
    validate(max_factor, min_factor)
    return find_palindromes(max_factor, min_factor, True)
