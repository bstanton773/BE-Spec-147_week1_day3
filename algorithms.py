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

line_break()


# Merge Sort - 
# Worst Case - O(n log n) Time Complexity
# Best Case - O(n log n) Time Complexity
# Space Complexity - O(n)
print('Merge Sort:')

another_list = [randint(1, 50) for _ in range(10)]


def merge_sort(lst):
    # Check if the list can be split into two
    if len(lst) > 1:
        # Find the midway point
        mid = len(lst) // 2
        # Split the list into a left half and right half
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Call merge_sort on the left half
        merge_sort(left_half)
        # Call merge_sort on the right half
        merge_sort(right_half)

        # Merge the left and right half lists back into the original list
        # index pointers for the three lists
        l = 0 # pointer for the left half
        r = 0 # pointer for the right half
        m = 0 # pointer for the main list

        # While the left and right pointer are still pointing at valid indices
        while l < len(left_half) and r < len(right_half):
            # Compare the value at left pointer vs right pointer
            if left_half[l] < right_half[r]:
                # Copy the left value into the main list
                lst[m] = left_half[l]
                # Move the left pointer to the right
                l += 1
            else:
                # Copy the right value into the main list
                lst[m] = right_half[r]
                # Move the right pointer to the right
                r += 1
            # Either way, always move the main pointer to the right
            m += 1

        # When one half finishes (either left or right), copy the res of the other half into the main list
        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1

    return lst


print(another_list)
merge_sort(another_list)
print(another_list)


line_break()
line_break()
#####################
# Search Algorithms #
#####################

# * List must be sorted #

# Linear Search
print('Linear Search')

def linear_search(lst, target):
    num_checks = 0
    # Starting at index 0 until the end of the list
    for i in range(len(lst)):
        num_checks += 1
        # If the list at index i is equal to target
        if lst[i] == target:
            # Return the index
            return f"{target} can be found at index {i} and it took {num_checks} checks to find"
        # If the list at index i in greater than the target
        elif lst[i] > target:
            return f"Target is not found and it took {num_checks} checks"
    # If we loop through the entire list, we know target is not there
    return f"Target is not found and it took {num_checks} checks"


nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

print(linear_search(nums, 60))
print(linear_search(nums, 10))
print(linear_search(nums, 64))
print(linear_search(nums, 95))



line_break()

print('Binary Search:')
def binary_search(lst, target):
    # Set the high and low point on the list
    low = 0
    high = len(lst) - 1
    num_checks = 0
    while low <= high:
        # Get the middle of low and high
        mid = (low + high) // 2
        num_checks += 1
        # Check if the middle is the target
        if lst[mid] == target:
            return f"{target} can be found at index {mid} and it took {num_checks} checks to find"
        # If the middle is greater than the target
        elif lst[mid] > target:
            # Set the high to be one less than mid
            high = mid - 1
        # if the middle is less than target
        else:
            # Set the low to be one more than mid
            low = mid + 1
    # If low ever passes high, we know target is not there
    return f"Target is not found and it took {num_checks} checks"


nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

print(binary_search(nums, 60))
print(binary_search(nums, 10))
print(binary_search(nums, 64))
print(binary_search(nums, 95))


line_break()

big_nums = [x for x in range(1000000)]

print(linear_search(big_nums, 118359))
print(binary_search(big_nums, 118359))

