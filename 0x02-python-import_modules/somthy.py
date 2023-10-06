#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
module_list = dir(hidden_4)
for i in module_list:
    if not i.startswith('__'):
        print("{}", format(i))
