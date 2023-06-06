p = 191
q = 167
n = p * q
s = 599

input = input("Wie groß soll die Zufallszahl sein?")


def prn(input):
    result: str = ""
    x = pow(s, 2, n)
    for _ in range(int (input)): 
        x = pow(x, 2, n)
        result += str(x % 2)
    return result

def runTest(input):
    count = 1
    arr = list(input)
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
    return "Erwartet:" + str ((len(arr)+1)/2) + " Actual:" + str(count)


print(prn(input))
print(runTest(prn(input)))