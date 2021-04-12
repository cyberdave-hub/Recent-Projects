r, i = input().split("|")

def compare(r, i):
    if r == "":
        print("True")
    elif i == "":
        print("False")
    elif len(r) == len(i) == 1:
        if r[0] == i[0] or r[0] == ".":
            print("True")
        else:
            print("False")
    elif r[0] == "^":
        compare(r[1:], i[:len(r) - 1])
    elif r[len(r) - 1:] == "$":
        if (len(r) - 1) < len(i):
            compare(r[:len(r) - 1], i[len(r):])
        else:
            compare(r[:len(r) - 1], i[:len(r) - 1])
    elif len(r) < len(i) and r[0] != i[0]:
        compare(r, i[1:])
    elif len(r) == len(i) and r[0] == i[0] or r[0] == ".":
        compare(r[1:], i[1:])
    elif r in i:
        print("True")
    else:
        print("False")

compare(r, i)
