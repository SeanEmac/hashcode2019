def readFile(fileName):
    f = open(fileName, "r")
    contents =f.read()
    print(contents)
    f.close()


def main():
    readFile("a_example.in")
    readFile("b_small.in")


if __name__=="__main__":
    main()