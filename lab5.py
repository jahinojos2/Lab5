class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)

        self.percolate_up(len(self.heap_array) - 1)

    # TODO: Complete implementation
    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2

            # check for a violation of the max heap property
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[parent_index]
                self.heap_array[parent_index] = self.heap_array[node_index]
                self.heap_array[node_index] = temp

                # continue the loop from the parent node
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the max among the node and the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i = i + 1

            # check for a violation of the max heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[max_index]
                temp = self.heap_array[min_index]
                self.heap_array[min_index] = self.heap_array[node_index]
                self.heap_array[node_index] = temp

                # continue loop from the larger child node
                node_index = min_index
                child_index = 2 * node_index + 1

    def remove(self):
        # save the max value from the root of the heap.
        min_value = self.heap_array[0]

        # move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value

            # percolate down to restore max heap property.
            self.percolate_down(0)

        # return the max value
        return min_value


    def extract_min(self):

        if self.is_empty():
            return None

        min_elem = self.remove()

    # TODO: Complete implementation
        return min_elem


    def is_empty(self):
        return len(self.heap_array) == 0


def min_heap_percolate_down(node_index, heap_list, list_size):
    child_index = 2 * node_index + 1
    value = heap_list[node_index]

    while child_index < list_size:
        # Find the max among the node and all the node's children
        min_value = value
        min_index = -1
        i = 0
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > min_value:
                min_value = heap_list[i + child_index]
                min_index = i + child_index
            i = i + 1

        if min_value == value:
            return

        # Swap heap_list[node_index] and heap_list[max_index]
        temp = heap_list[min_index]
        heap_list[min_index] = heap_list[node_index]
        heap_list[node_index] = temp

        node_index = min_index
        child_index = 2 * node_index + 1

def heap_sort(numbers):
        # Heapify numbers list
        i = len(numbers) // 2 - 1
        while i >= 0:
            min_heap_percolate_down(i, numbers, len(numbers))
            i = i - 1

        i = len(numbers) - 1

        while i > 0:
            # Swap numbers[0] and numbers[i]
            temp = numbers[0]
            numbers[0] = numbers[i]
            numbers[i] = temp

            min_heap_percolate_down(0, numbers, i)
            i = i - 1

def main(a):
    heap_array = Heap()

    with open(a) as f:
        list = f.read().splitlines()

    for i in list:
        heap_array.insert(int(i))
    print('Heap array created after reading the file: ')
    print(heap_array.heap_array)
    print('')
    heap_sort(heap_array.heap_array)
    print('')
    print('Heap array after min heap sorting: ')
    print(heap_array.heap_array)
    print('')
    print('Extracting min of heap array: ')
    print(heap_array.extract_min())
    print('')
    print('Heap array after extract min: ')
    print(heap_array.heap_array)
a = 'textfile.txt'
main(a)