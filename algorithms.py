import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


##############
# Algorithms #
##############

# An algorithm is a set of instructions for solving a problem
# Used to solve all types of problems e.g. sorting data or searching for information
# Being able to write efficient algorithms is key to becoming a great programmer


# Looking at Time Complexity

def linear_loop(a_list):
    for item in a_list:
        print(item)

def quadratic_loop(a_list):
    for item_a in a_list:
        for item_b in a_list:
            print(item_a, item_b)


nums = [1, 2, 3, 4]

linear_loop(nums)
line_break()
quadratic_loop(nums)

line_break()


# Space Complexity

# Swapping Function - A function that will take in a list, and 2 indices to swap

def swap_out_of_place(list_a, index_a, index_b): # O(n) - Linear Space Complexity
    # Create a new list that is a copy of list_a
    list_b = list_a[:]
    # Assign the index values
    list_b[index_a] = list_a[index_b]
    list_b[index_b] = list_a[index_a]
    # Return the new list with swapped values
    return list_b


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

swapped = swap_out_of_place(colors, 2, 5)
print(colors)
print(swapped)


def swap_in_place(list_a, index_a, index_b): # O(1) - Constant Space Complexity
    temp = list_a[index_a]
    list_a[index_a] = list_a[index_b]
    list_a[index_b] = temp
    return list_a

subjects = ['math', 'science', 'history', 'english', 'computer', 'python']

swapped2 = swap_in_place(subjects, 1, 3)
print(subjects)
print(swapped2)


# Multiple Item Assignment
x, y, z = 10, 20, 30

print(f"{x=}")
print(f"{y=}")
print(f"{z=}")


def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    # return lst


sports = ['basketball', 'baseball', 'hockey', 'soccer', 'football', 'lacrosse', 'rugby']

print('Before swap:', sports)
swap(sports, 2, 5)
print('After swap:', sports)


line_break()


# builtin sorted() vs. list.sort()

print('Sorted Function:') # O(n) - Out Of Place - Linear Space Complexity
continents = ['North America', 'Australia', 'South America', 'Europe', 'Asia', 'Africa', 'Antarctica']

print('Before:', continents)
sorted_return = sorted(continents)
print('After:', continents)
print('Return Value:', sorted_return)

print()

print('list.sort:') # O(1) - In Place - Constant Space Complexity
continents = ['North America', 'Australia', 'South America', 'Europe', 'Asia', 'Africa', 'Antarctica']

print('Before:', continents)
sort_return = continents.sort()
print('After:', continents)
print('Return Value:', sort_return)


line_break()


