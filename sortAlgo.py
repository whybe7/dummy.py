from typing import Sized


def bubble_sort(array:list):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array  
 
def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array 
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result 
def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])) 
    
def timsort(array):
    min_run = 32
    n = len(array)
    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))
    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array
        # Each iteration should double the size of your arrays
        size *= 2
    return array

def matrix(l:int):
    matrix = []
    d1 = []
    if l < 0:
        return l
    else:
        for row in range(l):
            matrix.append([])
            for col in range(l):
                matrix[row].append(int(input("> element (%d,%d): "%(row,col))))
        print(matrix)
        print(f"is magic matrix: {isMagic(matrix)}")
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                d1.append(matrix[row][col])
                
    
    if l == 3 :      
        print('┌'+'─'*3+'┬'+'─'*3+'┬'+'─'*3+'┐')
        print('│'+' '+str(d1[0])+' '+'│'+' '+str(d1[1])+' '+'│'+' '+str(d1[2])+' '+'│')
        print('├'+'─'*3+'┼'+'─'*3+'┼'+'─'*3+'┤')
        print('│'+' '+str(d1[3])+' '+'│'+' '+str(d1[4])+' '+'│'+' '+str(d1[5])+' '+'│')
        print('├'+'─'*3+'┼'+'─'*3+'┼'+'─'*3+'┤')
        print('│'+' '+str(d1[6])+' '+'│'+' '+str(d1[7])+' '+'│'+' '+str(d1[8])+' '+'│')
        print('└'+'─'*3+'┴'+'─'*3+'┴'+'─'*3+'┘')
def isMagic(squear:list):
    result = isSquear(squear)
    if result:
        total = []
        
        #diagonal /:
        sum = 0
        for same in range(len(squear)):
            sum += squear[same][same]
        total.append(sum)

        #diagonal \:
        sum = 0
        loc = len(squear)-1
        for row in range (len(squear)):
            sum += squear[row][loc]
            loc -= 1
        total.append(sum)
        
        #rows ── :
        sum = 0
        for row in range(len(squear)):
            for col in range(len(squear)):
                sum += squear[row][col]
            total.append(sum)
            sum = 0
        
        #col | :
        sum = 0
        for row in range(len(squear)):
            for col in range(len(squear)):
                sum += squear[col][row]
            total.append(sum)
            sum = 0
        
        value = total[0]
        for i in range(1,len(total)):
            if total[i] != value:
                result = False
                break
    return result
            
def isSquear( squear:list ):                      
    result = True
    size = len(squear)
    for row in squear:
        if len(row) != size:
            result = False
            break
    return result 
    
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

[[1, 4, 7], 
 [2, 5, 8],
 [3, 6, 9]]
#magic squer
[[8, 1, 6], 
 [3, 5, 7], 
 [4, 9, 2]]

matrix(3)

