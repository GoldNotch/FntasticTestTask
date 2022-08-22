import sys
def main(args):
    for input_str in args:
        input_str = input_str.lower()
        counts = [0] * 256
        for c in input_str:
            counts[ord(c)] += 1
        output = ''.join(['(' if counts[ord(c)] == 1 else ')' for c in input_str])
        print(input_str, ' => ', output)

if __name__ == "__main__":
   main(sys.argv[1:])