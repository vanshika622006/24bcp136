stack = []

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        item = input("Enter item to push: ")
        stack.append(item)
    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty!")
    elif choice == 3:
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty!")
    elif choice == 4:
        print("Stack:", stack)
    elif choice == 5:
        break
    else:
        print("Invalid choice!")