def milim():
    f = open('c:\milim.txt', 'r', encoding="utf8").readlines()
    for line in f:
        print (line)
    return f
