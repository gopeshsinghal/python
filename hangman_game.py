import sys 
sys.path.append('/home/gopesh/python/')
from random_word_generator import pick_random_word

def print_current_state(current_word_state,attempts_remaining):
    #printing current condition of user
    print("current State: ",end=" ")
    for i in current_word_state:
        print(i,end=" ")
    print("\nAttempts remaining: {}".format(attempts_remaining))


def change_current_word_state(selected_word,current_word_state,character):
    modified_word_state = ""
    for i in range(len(selected_word)):
        if current_word_state[i] == "_" and  selected_word[i] == character:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]
    return modified_word_state

def input_character_in_words(selected_word,input_char,current_word_state,attempts_remaining):
    
    if input_char in selected_word:
        current_word_state = change_current_word_state(selected_word,current_word_state,input_char)
    else:
        attempts_remaining -= 1
    return current_word_state, attempts_remaining

def check_game_status(selected_word, current_word_state, attempts_remaining):
    #if game has ended or not
    if current_word_state == selected_word:
        print("you won :D")
        return True
    elif attempts_remaining <= 0:
       print("you lose :( Please! try again")
       print("Corret word is {}".format(selected_word))
       return True
    return False


def play_game(attempt = 5):
    #It will contain main logic of my game
    
    #It will store the value of randomly selected words
    selected_word = pick_random_word()
    
    #generate current state of word
    #current_word_state = "_"*len(selected_word)
    current_word_state = ""
    for i in selected_word:
        if i == " " or i == "a"or i == "e"or i == "i"or i == "o"or i == "u":
            current_word_state += i
        else:
            current_word_state += "_"
        
    #attempts that are allowed
    attempts_remaining = attempt
    
    print_current_state(current_word_state,attempts_remaining)
    
    while True:
        input_char = input("Enter character: ")
        print("")
        
        #check whether character is in word or not
        current_word_state,attempts_remaining = input_character_in_words(selected_word,input_char,current_word_state,attempts_remaining)
        
        print_current_state(current_word_state,attempts_remaining)
        
        game_ended = check_game_status(selected_word, current_word_state,attempts_remaining)
        
        if game_ended:
            break
if __name__ == "__main__":
    play_game()