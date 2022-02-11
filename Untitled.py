def main() :
   
    N = int(input('Enter a value for N: '))
    testCase(N)

def testCase(N):
    if N <= 0:
        return 0

    X = int(input('Enter a value for X: '))
    print(sumOfSquare(X))
    return testCase(N-1)


def sumOfSquare(X):
    if X == 0 :
        return 0
  
    Y = int(input('Enter a value for Y: '))
    if Y > 0 :
        return Y*Y + sumOfSquare(X-1)
    return sumOfSquare(X-1)

if __name__ == "__main__":
    main()