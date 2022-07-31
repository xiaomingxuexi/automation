
def demo(name, age):
    print(name, age)

if __name__ == '__main__':
    name = ("bob","12")
    demo(*name)