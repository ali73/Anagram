from sys import argv
import argparse
from database import get_word

parser = argparse.ArgumentParser(description='anagram...')
parser.add_argument('--add',help='')



word = input("کلمه‌ی مورد نظر را وارد کنید:")
word = list(word)
result = get_word(''.join(sorted(list(word)))).all()
for ouput in result:
    print(ouput.word)