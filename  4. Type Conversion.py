# Given a list of integers, write a Python program to convert each element of the list to a string.

lst = input("Enter integers separated by spaces: ")


int_list = list(map(int, lst.split()))

str_list = list(map(str, int_list))

print("List of strings:", str_list)
