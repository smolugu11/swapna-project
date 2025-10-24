import random
class GuessNumbers():
    def main():

        num = random.randint(1,100)# generating a random number between 1 and 100
        print("Please enter the number of attempts you want to guess the number:")

        while True:
            guess = int(input("enter the number the number :"))

            if guess < num:
                print("Your guess is too low")
            elif guess > num:
                print("Your guess is too high")
            else:
                print("Congratulations! You guessed the number correctly.")
                break

    main()