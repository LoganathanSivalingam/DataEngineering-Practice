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

    
test = HashFunction(3)
test.set("apple",100)
test.set("banana",54)
test.set("orange",20)
print(test.get("orange"))
print(test.delete("orange"))
