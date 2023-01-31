n = int(input())
lst = list(map(int, input().split()))

m = int(input())
search = list(map(int, input().split()))

for i in search:
    s = 0
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if lst[mid] == i:
            print('yes')
            break
        elif lst[mid] > i:
            e = mid - 1
        else:
            s = mid + 1
    else:
        print('no')