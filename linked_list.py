class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def to_array(self):
        arr = []
        if self.head is None:
            return arr
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr
        
    def print_linked_list(self):
        linkedListString = ""
        node = self.head
        if node is None:
            print(None)
            
        while node:
            linkedListString += f" {str(node.data)} ->"
            node = node.next_node
        linkedListString == " None"
        print(linkedListString)
        
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        
        new_node = Node(data, self.head)
        self.head = new_node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_beginning(data)
            return
        
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
        
# # linkedL = LinkedList()
# # node4 = Node("data4", None)
# # node3 = Node("data3", node4)
# # node2 = Node("data2", node3)
# # node1 = Node("data1", node2)

# # linkedL.head = node1

# # linkedL.print_linked_list()

# linkedLst = LinkedList()
# linkedLst.insert_beginning("data")
# linkedLst.insert_beginning("Not New data")

# linkedLst.insert_at_end("end")
# linkedLst.insert_at_end("endL")
# linkedLst.print_linked_list()