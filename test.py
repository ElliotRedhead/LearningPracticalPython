#print("Hello world!")

def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "Empty string."
assert count_upper_case("A") == 1, "One upper case."
assert count_upper_case("a") == 0, "One lower case."
assert count_upper_case("£$%^") == 0, "Special characters."
# print(count_upper_case("Hello world!"))

def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
    if evens == 0:
        return False
    else:
        return evens % 2 == 0

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")