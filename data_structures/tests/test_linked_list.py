from data_structures.linked_list.main import LinkedList, DoubleLinkedList

# ---------- Singly Linked List Tests ----------

def test_linked_list_append_and_display(capsys):
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()
    captured = capsys.readouterr()
    assert "10" in captured.out
    assert "20" in captured.out
    assert "30" in captured.out

def test_linked_list_find():
    ll = LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")
    assert ll.find(0) == "a"
    assert ll.find(2) == "c"

def test_linked_list_delete():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete(1)  # delete "2"
    assert ll.find(1) == 3

def test_linked_list_reverse():
    ll = LinkedList()
    ll.append("x")
    ll.append("y")
    ll.append("z")
    ll.reverse()
    assert ll.find(0) == "z"
    assert ll.find(2) == "x"

# ---------- Doubly Linked List Tests ----------

def test_double_linked_list_append_and_display(capsys):
    dll = DoubleLinkedList()
    dll.append("first")
    dll.append("second")
    dll.append("third")
    dll.display()
    captured = capsys.readouterr()
    assert "first" in captured.out
    assert "second" in captured.out
    assert "third" in captured.out

def test_double_linked_list_find():
    dll = DoubleLinkedList()
    dll.append(100)
    dll.append(200)
    dll.append(300)
    assert dll.find(0) == 100
    assert dll.find(2) == 300

def test_double_linked_list_delete():
    dll = DoubleLinkedList()
    dll.append("a")
    dll.append("b")
    dll.append("c")
    dll.delete(1)  # delete "b"
    assert dll.find(1) == "c"

def test_double_linked_list_reverse():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.reverse()
    assert dll.find(0) == 3
    assert dll.find(2) == 1