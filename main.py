import argparse
import random

def generate(set, count):
    return ''.join([random.choice(set) for _ in range(count)])

def main():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('chars', type=str, help='the letters to use')
    parser.add_argument('count', type=int, default=100, help='the number of characters to print')
    args = parser.parse_args()
    
    letters = list(set(args.chars))

    print(generate(letters, args.count))


    

if __name__ == '__main__':
    main()