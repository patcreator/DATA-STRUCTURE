# Queue Challenge: Queue vs Stack for Polling Station

## Algorithmic Comparison

### Queue (FIFO)
1. Voters join at the end.
2. First to join is first to vote.
3. No one can skip the line.

### Stack (LIFO)
1. Voters join at the top.
2. Last to join is first to vote.
3. Early arrivals may wait longer.

## Code Illustration

```python
# Queue
from collections import deque
queue = deque(["Alice", "Bob", "Carol"])
queue.append("David")
print(queue.popleft())  # Alice

# Stack
stack = []
stack.append("Alice")
stack.append("Bob")
stack.append("Carol")
stack.append("David")
print(stack.pop())  # David
```

## Explanation

- **Queue** is fair: order of arrival = order of service.
- **Stack** is unfair: last arrival is served first.

**Conclusion:** Queue is fair for polling stations.