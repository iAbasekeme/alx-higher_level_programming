#!/usr/bin/python3
start_ascii = 97
end_ascii = 122
for i in range(start_ascii, end_ascii+1):
    txt = chr(i)
    print(txt.format(), end="")
