                                                #1)  Data Structures

#   -Create a list of integers and add 5 elements to it.
my_list = [1, 2, 3, 4, 5]
print(my_list)

#   -Create a dictionary with string keys and integer values, and add 5 key-value pairs to it.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print(my_dict)

#   -Create a queue of integers and add 5 elements to it.
from collections import deque
queue = deque([1, 2, 3, 4, 5])
print(queue)

#   -Create a stack of integers and add 5 elements to it.
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)
#-----------------------------------------------------------------------------------------------------------------------

                                        #2)Operations on Data Structures

#   -Calculate and print the sum of all elements in the list.
my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)

print(total_sum)


#   -Calculate and print the sum of all values in the dictionary.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
total_sum = sum(my_dict.values())

print(total_sum)


#   -Remove 2 elements from the queue and print the remaining elements.
from collections import deque

queue = deque([1, 2, 3, 4, 5])
queue.popleft()
queue.pop()

print(queue)

#   -Remove 2 elements from the stack and print the remaining elements.

stack = [1, 2, 3, 4, 5]
stack.pop()
stack.pop()

print(stack)

# #-----------------------------------------------------------------------------------------------------------------------
#                                             #3)Additional Tasks

#   -Print all elements of the list.
my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

#   -From a three-digit number (e.g., 124), print the largest digit.

number = 950

number_str = str(number)
largest_digit = max(int(digit) for digit in number_str)

print(largest_digit)

#   -From a three-digit number (e.g., 124), print the smallest digit.

number = 185

number_str = str(number)
largest_digit = min(int(digit) for digit in number_str)

print(largest_digit)

#   -From an array, find all even values and print their sum.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_values = [num for num in array if num % 2 == 0]
sum_of_even_values = sum(even_values)

print(sum_of_even_values)


#   -Calculate and print the average of all elements in the array.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_sum = sum(array)
num_elements = len(array)
average = total_sum / num_elements

print(average)

#-----------------------------------------------------------------------------------------------------------------------
                                                      #Homework 2
                                      #Implement Insertion Sort recursively.


def insertion_sort_recursive(arr, n):
    if n <= 1:
        return

    insertion_sort_recursive(arr, n-1)
    last = arr[n-1]
    j = n-2

    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last

arr = [12, 11, 13, 5, 6]
insertion_sort_recursive(arr, len(arr))
print("Sorted array is:", arr)



#-----------------------------------------------------------------------------------------------------------------------
                                        #Implement a Custom Queue using a list.

class CustomQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

queue = CustomQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeued item is:", queue.dequeue())
print("Peek item is:", queue.peek())
print("Queue size is:", queue.size())
