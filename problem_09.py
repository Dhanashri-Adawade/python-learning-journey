# -------------------------------
# 1. LIST (Mutable, Ordered)
# -------------------------------
print("LIST:")
my_list = [10, 20, 30, 40]
my_list.append(50)        # Add element
my_list.remove(20)        # Remove element
print(my_list)
print()

# -------------------------------
# 2. TUPLE (Immutable, Ordered)
# -------------------------------
print("TUPLE:")
my_tuple = (1, 2, 3, 4)
print(my_tuple)
print(my_tuple[1])        # Access element
print()

# -------------------------------
# 3. SET (Unordered, Unique)
# -------------------------------
print("SET:")
my_set = {1, 2, 3, 3, 4}
my_set.add(5)
my_set.remove(2)
print(my_set)
print()

# -------------------------------
# 4. DICTIONARY (Key-Value Pair)
# -------------------------------
print("DICTIONARY:")
my_dict = {
    "name": "Dhanashri",
    "age": 20,
    "course": "Computer Engineering"
}
my_dict["city"] = "Mumbai"   # Add new key
print(my_dict)
print(my_dict["name"])       # Access value
print()

# -------------------------------
# 5. STACK (Using List - LIFO)
# -------------------------------
print("STACK:")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())   # Removes last element
print(stack)
print()

# -------------------------------
# 6. QUEUE (Using List - FIFO)
# -------------------------------
print("QUEUE:")
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print(queue.pop(0))  # Removes first element
print(queue)
print()

# -------------------------------
# 7. STRING (Immutable)
# -------------------------------
print("STRING:")
text = "Hello"
print(text.upper())
print(text[1])
print()

# -------------------------------
# 8. ARRAY (Using List)
# -------------------------------
print("ARRAY:")
arr = [5, 10, 15, 20]
print(arr)
print(arr[2])