import os
import sys

import chardet


def check(_filename, _str_list):
    a = True
    for _str in _str_list:
        if _filename.split('.')[-1] == _str:
            a = False
    return a


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid argments.")
        exit(121)
    name = ['c', 'h', 'md', 'txt', 'sh', 'py', 'xml', 'conf', 'plist', 'json', 'log', 'lua', 'ini']
    for filepath, dir_names, filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            try:
                name.index(filename.split('.')[-1])
                with open(filepath + '/' + filename, 'rb') as f:
                    encode = chardet.detect(f.read())
                print(filepath + '/' + filename)
                print(encode)
                with open(filepath + '/' + filename, encoding=encode['encoding']) as f:
                    content = f.read()
                with open(filepath + '/' + filename, 'w', encoding='utf-8') as f:
                    f.write(content)
            except ValueError:
                pass
