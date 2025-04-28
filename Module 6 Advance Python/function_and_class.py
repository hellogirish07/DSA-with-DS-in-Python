import time

def timing_decorator(func):
    def wrapper(*args, **kaargs):
        start_time = time.time()
        result = func(*args, **kaargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time: .4f} seconds ")
        return result
    
    return wrapper

def slow_function():
    time.sleep(2)
    return "Function Completed"

print(slow_function())