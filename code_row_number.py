with open("my_file.txt", "r") as fobj_in:
    with open("my_file2.txt", "w") as fobj_out:
        i = 1
        for line in fobj_in:
            print(line.rstrip())
            fobj_out.write(str(i) + ": " + line)
            i = i + 1
