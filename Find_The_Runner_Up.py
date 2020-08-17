if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = list(arr)
    sorted_list = sorted(my_list)
    while True:    
        if sorted_list[-2] == sorted_list[-1]:
            sorted_list.pop()
        else:
            print (sorted_list[-2])
            break
