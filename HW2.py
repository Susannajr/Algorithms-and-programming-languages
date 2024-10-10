#Homework 2
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
