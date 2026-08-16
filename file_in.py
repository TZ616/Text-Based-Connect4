def file_in():
    lis = []
    while (1):
        try:
            read = open(input("Enter the file name you want to import from, with the extension: "), 'r')
        except FileNotFoundError:
            print("File could not be located!")
        else:
            break
    l = read.readlines()
    moves = int(l[0])
    for _ in l[1:]:
        lis.append([])
        temp = _.strip()
        for j in temp:
            lis[len(lis)-1].append(j)
    return moves, lis