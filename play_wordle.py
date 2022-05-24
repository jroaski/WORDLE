from wordle import Wordle
def main():
    print("Hello Wordle")
    wordle = Wordle("APPLE")
    while wordle.can_attempt:
        x = input("Type your guess:")
        wordle.attempt(x)
    if wordle.is_solved:
        print("DONE!")
    else:
        print("You've failed")

if __name__ == '__main__':

    main()