import queue

value = queue.SimpleQueue()

value.put("[1,2,3]")
print(value.get(timeout=1.0))
try:
    value = value.get(timeout=1.0)
except queue.Empty:
    print("Empty")

