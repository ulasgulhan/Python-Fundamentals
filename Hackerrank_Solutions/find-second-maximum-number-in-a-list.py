if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_array = list(arr)
    print(max([x for x in my_array if x != max(my_array)]))