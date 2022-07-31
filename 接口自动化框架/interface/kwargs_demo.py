

def param_demo(a=None, b=None, *args, **kwargs):
    print(f"a的值为{a}，b的值为{b}")
    print(f"{args}")
    print(f"{kwargs}")


if __name__ == '__main__':
    param_demo(1, 2, 3, 4, 5, d=23, c=33)
