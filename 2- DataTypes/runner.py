if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_unique_list = list(set(arr))
    sorted_list = sorted(sorted_unique_list, reverse=True)
    print(sorted_list[1])
