from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def _overwrite(self, item):
        self.storage.add_to_head(item)
        if self.current == self.storage.tail:
            self.current = self.storage.head
        self.storage.remove_from_tail()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            if self.storage.length == 1:
                self.current = self.storage.tail
        else:
            self._overwrite(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        run = self.current
        while run is not None:
            list_buffer_contents.append(run.value)
            run = run.prev
        if self.current is not self.storage.tail:
            run = self.storage.tail
            while run is not self.current:
                list_buffer_contents.append(run.value)
                run = run.prev
        return list_buffer_contents

buf = RingBuffer(4)
for n in range(7):
    buf.append(n)
    print(buf.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
