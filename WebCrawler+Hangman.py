from bs4 import BeautifulSoup
import requests
from collections import Counter
import random                              # Random module helps in randomly choosing a word/url from the commonwordslist/urllist.

listofwords = []
goodwordlist = []
commonwordslist = []
def dictionary(goodlist):          # It creates a dictionary containing each word's count
    wordcount = {}
    for word in goodlist:
        if word in wordcount:
            wordcount[word] = wordcount[word] + 1
        else:
            wordcount[word] = 1
    count = Counter(wordcount)
    commonwords = count.most_common(25)      # Counts the top 25 most common words
    for key,val in commonwords:
        commonwordslist.append(key)

def goodwordslist(listofwords):      # It removes any unwanted symbols
    for word in listofwords:
        symbols = ' +_()*&^%$#@!-=[{]}|\:;<>,.?/" '
        for a in range(len(symbols)):
            word = word.replace(symbols[a], '')
        if len(word) > 0:
            goodwordlist.append(word)
    dictionary(goodwordlist)

def start(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')     # This soup object navigates through the requested url for data
    for everytxt in soup.findAll('div', {'class':'entry-content'}):
        c = everytxt.text
        words = c.lower().split()   # Breaks the sentence into words and convert them into lowercase
        for everyword in words:
            listofwords.append(everyword)
        goodwordslist(listofwords)
urllist = ["https://www.geeksforgeeks.org/i-cant-use-logic-in-programming-what-should-i-do/?ref=lbp", "https://www.geeksforgeeks.org/which-programming-language-should-i-choose-as-a-beginner/?ref=lbp", "https://www.geeksforgeeks.org/how-to-approach-a-coding-problem/?ref=lbp"]
url = random.choice(urllist)

if __name__ == '__main__':
    start(url) 


def anyrandomword():
    word = random.choice(commonwordslist)
    word = word.lower()
    return word

name = input("What is your name? ")
print("Hey " + name, "Let's play Hangman!")

def hangman(wordtoguess):                        # It prints blank space and asks user to guess the letters of a word and appends the blank space if the guessed letter is correct.
    blanks = "_" * len(wordtoguess)
    guessed = False
    guesses = []
    print(blanks, "It is a " + str(len(wordtoguess)), "letter word")
    print("\n")
    chances = 6
    while not guessed and chances > 0:
        guess = input("Guess a letter: ")
        if len(guess) == 1:
            if guess in guesses:
                print("You have already guessed the letter", guess)
            elif guess not in wordtoguess:
                print('Wrong Guess! Please Try Again.')
                chances = chances - 1
                guesses.append(guess)
            else:
                guesses.append(guess)
                newblankslist = list(blanks)
                lst = [x for x, letter in enumerate(wordtoguess) if letter == guess]
                for index in lst:
                    newblankslist[index] = guess
                blanks = "".join(newblankslist)
                print("Great guess!")
                if "_" not in blanks:
                    guessed = True
        else:
            print("Invalid Input!!!")
        print(blanks)
        print("\n")
    if guessed:
        print("You Win. Congrats!!!")
    else:
        print("You Lose. Better Luck Next Time.")
        print("The word is:", wordtoguess)
wordtoguess = anyrandomword() 
hangman(wordtoguess) 