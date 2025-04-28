# def simple_genrator():
#     # yield 1
#     # yield 2
#     # yield 3
    
#     for i in range(10):
#         yield i

# gen = simple_genrator()

# for value in gen:
#     print(value)

def fibonacchi_genrator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    
fin_gen = fibonacchi_genrator()
for i in range(10):
    print(next(fin_gen))  