import sys

def binary_tree(trees_height, target):
    start = 0
    end = max(trees_height)
    
    while start<=end:    
        mid= (start+end)//2
        sum_trees = 0

        for tree in trees_height:
            if tree >= mid:
                sum_trees += (tree-mid)

        # if sum_trees == target:
        #     return(mid)
        if sum_trees >= target:
            start = mid+1
        else:
            end = mid-1

    return end


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    trees_height = list(map(int, sys.stdin.readline().split()))

    print(binary_tree(trees_height, M))