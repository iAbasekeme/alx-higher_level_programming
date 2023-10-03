#!usr/bin/python3
start_Ascii = 97
end_Ascii = 122
for i in range(start_Ascii, end_Ascii):
    if i not in [113, 101]:
        print('{}'.format(chr(i)), end="")
