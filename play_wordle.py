from wordle import Wordle

def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")
#PUPSKO
    while wordle.can_attempt:
        x = input("Type your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(f"Word must be {wordle.WORD_LENGTH} letters long")
            continue
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep=" \n")
    if wordle.is_solved:
        print("DONE!")
    else:
        print("You've failed")


if __name__ == '__main__':

    main()
