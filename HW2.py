# Homework 2
def recursive_insertion_sort(sequence, length):
    if length <= 1:
        return

    recursive_insertion_sort(sequence, length - 1)
    last_element = sequence[length - 1]
    index = length - 2

    while index >= 0 and sequence[index] > last_element:
        sequence[index + 1] = sequence[index]
        index -= 1

    sequence[index + 1] = last_element

numbers = [12, 11, 13, 5, 6]
recursive_insertion_sort(numbers, len(numbers))
print("Sorted list is:", numbers)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, element):
        self.items.append(element)

    def remove(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]

    def length(self):
        return len(self.items)

custom_queue = Queue()
custom_queue.add(1)
custom_queue.add(2)
custom_queue.add(3)
print("Removed item is:", custom_queue.remove())
print("Front item is:", custom_queue.front())
print("Queue length is:", custom_queue.length())
