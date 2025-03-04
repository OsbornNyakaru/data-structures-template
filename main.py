# main.py - Entry point for testing the implemented data structures

from data_structures import Array, LinkedList, Stack, Queue

def main():
    # Example test for Array
    arr = Array([1, 2, 3])
    print(f"Array: {arr}")
    arr.append(4)
    print(f"Array after append: {arr}")
    arr.remove(2)
    print(f"Array after remove: {arr}")
    
    # Example test for Linked List
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    print(f"Linked List: {ll}")
    
    # Example test for Stack
    stack = Stack()
    stack.push(5)
    stack.push(10)
    print(f"Stack: {stack}")
    stack.pop()
    print(f"Stack after pop: {stack}")
    
    # Example test for Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Queue: {queue}")
    queue.dequeue()
    print(f"Queue after dequeue: {queue}")

if __name__ == "__main__":
    main()
