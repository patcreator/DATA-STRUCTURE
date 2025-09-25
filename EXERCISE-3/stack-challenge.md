# Stack Challenge: Reverse "QUEUEFIFO" using a Stack

## Algorithm Steps

1. **Initialize an empty stack.**
2. **Push each character of "QUEUEFIFO" onto the stack.**
3. **Pop each character from the stack and append to a result string.**
4. **The result string is the reversed word.**

## Explanation

- Stacks are LIFO (Last-In, First-Out). Pushing all characters and then popping them reverses the order.

## Code

```python
word = "QUEUEFIFO"
stack = []
# Step 2: Push each character
for char in word:
    stack.append(char)
# Step 3: Pop to reverse
reversed_word = ""
while stack:
    reversed_word += stack.pop()
print(reversed_word)  # Output: "OFIFEUEUQ"
```

## Output

```
OFIFEUEUQ
```