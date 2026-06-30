from datetime import datetime
start_time = datetime.now()
end_time = datetime.now()
def display_rule():
    print("---------WELCOME TO WORDLE (powered by mahesh )------------")
    print("\n")
    print("Game Rules: ")
    print(" A random 5-letter English word has been selected.\n You have 6 attempts to guess the hidden word.\n Every guess must: Contain exactly 5 letters , Be a valid English word.\n Invalid words do NOT count as an attempt.\n After each valid guess, you will receive feedback:\n ✓ Letter is correct and in the correct position\n *Letter exists in the word but is the wrong position\n . Letter does not exist in the word\n 6. Guess the word within 6 attempts to win!")
    print("\n")
display_rule()

def load_words():
    import random 
    try:
        with open("words.txt","r") as file:
            words = file.read().split()
        suffled_words = random.choice(words)
        return suffled_words
    except FileNotFoundError:
        print("File not found")

def playgame(suffled_words,choice):
        result=""
     
        for i in range(0,5):
                if choice[i]==suffled_words[i]:
                    result+="✓"
                elif choice[i] in suffled_words:
                    result+="*"
                else:
                    result+="."
        print(result)
        
    
            
     



def choose_words(suffled_words):
    attempts = 0
    
    while attempts<6:
        

        is_true = False
        choice = input("Enter 5-character words:- ").strip().upper()
       
        try:
            if not choice:
                print("empty input is not valid")
                is_true = True
                
                 
            elif len(choice)!= 5:
                print("Please enter 5-character words only")
                is_true = True
                
                
            elif not choice.isalpha():
                print("Please Enter words between (A-Z)")
                is_true = True
                
            
            elif len(choice)==5 :
                attempts=attempts+1
                
                playgame(suffled_words,choice)
                
                
        except ValueError:
            print("Internal server problem")
            
        if choice.upper() == suffled_words:
            print("Woah!! You Made a Right guess buddy :)")
            print(f" You have Done in Attempts:{attempts}")
            print(f" You started the game in {start_time} and completed in {end_time}. ")
            print(f"Computer words: {suffled_words}")
            break
        
        elif not is_true:
            if attempts == 6 :
                print(f"Better luck next time,you failed to guess :( Attemps Done = {attempts} )")
                print(f"Computer words: {suffled_words}")
            else :
                print(f"Attemps Done = {attempts}")
            
                     
suffled_words = load_words()
choose_words(suffled_words) 
while True: 
    user_choice = input("Do you want to play again? (yes/no): ").lower().strip()
    try:
        if not user_choice:
            print("Choice cannot be empty")
        elif not user_choice.isalpha():
            print("Only valid options are 'yes' or 'no'.")
        elif user_choice == "yes":
            suffled_words = load_words()
            choose_words(suffled_words)
        elif user_choice == "no":
            print("Quitting the game!!")
            break
    except KeyboardInterrupt:
        print("\nPlease type 'no' to exit.")
            