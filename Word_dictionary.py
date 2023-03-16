#have a python dictionary that has a key/value pair and that represents a word and its defination
#collect input from user and it must be a word
#check if the word is in the dictionary
#print the value for the word 
def main():
    word_dictionary={"hi":"A way of greeting",
    "eyes":"An organ for seeing",
    "earth":"A planet in space orbiting the sun"}#you can add as many words as you want
    while True:
        word=input("enter your word : ")
        if word not in word_dictionary:
            print("This word is not in the dictionary")
        if word.lower() in word_dictionary:
            print("\n{} = {}".format(word,word_dictionary[word]))
        exit=input("\n Enter (0) to exit or press (1) to continue : ")
        if int(exit) == 0:
            break
        else:
            continue
main()
        
