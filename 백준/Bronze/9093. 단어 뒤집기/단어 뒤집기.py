import sys
from collections import deque

def reverse_word(input_sentence):
    words_list = input_sentence.split()

    for i, word in enumerate(words_list):
        if len(word) == 1:
            pass
        else:
            words_list[i] = word[::-1]

    reversed_result = ' '.join(words_list)

    return reversed_result


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        input_sentence = sys.stdin.readline()
        print(reverse_word(input_sentence))
