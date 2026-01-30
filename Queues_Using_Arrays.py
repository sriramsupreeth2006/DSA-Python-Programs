class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print('Stack overflow')
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.top == -1:
            print("Stack underflow")
            return
        return self.stack[self.top]

    def display(self):
        if self.top == -1:
            print("Stack is empty")
            return
        for i in range(self.top, -1, -1):
            print(self.stack[i])


def main():
    size = int(input("Enter stack size: "))
    stack = Stack(size)

    while True:
        print("\nStack Menu:")
        print("1. Push the stack")
        print("2. Pop the stack")
        print("3. Peek the stack")
        print("4. Display the stack")
        print("5. Exit")

        choice = input("Enter the number of the menu operation you need: ")

        if choice == "1":
            data = int(input("Enter data to push: "))
            stack.push(data)
        elif choice == "2":
            print("Popped data:", stack.pop())
        elif choice == "3":
            print("Top data:", stack.peek())
        elif choice == "4":
            print("Stack data:")
            stack.display()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
