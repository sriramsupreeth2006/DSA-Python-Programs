class QueueUsingTwoStacks:
    def init(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)
        print(f"{data} enqueued")

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return "Queue is empty"

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def display(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty")
            return
        print("Queue:", end=" ")
        for item in reversed(self.stack2):
            print(item, end=" ")
        for item in self.stack1:
            print(item, end=" ")
        print()

def menu():
    queue = QueueUsingTwoStacks()

    while True:
        print("\nQueue Operations using Two Stacks:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter element to enqueue: "))
            queue.enqueue(data)
        elif choice == 2:
            removed = queue.dequeue()
            print(f"Dequeued: {removed}")
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice! Please try again.")



menu()
