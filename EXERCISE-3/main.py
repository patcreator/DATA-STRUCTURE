# DATA STRUCTURE - BIT - EXERCISE NO:4

# --- Stack Practical 1 ---
print("Stack Practical 1 (MoMo):")
stack = []
stack.append("Enter PIN")
stack.append("Enter Amount")
stack.append("Confirm")
print("Initial stack:", stack)
# Undo last
stack.pop()
print("After undo (pop):", stack)
print("Remains:", stack)
print("-" * 40)

# --- Stack Practical 2 ---
print("Stack Practical 2 (UR):")
stack = []
stack.append("Topic1")
stack.append("Topic2")
stack.append("Topic3")
print("Initial stack:", stack)
# Pop two
stack.pop()
stack.pop()
print("After popping two:", stack)
print("Top of stack:", stack[-1] if stack else "Empty")
print("-" * 40)

# --- Queue Practical 1 ---
from collections import deque

print("Queue Practical 1 (CHUK):")
queue = deque(range(1, 11))  # Patients 1 to 10
print("Initial queue:", list(queue))
# Serve 6
for _ in range(6):
    queue.popleft()
print("After serving 6:", list(queue))
print("Patient in front:", queue[0])
print("-" * 40)

# --- Queue Practical 2 ---
print("Queue Practical 2 (BK ATM):")
queue = deque(range(1, 10))  # Clients 1 to 9
print("Initial queue:", list(queue))
print("Second in queue:", queue[1])
print("-" * 40)

# --- Screenshot-style outputs ---
print("""
--- Screenshot-style Outputs ---

Stack Practical 1 (MoMo):
Initial stack: ['Enter PIN', 'Enter Amount', 'Confirm']
After undo (pop): ['Enter PIN', 'Enter Amount']
Remains: ['Enter PIN', 'Enter Amount']

Stack Practical 2 (UR):
Initial stack: ['Topic1', 'Topic2', 'Topic3']
After popping two: ['Topic1']
Top of stack: Topic1

Queue Practical 1 (CHUK):
Initial queue: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After serving 6: [7, 8, 9, 10]
Patient in front: 7

Queue Practical 2 (BK ATM):
Initial queue: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Second in queue: 2
""")