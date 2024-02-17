import sys
    

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    levels = list(map(int, sys.stdin.readline().split()))

    sorted_levels = sorted(levels)
    sorted_levels.reverse()
    gold=0

    for i in range(1, len(sorted_levels)):
        gold += (sorted_levels[0]+sorted_levels[i])


    print(gold)