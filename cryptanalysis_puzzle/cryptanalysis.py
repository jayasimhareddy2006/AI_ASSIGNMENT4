import itertools

letters = ('T','W','O','F','U','R')
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):

    assign = dict(zip(letters, perm))

    if assign['T'] == 0 oign['F'] == 0:
        continue

    TWO = (
        assign['T']*100 +
        assign['W']*10 +
        assign['O']
    )

    FOUR = (
        assign['F']*1000 +
        assign['O']*100 +
        assign['U']*10 +
        assign['R']
    )

    if TWO + TWO == FOUR:
        print("\nSolution Found:\n")
        print(assign)
        print("\nVerification:")
        print(TWO, "+", TWO, "=", FOUR)
        break
