#!/usr/bin/python3

if __name__ == "__main__":
    import add, sub, mul, div from calculator_1

    a = 10
    b = 5

    print('{0} + {1} = 2'.format(a, b, add(a, b)))
    print('{0} + {1} = 2'.format(a, b, sub(a, b)))
    print('{0} + {1} = 2'.format(a, b, mul(a, b)))
    print('{0} + {1} = 2'.format(a, b, div(a, b)))