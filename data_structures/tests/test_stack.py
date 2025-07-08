import pytest
from data_structures.stack.main import ArrayStack, LinkedListStack

# ---------- ArrayStack Tests ----------

def test_array_stack_push_and_peek():
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    stack.push(3)
    assert stack.peek() == 3

def test_array_stack_pop():
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    popped = stack.pop()
    assert popped == 20
    assert stack.peek() == 10

def test_array_stack_is_empty():
    stack = ArrayStack()
    assert stack.is_empty()
    stack.push("x")
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()

def test_array_stack_underflow_pop():
    stack = ArrayStack()
    with pytest.raises(Exception, match="Stack is empty"):
        stack.pop()

def test_array_stack_underflow_peek():
    stack = ArrayStack()
    with pytest.raises(IndexError):
        stack.peek()


# ---------- LinkedListStack Tests ----------

def test_linked_list_stack_push_and_peek():
    stack = LinkedListStack()
    stack.push("a")
    stack.push("b")
    assert stack.peek() == "b"
    stack.push("c")
    assert stack.peek() == "c"

def test_linked_list_stack_pop():
    stack = LinkedListStack()
    stack.push(100)
    stack.push(200)
    popped = stack.pop()
    assert popped == 200
    assert stack.peek() == 100

def test_linked_list_stack_is_empty():
    stack = LinkedListStack()
    assert stack.is_empty()
    stack.push("data")
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()

def test_linked_list_stack_underflow_pop():
    stack = LinkedListStack()
    with pytest.raises(Exception, match="Stack is empty"):
        stack.pop()

def test_linked_list_stack_underflow_peek():
    stack = LinkedListStack()
    with pytest.raises(Exception, match="Linked list is empty"):
        stack.peek()