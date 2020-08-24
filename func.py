def hello(a, b):
    print(a + b)
    
hello(21, 29)

# 5.4 演習(1)
def calc(a, b):
    print(a * b)
    
calc(2, 3)

# 5.4 演習(2)
def traingle_area(a, h):
    return a * h / 2
    
print(traingle_area(2,3))

# 5.4 演習(3)
file_list = []
def add_list(name):
    file_name = name + ".py"
    file_list.append(file_name)

add_list("function")
print(file_list)
# ['function.py']と表示される
add_list("hello")
print(file_list)
# ['function.py', 'hello.py']と表示される
