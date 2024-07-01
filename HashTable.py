class CreateNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.table = [None] * 100

    def hash(self, key):
        hashed = 0
        for char in key:
            hashed = (hashed * 31 + ord(char)) % len(self.table)
        return hashed

    def add(self, key):
        index = self.hash(key)
        if not self.table[index]:
            self.table[index] = CreateNode(key, index)
        else:
            temp = self.table[index]
            while temp.next:
                temp = temp.next
            temp.next = CreateNode(key, index)

    def remove(self, key):
        index = self.hash(key)
        if not self.table[index]:
            return False
        elif self.table[index].key == key:
            self.table[index] = self.table[index].next
            return True
        else:
            temp = self.table[index]
            while temp.next:
                if temp.next.key == key:
                    temp.next = temp.next.next
                    return True
                temp = temp.next
            return False

    def size(self):
        count = 0
        for head in self.table:
            temp = head
            while temp:
                count += 1
                temp = temp.next
        return count

    def contains(self, key):
        index = self.hash(key)
        temp = self.table[index]
        while temp:
            if temp.key == key:
                return True
            temp = temp.next
        return False

    def display(self):
        for i in range(len(self.table)):
            temp = self.table[i]
            while temp:
                print(f"Key: {temp.key}, Value: {temp.value}")
                temp = temp.next

    def exit(self):
        return exit(0)

    def task(self, old_option):
        tab = old_option.split(" ")
        option = tab[0]
        if len(tab) >= 1 and len(tab) < 2:
            key = tab[1]
        else:
            key = None

        if option == "add" and key!=None:
            self.add(key)
        elif option == "remove" and key!=None:
            self.remove(key)
        elif option == "size":
            print(self.size())
        elif option == "contains" and key!=None:
            print(self.contains(key))
        elif option == "display":
            self.display()
        elif option == "exit":
            self.exit()
        else:
            print("Invalid option. Please choose a valid option.")

def main():
    ht = HashTable()
    while True:
        try:
            choice = input("Enter command: ")
            ht.task(choice)
            if choice == "exit":
                break
        except IndexError:
            print("error")
            
if __name__ == "__main__":
    main()
