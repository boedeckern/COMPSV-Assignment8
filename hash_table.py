class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self,name,number):
        self.name=name
        self.number=number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self,size):
        self.size=size
        self.data=[None]*size

    def hash_function(self,key):
        total=0
        for char in key:
            total+=ord(char)
        return total % self.size

    def insert(self,key,value):
        index=self.hash_function(key)
        current=self.data[index]
        if self.data[index] is None:
            self.data[index]=Node(key,value)
            return
        while current:
            if current.key==key:
                current.value=value
                return
            if current.next is None:
                break
            current=current.next
        current.next=Node(key,value)

    def search(self,key):
        index=self.hash_function(key)
        current=self.data[index]
        while current:
            if current.key==key:
                return current.value
            current.value=next
        return None

    def print_table(self):
        index=0
        for contact in self.data:
            if contact is None:
                print(f"Index {index}: Empty")
            elif contact.next is None:
                print(f"Index {index}: - {contact.key}: {contact.value}")
            else:
                print(f"Index {index}: {self.print_table_iterate(index,0)}")
            index=index+1

    def print_table_iterate(self,index,iterate):
        current=self.data[index]
        temp=iterate
        while temp>0:
            current=current.next
            temp=temp-1
        if current.next is None:
            return f"- {current.key}: {current.value} "
        else:
            return f"- {current.key}: {current.value} {self.print_table_iterate(index,iterate+1)}"




# Test your hash table implementation here.  
table=HashTable(10)
table.insert("John","909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.insert("Amy", "111-222-3333")
table.insert("May","222-333-1111")
table.insert("Rebecca","999-444-9999")
print(table.search("Chris"))
#table.print_table()