class Pizza:
  def __init__(self, R, C, Min, Max, numT, numM):
    self.R = R
    self.C = C
    self.Min = Min
    self.Max = Max
    self.numT = numT
    self.numM = numM
    

def processFile(fileName):
    f = open(fileName)
    lines = f.readlines()

    R, C, Min, Max = map(int, lines[0].split())

    matrix = []
    numT = 0
    numM = 0

    for i in range(1, R+1):
        line = lines[i].rstrip()
        chars = list(line)
    
        matrix.append(chars)

        numT += chars.count('T')
        numM += chars.count('M')

    pizza1 = Pizza(R, C, Min, Max, numT, numM)

def main():
    fileNames = ["a_example.in", "b_small.in", "c_medium.in", "d_big.in"]

    for file in fileNames:
        processFile(file)


if __name__=="__main__":
    main()