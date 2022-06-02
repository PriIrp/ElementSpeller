import requests

def elementSpeller(userWord):
    box = []
    start = 0
    pausePoints = []

    def symFinder(word, start, pausePoint=0):
        for i in range(pausePoint, len(atomicSymbols)):
            sym = atomicSymbols[i]
            if(word.find(sym.upper(), start, start + len(sym)) != -1):
                pausePoints.append(atomicSymbols.index(sym))
                return sym

        return -1

    while start != len(userWord):
        sym = symFinder(userWord, start)
        
        if sym == -1:
            while sym == -1:
                if(len(box) != 0):
                    popLen = len(box.pop())
                    start -= popLen
                    lastIdx = pausePoints.pop()
                    sym = symFinder(userWord, start, lastIdx+1)

                else:
                    print("Impossible!")
                    break

        if(sym != -1):
            box.append(sym)

            start += len(sym)
        
        else:
            break
    
    if(start == len(userWord)):
        print(box)

url = "https://periodic-table-elements-info.herokuapp.com/elements"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
response = response.json()

atomicSymbols = []

for element in response:
    symbol = element.get('symbol')
    atomicSymbols.append(symbol)

while True:
    userWord = input("Please enter a word: ")
    userWord = userWord.upper()
    elementSpeller(userWord)

