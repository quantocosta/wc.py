# Description
Simple wc implementation in Python 3. Supports lines, words and bytes count from file or console input. For example:

```sh
$ cat sample.txt | python3 wc.py
5 40 541
```

```sh
$ python3 wc.py sample.txt
5 40 541    sample.txt
```

```sh
$ python3 wc.py -w -l
Lorem ipsum dolor sit amet, 
consectetur adipiscing 
elit, sed do eiusmod 

tempor incididunt ut 
labore et 
dolore magna 
aliqua
8 19
```

# Usage
```sh
usage: wc.py [-h] [-l] [-w] [-c] [file]

positional arguments:
  file        filename

optional arguments:
  -h, --help  show this help message and exit
  -l              print the new line counts
  -w            print the word counts
  -c             print the byte count
```
