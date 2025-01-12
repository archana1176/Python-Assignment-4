
 # Exercise 1:


def new_function(a,b=10,c=None):
    if c is None:
        print(a+b)
    else:
        print(a*b*c)


new_function(5,c=4)
new_function(5, 20)
new_function(5, 20, 2)

# Exercise 2

input_list=["apple", "cat", "banana", "dog", "elephant"]
print("input list: ",input_list)

def filter_strings(input_list):
    output_list = []
    for string in input_list:
          if len(string)>=5:
            output_list.append(string)
    return output_list

output=filter_strings(input_list)
print("filtered output :",output)

#Exercise 3:
# Write a Python program to evaluate a given mathematical expression using the eval() function. expression = "3 * 5 + 2"

print("Result of 3*5+2 :",eval("3*5+2"))


#Exercise 4:

# Write a Python program to filter out the prime numbers from a given list of integers using the filter() function.


numbers=[int(input("enter the list of numbers")) for _ in  range(6)]
print(numbers)

def filter_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = list(filter(filter_prime, numbers))
print("The prime numbers in the list are:", prime_numbers)

#Exercise 5:

#Write a Python program to convert a list of strings to uppercase using the map() function.


list_string=[input("enter list string element:") for _ in range(5)]
uppercase_strings = list(map(str.upper, list_string))
print(list(uppercase_strings))