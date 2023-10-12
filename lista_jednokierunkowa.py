"""
By Michał Matuszyk
on 12/10/2023
"""

class listaJednokierunkowa:
    def __init__(self):
        head = None

    def addElementToEnd(self, newElement):
        if self.head == None:
            head = newElement
        current_element = self.head
        while current_element.next != None:
            current_element = current_element.next
        current_element.next = newElement

    def removeLastElement(self):
        if self.head == None: # if list is empty - do nothing
            return
        if self.head.next == None: # if only 1 elem. in list - remove the head
            self.head = None
        # Now we know, that the list contains a head and a next elem.
        current_element = self.head.next
        previous_elem = self.head
        while current_element.next != None:
            previous_elem = current_element
            current_element = current_element.next
        previous_elem.next = None


    def __len__(self):
        if self.head == None:
            return 0
        i = 1
        currentElement = self.head
        while currentElement.next != None:
            currentElement = currentElement.next
            i += 1
        return i
