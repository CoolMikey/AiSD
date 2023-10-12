"""
By Michał Matuszyk
on 12/10/2023
"""
from simpleElement import simpleElement
from lista_jednokierunkowa import listaJednokierunkowa



def createASimpleList(n): #create a simple list with n elements, only one-way (next)
    if n < 0:
        raise Exception("Number of elements can't be less than 0")
    if n == 1:
        return listaJednokierunkowa()
    # n > 1
    head = simpleElement(0)
    current_elem = head
    for i in range(n-1):
        current_elem.next = simpleElement(i+1)
        current_elem = current_elem.next
    wynik = listaJednokierunkowa()
    wynik.head = head
    return wynik


def demonstrate_simple_list():
    lista_1 = createASimpleList(10) # creates a simple 10 element list
    print("Liczba elem. listy:", len(lista_1))
    #### Add an element
    new_element = simpleElement("Nowa wartosc xyz")
    lista_1.addElementToEnd(new_element)
    print("Liczba elem. listy po dodaniu:", len(lista_1))
    lista_1.removeLastElement()
    print("Liczba elem. listy po usunieciu:", len(lista_1))


if __name__ == "__main__":
    demonstrate_simple_list()