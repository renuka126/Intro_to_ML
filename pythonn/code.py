class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  

    
    def hash_function(self, key):
        return key % self.size

    
    def insert(self, key, value):
        index = self.hash_function(key)
       
        for node in self.table[index]:
            if node.key == key:
                node.value = value
                return
   
        self.table[index].append(HashNode(key, value))


    def search(self, key):
        index = self.hash_function(key)
        for node in self.table[index]:
            if node.key == key:
                return node.value
        return "Key not found"

   
    def delete(self, key):
        index = self.hash_function(key)
        for i, node in enumerate(self.table[index]):
            if node.key == key:
                del self.table[index][i]
                print(f"Key {key} deleted")
                return
        print("Key not found")


    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            for node in bucket:
                print(f"[{node.key} -> {node.value}]", end=" ")
            print()



if __name__ == "__main__":
    ht = HashTable()

 
    ht.insert(10, "Apple")
    ht.insert(20, "Banana")
    ht.insert(25, "Mango")  

    ht.display()

    
    print("Search 20:", ht.search(20))
    print("Search 15:", ht.search(15))

    
    ht.delete(20)
    ht.display()

