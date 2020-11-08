class CuckooHashing: 
    def __init__(self, size): # 
        self.M = size
        self.h = [[None, None] for x in range(size+1)]  # h-table
        self.d = [[None, None] for x in range(size+1)]  # d-table

    def hash(self, key):        # h-hash function, h(key)
        return key % self.M      
    
    def hash2(self, key):       # d-hash function, d(key)
        return (key*key % 17) *11 % self.M  
    
    def put(self, key, data): # item (key,data) 삽입위한 method 
        def in_to_h(key,data):
            h = self.hash(key)
            if(self.h[h][0]!=None):
                nK = self.h[h][0]
                nV = self.h[h][1]
                self.h[h] = [None,None] #초기화, Loop 해결
                in_to_d(nK,nV)
            self.h[h] = [key,data]
        def in_to_d(key,data):
            d = self.hash2(key)
            if(self.d[d][0]!=None):
                nK = self.d[d][0]
                nV = self.d[d][1]
                self.d[d] = [None, None] #초기화, Loop 해결
                in_to_h(nK,nV)
            self.d[d] = [key,data]
        in_to_h(key,data)

        #### 구현하시오. 
                                 
    def get(self, key): # key 값에 해당하는 value 값을 return 
        h = self.hash(key)
        d = self.hash2(key)
        if(self.h[h][0]==key):
            return self.h[h][1]
        elif(self.d[d][0]==key):
            return self.d[d][1]
        return None
        #### 구현하시오.

    def delete(self, key): # key를 가지는 item 삭제 
        h = self.hash(key)
        d = self.hash2(key)
        if(self.h[h][0]==key):
            self.h[h] = [None,None]
        elif(self.d[d][0]==key):
            self.d[d] = [None,None]
        #### 구현하시오. 

    def print_table(self):
        print('********* Print Tables ************')
        print('h-table:')
            #### h-table 출력 : 구현하시오 
        print('\t'.join([str(i) for i in range(len(self.h))]))
        print('\t'.join([str(i[0]) for i in self.h]))


        print('d-table:')
            #### d-table 출력 : 구현하시오 
        print('\t'.join([str(i) for i in range(len(self.d))]))
        print('\t'.join([str(i[0]) for i in self.d]))

if __name__ == '__main__':
    t = CuckooHashing(13)
    t.put(25, 'grape')      # 25:  12,   0
    t.put(43, 'apple')      # 43:   4,   0
    t.put(13, 'banana')     # 13:   0,   7
    t.put(26, 'cherry')     # 26:   0,   0
    t.put(39, 'mango')      # 39:   0,  10
    t.put(71, 'lime')       # 71:   9,   8
    t.put(50, 'orange')     # 50:  11,  11
    t.put(64, 'watermelon') # 64:  12,   7
    print()
    print('--- Get data using keys:')
    print('key 50 data = ', t.get(50))
    print('key 64 data = ', t.get(64))
    print()
    t.print_table() 
    print()
    print('-----  after deleting key 50 : ---------------')
    t.delete(50)
    t.print_table() 
    print()
    print('key 64 data = ', t.get(64))
    print('-----  after adding key 91 with data berry:---------------')
    t.put(91, 'berry')
    t.print_table()
    print()
    print('-----  after changing data with key 91 from berry to kiwi:---------------')
    t.put(91, 'kiwi')       # 91:  0,   9
    print('key 91 data = ', t.get(91))    
    t.print_table()
    
