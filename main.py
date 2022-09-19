import argparse
import random

def main():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('chars', type=str, help='the letters to use')
    parser.add_argument('count', type=int, help='the number of characters to print')
    args = parser.parse_args()
    
    letters = list(set(args.chars))

    for _ in range(args.count):
      print(random.choice(letters), end='')
    print()


    

if __name__ == '__main__':
    main()