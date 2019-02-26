def readFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()

    firstLine = lines[0].split(" ")

    R = firstLine[0]
    C = firstLine[1]
    L = firstLine[2] 
    H = firstLine[3]

    print(R, C, L, H)

def main():
    readFile("a_example.in")
    readFile("b_small.in")


if __name__=="__main__":
    main()