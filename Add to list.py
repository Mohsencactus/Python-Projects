def firstletter(data,list = []):
    n = len(list)
    if (n == 0) or (n > 0 and list[n-1] != data):
        list.append(data)
    else:
        pass
    return list


while True:
    qr = 'abcdefg'
    a = firstletter(qr)
    print(a)