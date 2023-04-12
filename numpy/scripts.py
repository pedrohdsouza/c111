import numpy as np

def printQuestionNumber(number):
    print("---Questão " + str(number) + "---")
    print()

def printAnswer(answer):
    print(answer)
    print()

def arrayForQuestion2And3():
        arrayEvenBetween0To51 = np.arange(0, 51, 2)
        arrayEvenBetween50To101 = np.arange(50, 101, 2)
        arrayReordered101To50 = np.flip(arrayEvenBetween50To101)
        arrayConcatenate = np.concatenate([arrayEvenBetween0To51, arrayReordered101To50])
        return(arrayConcatenate)

def questionSolution(question):
    if (question == 1):
        printQuestionNumber(1)

        arrayLinearlySpacedBetween0And1With21Values = np.linspace(0, 1, 21)

        printAnswer(arrayLinearlySpacedBetween0And1With21Values)
    elif (question == 2):
        printQuestionNumber(2)

        arraySort = np.sort(arrayForQuestion2And3())

        printAnswer(arraySort)
    elif (question == 3):
        printQuestionNumber(3)

        arrayReverse = np.sort(arrayForQuestion2And3())[::-1]

        printAnswer(arrayReverse)
    elif (question == 4):
        printQuestionNumber(4)

        matrixOfOnes = np.ones((3,4))
        print(matrixOfOnes)
        print()
        convertedToArray = matrixOfOnes.reshape(-1)
        
        printAnswer(convertedToArray)
    elif (question == 5):
        printQuestionNumber(5)

        matrix = np.array([[21,29,34,38],[60,66,7,1]])
        print(matrix)
        print()
        lines = matrix.shape[0]
        columns = matrix.shape[1]

        if (((lines*columns) % 2) == 0):
            print("Essa matriz se torna um vetor com número par de elementos")
        else:
            print("Essa matriz se torna um vetor com número impar de elementos")

#Questão 1
questionSolution(1)

#Questão 2
questionSolution(2)

#Questão 3
questionSolution(3)

#Questão 4
questionSolution(4)

#Questão 5
questionSolution(5)