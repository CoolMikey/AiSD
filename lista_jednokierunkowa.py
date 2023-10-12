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
        while self.head.next != None:
            current_element = current_element.next
        current_element.next = newElement