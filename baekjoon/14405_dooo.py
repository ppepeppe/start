val = input()
idx = 0
while idx < len(val):
    if val[idx] == 'p':
        if val[idx:idx+2] == 'pi':
            idx += 2
        else:
            print('NO')
            break
    elif val[idx] == 'k':
        if val[idx:idx+2] == 'ka':
            idx+=2
        else:
            print('NO')
            break
    elif val[idx] == 'c':
        if val[idx:idx+3] == 'chu':
            idx+=3
        else:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')