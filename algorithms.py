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


from random import randint

unsorted_list = [randint(1,50) for _ in range(10)]



# Bubble Sort - 
# Worst Case - O(n**2) Time Complexity
# Best Case - O(n) Time Complexity
# Space Complexity - O(1) Constant

print('Bubble Sort:')

def bubble_sort(lst):
    # When we first start, set up a vairable (swapped) to True to begin the while loop
    swapped = True
    # Set a variable for number of indices we can skip at end of list (after x loops, we know the last x elements are sorted)
    x = 1
    while swapped:
        # Begin the loop with the assumption (hope?) that we don't have to make any more swaps (aka the list is already sorted)
        swapped = False
        # Start at the 0-index and loop to the second to last item (because we check each item and the item to its right)
        for idx in range(len(lst) - x):
            # Check if the value at idx is greater than the value to its right (idx+1)
            if lst[idx] > lst[idx+1]:
                # Swap those value
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                # Because we made a swap, set the swapped boolean to True 
                swapped = True
        # After each full loop through the list, increase the num we can skip at end by 1
        x += 1
    # Once the while loop is done (meaning we looped through and made no swaps), our list is sorted, return the list
    return lst

print(unsorted_list)
bubble_sort(unsorted_list)
print(unsorted_list)


random_list = [randint(1,50) for _ in range(10)]


# Insertion Sort - 
# Worst Case - O(n**2) Time Complexity
# Best Case - O(n) Time Complexity
# Space Complexity - O(1) Constant

print('Insertion Sort:')

def insertion_sort(lst):
    # Loop over the unsorted section (start at the 1-index because the 0-index is "sorted")
    for i in range(1, len(lst)):
        pointer = i
        # While we are not at the front of the list AND the element to the left is greater than the pointer element
        while pointer > 0 and lst[pointer-1] > lst[pointer]:
            # Swap the element with the element to its left
            lst[pointer], lst[pointer-1] = lst[pointer-1], lst[pointer]
            # Move the pointer to the left one index (to match the new swap)
            pointer -= 1
    # Once we've looped over the unordered section, the list should be ordered
    return lst

print(random_list)
insertion_sort(random_list)
print(random_list)



cities = ['Chicago', 'New York', 'Los Angeles', 'Phoenix', 'Denver', 'Houston', 'Boston']

bubble_sort(cities)
print(cities)


