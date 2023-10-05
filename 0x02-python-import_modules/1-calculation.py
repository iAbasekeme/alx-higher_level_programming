#!/usr/bin/python3
import calculator_1
if __name__ == "__main__":
    a = 10
    b = 5

    operation_add = calculator_1.add(a, b)
    operation_sub = calculator_1.sub(a, b)
    operation_mul = calculator_1.mul(a, b)
    operation_div = calculator_1.div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, operation_add))
    print("{:d} - {:d} = {:d}".format(a, b, operation_sub))
    print("{:d} * {:d} = {:d}".format(a, b, operation_mul))
    print("{:d} / {:d} = {:d}".format(a, b, operation_div))
