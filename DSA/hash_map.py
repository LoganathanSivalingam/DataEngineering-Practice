class HashFunction():

    def __init__(self,n):

        self.hash_storage = [None] * n

    def hash_value(self,key):

        self.key = key
        self.hashValue = hash(key) % len(self.hash_storage)
        
        return self.hashValue
    
    def set(self,key,value):

        index = self.hash_value(key)

        if self.hash_storage[index] == None:

            self.hash_storage[index] = []
            self.hash_storage[index].append([key,value])

        else :

            self.hash_storage[index].append([key,value])


    def get(self,key):

        find_index = self.hash_value(key)

        if self.hash_storage[find_index] is not None:

            for i in range(0,len(self.hash_storage[find_index])):
                if self.hash_storage[find_index][i][0] == key:
                    return self.hash_storage[find_index][i][1]
            return None

    def delete(self,key):

        find_index = self.hash_value(key)

        if self.hash_storage[find_index] is not None:

            for i in range(0,len(self.hash_storage[find_index])):
                if self.hash_storage[find_index][i][0] == key:
                    self.hash_storage[find_index].remove(self.hash_storage[find_index][i])
                    return self.hash_storage
            return self.hash_storage

    
class HashLinearProbing() :

    def __init__(self,n):

        self.table_size = n
        self.hash_table = [None]*n

    def get_hash_value(self,key):

        i = 0
        hash_value = (hash(key)+i) % self.table_size

        while self.hash_table[hash_value] != None:

            i += 1

            if i == len(self.hash_table):
                raise Exception("Table is full")
        
            hash_value = (hash(key)+i) % self.table_size

        return hash_value
    
    def add(self,**kwargs):

        for key , value in kwargs.items():

            try:
                hash_value = self.get_hash_value(key)

            except Exception as e:
                print(e)
                break

            if self.hash_table[hash_value] is None:
                self.hash_table[hash_value] = [key,value] 

    
    def get(self,key):

        i = 0
        hash_value = (hash(key)+i) % self.table_size

        while self.hash_table[hash_value] != None and self.hash_table[hash_value][0] != key:

            i+=1

            if i == self.table_size:
                return "Key Not Found"
                exit
            hash_value = (hash(key)+i) % self.table_size
        
        if self.hash_table[hash_value] != None and self.hash_table[hash_value][0] == key:
            return self.hash_table[hash_value][1]
        
        return


hashLP = HashLinearProbing(3)

hashLP.add(apple=10,banana=20)   
print(hashLP.hash_table)
print(hashLP.get("apple"))
print(hashLP.get("orange"))
print(hashLP.get("banana"))
print(hashLP.get("grape"))



