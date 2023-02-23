#make the hangman game

import random 
import os
import sys
import time

def main():
    #create a list of words
    word_list = ['python', 'java', 'kotlin', 'javascript']
    #pick a random word
    word = random.choice(word_list)
    #create a list of letters in the word
    word_list = []
    for i in range(len(word)):
        word_list.append(word[i])
    #create a list of letters guessed
    letter_list = []
    