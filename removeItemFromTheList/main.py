# To remove an element from a list using the remove() method, specify
# the value of that element and pass it as an argument to the method.
#
# remove() will search the list to find it and remove it.

# original list
programming_languages = ["JavaScript", "Python", "Java", "C++"]

#print original list
print(programming_languages)

# remove the value 'JavaScript' from the list
programming_languages.remove("JavaScript")
programming_languages.pop(0)

#print updated list
print(programming_languages)

#output

#['JavaScript', 'Python', 'Java', 'C++']
#['Python', 'Java', 'C++']

# Remove all items: clear()
# Remove an item by index and get its value: pop()
# Remove an item by value: remove()
# Remove items by index or slice: del

programming_languages = ["JavaScript", "Python", "Java", "C++"]
print(programming_languages.pop(0))

# If the argument is omitted, the last item is deleted.
programming_languages = ["JavaScript", "Python", "Java", "C++"]
print(programming_languages.pop())

programming_languages = ["JavaScript", "Python", "Java", "C++"]
del programming_languages[0]
print(programming_languages)  # ['Python', 'Java', 'C++']

programming_languages = ["JavaScript", "Python", "Java", "C++"]
programming_languages.clear()
print(programming_languages)  # []
