

def printSubsets(array, i, output, k):

    if (i == len(array)):
        print((''.join(output[0:k])))
        return


    printSubsets(array, i+1, output, k)
    output.insert(k, array[i])

    printSubsets(array, i+1, output, k+1)


def printSubsetsMain(inp):
    out = []
    return printSubsets(inp, 0, out, 0)


printSubsetsMain("ABCD")
