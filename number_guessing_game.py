import random

def main():

    number_to_guess = random.randint(1, 100)
    print(number_to_guess)
    difficulty_level = 0
    difficulty_selected = False

    print("\nWelcome to the Number Guessing Game!\n" \
    "I'm thinking of a number between 1 and 100.")

    selecting_difficulty()

    def selecting_difficulty():
        try:
            print("\nPlease select the difficulty level:" \
            "\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
        
            while difficulty_selected == False:
                difficulty_level = int(input("\nEnter your choice: "))

                if difficulty_level == 1:
                    print("\nGreat! You have selected the Easy difficulty level.")
                elif difficulty_level == 2:                
                    print("\nGreat! You have selected the Medium difficulty level.")
                elif difficulty_level == 3:              
                    print("\nGreat! You have selected the Hard difficulty level.")
                    print(difficulty_level)
                elif difficulty_level > 3:
                    print("There's no option beyond 3...")
                elif difficulty_level < 1:
                    print("There's no option below 1...")

        except ValueError:
            print("ValueError")

        if difficulty_level > 0:
            difficulty_selected = True
            return(difficulty_level)

main()