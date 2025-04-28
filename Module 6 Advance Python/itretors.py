class MyItrator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value =  self.data[self.index]
        self.index += 1
        return value

my_list = [1, 2, 3, 4, 5]
my_itrator = MyItrator(my_list)

for itom in my_itrator:
    print(itom)