"""
By Michał Matuszyk
on 02/12/2023
"""

class Node:
    def __init__(self, val):
        self.value = val


    def __str__(self):
        return str(self.value)

class KopiecZupelny:


    def __init__(self):
        self.elementy = [];
        self.last_elem_index = -1;

    def isEmpty(self):
        if len(self.elementy) <= 0:
            return True
        return False

    def insert(self, newNode):
        if self.isEmpty():
            print("Dodano")
            self.elementy.append(newNode)
            self.last_elem_index = 0
            return
        # nie jest pusty, czyli ma conajmniej jeden elem
        self.elementy.append(newNode)
        self.last_elem_index += 1
        ostatni_elem = len(self.elementy)-1
        self.upHeap(ostatni_elem)
        # dodaj na koniec i upHeap

        return

    def upHeap(self, i): #i to start. elem.
        while True:
            if i == 0:
                break
            if self.elementy[(i-1)//2].value < self.elementy[i].value:
                # print("zamiana", self.elementy[(i-1)//2].value, "z", self.elementy[i].value)
                self.swap(i, (i-1)//2)
            else:
                break
            i = (i-1)//2
        return


    def swap(self, i, j):
        i_elem = self.elementy[i]
        j_elem = self.elementy[j]
        self.elementy[i] = j_elem
        self.elementy[j] = i_elem

    def downHeap(self, i):
        while True:
            left_child = i * 2 + 1
            right_child = i * 2 + 2
            max_index = i

            if left_child < len(self.elementy) and self.elementy[left_child].value > self.elementy[max_index].value:
                max_index = left_child

            if right_child < len(self.elementy) and self.elementy[right_child].value > self.elementy[max_index].value:
                max_index = right_child

            if max_index != i:
                self.swap(i, max_index)
                i = max_index
            else:
                break

    def pop(self):
        if self.isEmpty():
            print("Kopiec jest pusty :(")
            return None
        elif len(self.elementy) == 1:
            wynik = self.elementy[0]
            self.elementy = []
            return wynik
        else:
            wynik = self.elementy[0]
            self.elementy[0] = self.elementy[len(self.elementy)-1]
            self.elementy = self.elementy[:len(self.elementy)-1]
            self.downHeap(0)  # Call downHeap with the starting index 0
            return wynik

    def wypiszElementy(self):
        print("Aktualny kopiec:", end = "[ ")
        for element in self.elementy:
            print(str(element), end = " ")
        print("]")

    # def sprPoprawnosc(self):
    #     for i in range(len(self.elementy)):




if __name__ == "__main__":
    kopiec1 = KopiecZupelny();
    print("Czy pusty:", kopiec1.isEmpty())
    for i in range(10):
        kopiec1.insert(Node(i))
        kopiec1.wypiszElementy()
    for i in range(10):
        print(kopiec1.pop())
        kopiec1.wypiszElementy()