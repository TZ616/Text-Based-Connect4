def file_out(moves, lis):
    with open(input("Enter the file name you want to export to, with the extension: "), "w") as write:
        write.write(f"{moves}\n")
        for i in lis[0]:
            write.write(i)
        for _ in lis[1:]:
            write.write("\n")
            for i in _:
                write.write(i)
