import os
import sys
import argparse

class MyWC():
    def count_lines(self, data):
        print(data.count('\n'), end=' ')

    def count_words(self, data):
        print(len(data.split(None)), end=' ')

    def count_bytes(self, data):
        print(len(data.encode('utf-8')), end=' ')

    def counter(self, data, args):
        if args.l:
            self.count_lines(data)
        if args.w:
            self.count_words(data)
        if args.c:
            self.count_bytes(data)
        if args.l == args.w == args.c == False:
            self.count_lines(data)
            self.count_words(data)
            self.count_bytes(data)

    def file_open(self, path):
        with open(path) as f:
            data = f.read()
        return data

    def args_parser(self, data_input):
        parser = argparse.ArgumentParser(prog='wc.py')
        parser.add_argument('file', nargs='?', help='filename', default=sys.stdin)
        parser.add_argument('-l', action='store_true', help='print the new line counts')
        parser.add_argument('-w', action='store_true', help='print the word counts')
        parser.add_argument('-c', action='store_true', help='print the byte count')
        return parser.parse_args()

if __name__ == '__main__':
    data_input = sys.stdin
    wc = MyWC()
    args = wc.args_parser(data_input)
    filename = args.file

    if data_input.isatty():
        try:
            if os.path.isfile(filename):
                data = wc.file_open(filename)
                wc.counter(data, args)
                print('\t{}'.format(filename))
        except TypeError:
            data = sys.stdin.read()
            wc.counter(data, args)
            print('')
    else:
        data = filename.read()
        wc.counter(data, args)
        print('')
