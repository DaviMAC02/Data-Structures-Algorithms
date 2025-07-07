from queues.main import ArrayQueue, LinkedListQueue

def test_array_queue_operations():
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 2
    assert q.size() == 1
    assert not q.is_empty()

def test_linked_list_queue_operations():
    q = LinkedListQueue()
    q.enqueue(5)
    q.enqueue(6)
    assert q.peek().data == 5
    q.dequeue()
    assert q.peek().data == 6
    assert q.size() == 1