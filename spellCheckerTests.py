#Phil K, Kevin M
import unittest
from spellChecker import *

class test_spellChecker(unittest.TestCase):
    def setUp(self):
        self.test_file = open("test_checker.txt", "r")
        self.test_dictionary = open("test_dictionary.txt", "r")
        self.test_dictionary_2 = open("test_dictionary_2.txt", "r")

    
    def test_ignoreCaseAndPunc(self):
        #tests capitalization
        self.assertEqual("help", ignoreCaseAndPunc("Help"))
        #tests another form of capitalization
        self.assertEqual("help", ignoreCaseAndPunc("HelP"))
        #tests the removal of a comma
        self.assertEqual("help", ignoreCaseAndPunc("Help,"))
        #tests the removal of a comma and semicolon
        self.assertEqual("help", ignoreCaseAndPunc("Help,;"))
        #tests the remove of additonal punctuation and punctuation location
        self.assertEqual("help", ignoreCaseAndPunc(":Help,;"))
        #tests the removal of additional punctuation and an alternative punctuation location
        self.assertEqual("help", ignoreCaseAndPunc(":He!lp,;"))
        #tests the removal of additional punctuation
        self.assertEqual("help", ignoreCaseAndPunc(":He!lp,;."))
        #tests the removal of additional punctuation
        self.assertEqual("help", ignoreCaseAndPunc(":?He!lp,;."))
        #tests the removal of repeat punctuation and a full mixture of errors
        self.assertEqual("help", ignoreCaseAndPunc(":?He!,lp,;;."))
    
    def test_findWordInDictionary(self):
        #checks to make sure a known word is recorded as in the dictionary
        self.assertTrue(findWordInDictionary("you","test_dictionary.txt"))
        #checks an additional word and capitalization and open/close status
        self.assertTrue(findWordInDictionary("Animals", "test_dictionary.txt"))
        #checks to make sure punctuation has been removed
        self.assertTrue(findWordInDictionary("animals,!", "test_dictionary.txt"))
        #checks to make sure that correct values are returned when something isn't in the dictionary
        self.assertFalse(findWordInDictionary("rabid", "test_dictionary.txt"))
        #checks to make sure that the return value is accurate
        self.assertFalse(findWordInDictionary("table", "test_dictionary.txt"))

    def test_getWordsOfSimLength(self):
        #checks to make sure that the list produced is accurate
        self.assertEqual(["you", "think", "exist", "are", "they", "merry"], getWordsOfSimLength("done", "test_dictionary.txt", 1))
        #checks a word that has equal length to a word in the dictionary 
        self.assertEqual(["think", "animals", "exist", "they", "merry", "affliction"], getWordsOfSimLength("Affable", "test_dictionary.txt", 3))
        #checks another extreme at the low end
        self.assertEqual(["do", "or", "a",], getWordsOfSimLength("I", "test_dictionary.txt", 1))
        #checks a wide range tomake sure all words are included
        self.assertEqual(["animals", "affliction"], getWordsOfSimLength("Happiness", "test_dictionary.txt", 3))
        #checks another word
        self.assertEqual(["think", "animals", "exist", "they", "merry", "affliction"], getWordsOfSimLength("Affable", "test_dictionary.txt", 3))
        #checks to make sure that an empty list is returned when a word that has no matches is entered
        self.assertEqual([], getWordsOfSimLength("AppleBanananaCantelope", "test_dictionary.txt", 1))
        #checks an extreme range
        #self.assertEqual(["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], getWordsOfSimLength("Happiness", "test_dictionary.txt", 15))

    def test_getWordsWithSameStart(self):
        #matches first 2 characters
        self.assertEqual(["Think", "They"], getWordsWithSameStart("Thanks!", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 2))
        #matches first character
        self.assertEqual(["Animals", "Are", "A", "Affliction"], getWordsWithSameStart("Apples", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 1))
        #makes sure that an empty list is returned if nothing matches
        #this also tests to make sure that the last character matching doesn't indicate a match
        self.assertEqual([], getWordsWithSameStart("Apples", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 4))
    def test_getWordsWithSameEnd(self):
    
        self.assertEqual(getWordsWithSameEnd('annimals',['animals','cannibas'],3),['animals'])
        #test for output if now words match
        self.assertEqual(getWordsWithSameEnd('ann',['pick','tick'],2),[])
        #If outputs excceed number of common letters
        self.assertEqual(getWordsWithSameEnd('aa',['aa','pick','fear'],3),['aa'])
        #test for words which end differently
        self.assertEqual(getWordsWithSameEnd('existt',['exist','a','animals'],1),['exist'])
        #Test for words that do not meet the End criteria
        self.assertEqual(getWordsWithSameEnd('existt',['pessimist','a','animals'],5),[])
    def test_getWordsWithCommonLetters(self):
        #test case for 3 common letters
        self.assertEqual(["Think", "They"], getWordsWithCommonLetters("Thane!", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 3))
        #test case for 2 common letters
        self.assertEqual(["Animals", "Affliction"], getWordsWithCommonLetters("An", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 2))
        #test case for 0 common letters
        self.assertEqual([], getWordsWithCommonLetters("An", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 0))
        #test case for asking for too many common letters
        self.assertEqual([], getWordsWithCommonLetters("An", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 20))
    def test_getWordsWithCommonPercent(self):
        #Test for commonpercent at 70%
        self.assertEqual(getWordsWithCommonPercent('Thane', ['Think','Than','Thought','Bye'], 70),['Than'])
        #Test for commonpercent at 50%
        self.assertEqual(getWordsWithCommonPercent('Thane', ['Thank','Than','Thought','Bye'], 50),['Thank','Than'])
        #Test for commonpercent with zero putputs
        self.assertEqual(getWordsWithCommonPercent('Thane', ['Them','Thanks','Thought','Bye'], 80),[])
    def test_getSimilarityMetric(self):
        #general test case
        self.assertEqual(2, getSimilarityMetric("Apple", "Append"))
        #defines the case where nothing matches
        self.assertEqual(0, getSimilarityMetric("xyz", "abc"))
        #defines case where everything mtches
        self.assertEqual(5, getSimilarityMetric("Apple", "Apple"))
        #general test case #2
        self.assertEqual(2, getSimilarityMetric("Joy", "Boy"))

    def test_getSimilarityDict(self):
        #tests a word with few similarities to the list
        self.assertEqual({"Do" : 0, "You" : 0, "Think" : 0, "Animals" : 1.0,
                          "Exist" : 0, "Or" : 0, "Are" : 1.0, "They" : 0, "A" : 0.5, "Merry" : 0,
                          "Affliction" : 1.0},getSimilarityDict("Apple", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]))
        #tests a word with zero similarities to the list
        self.assertEqual({"Do" : 0, "You" : 0, "Think" : 0, "Animals" : 0,
                          "Exist" : 0, "Or" : 0, "Are" : 0, "They" : 0, "A" : 0, "Merry" : 0,
                          "Affliction" : 0},getSimilarityDict("X", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]))
        #tests a word that is the same as one word in the dictionary
        self.assertEqual({"Do" : 2.0, "You" : 0.5, "Think" : 0, "Animals" : 0,
                          "Exist" : 0, "Or" : 0, "Are" : 0, "They" : 0, "A" : 0, "Merry" : 0,
                          "Affliction" : 0},getSimilarityDict("Do", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]))
        
    def test_sortIn2D(self):
        #the following test cases check all the expected returns from this function
        self.assertEqual(1, sortIn2D(("A", 5), ("B", 3)))
        self.assertEqual(-1, sortIn2D(("A", 2), ("B", 7)))
        self.assertEqual(0, sortIn2D(("A", 4), ("B", 4)))

    def test_getListOfFirstComponents(self):
        #test case for standard tuple list input
        tupleList = [("A", 0), ("B", 3), ("C", 0)]
        self.assertEqual(["A", "B", "C"], getListOfFirstComponents(tupleList))
        #test case for repeated first values
        self.assertEqual(["A", "A", "C"], getListOfFirstComponents([("A", 0), ("A", 3), ("C", 0)]))
        #test case for mixed string
        self.assertEqual(["A", "alpha", "C"], getListOfFirstComponents([("A", 0), ("alpha", 3), ("C", 0)]))

    def test_getBestWords(self):
        #tests output of the first top word
        self.assertEqual(["do"], getBestWords((getSimilarityDict("Do", ["do", "you", "think", "animals", "exist", "or", "sre", "they", "a", "merry", "affliction"])), 1))
        #test output of the two top words
        self.assertEqual(["do", "you"], getBestWords((getSimilarityDict("Do", ["do", "you", "think", "animals", "exist", "er", "are", "they", "a", "merry", "affliction"])), 2))  
     
    def test_getWordSuggestionsV1(self):
        #tests a known result with topN = two values
        self.assertEqual(["merry", "are"], getWordSuggestionsV1("mmerry", "test_dictionary.txt", 5, 30, 2))
        #tests to constrain the result to a lesser top value
        self.assertEqual(["merry"], getWordSuggestionsV1("mmerry", "test_dictionary.txt", 5, 30, 1))
        #tests a range outside of the total # of words available
        self.assertEqual(["a","are"], getWordSuggestionsV1("a", "test_dictionary.txt", 5, 30, 3))
        #tests an extreme range
        self.assertEqual(["exist"], getWordSuggestionsV1("existt", "test_dictionary.txt", 5, 30, 9))
        #tests a 0 constraint
        self.assertEqual([], getWordSuggestionsV1("Affable", "test_dictionary.txt", 5, 30, 0))
        #test case for multiple output
        self.assertEqual(["Appelfrate", "Aperlprite"], getWordSuggestionsV1("Appleplate", "test_dictionary_2.txt",5, 30, 2))
        self.assertEqual(["exist"], getWordSuggestionsV1("existt", "test_dictionary.txt", 2,75, 7))
        self.assertEqual(["they"], getWordSuggestionsV1("thy", "test_dictionary.txt", 2,75, 7))
    def test_getWordSuggestionsV2(self):
        #tests for known word that matches
        self.assertEqual(["animals"], getWordSuggestionsV2("animls", "test_dictionary.txt", 2, 1))
        #tests for known word that matches
        self.assertEqual(["exist"], getWordSuggestionsV2("exist", "test_dictionary.txt", 1, 2))
        self.assertEqual(["they"], getWordSuggestionsV2("they", "test_dictionary.txt", 1, 2))
        #test case for a 0 returned words
        self.assertEqual([], getWordSuggestionsV2("Animals", "test_dictionary.txt", 2, 0))
        #test case for more topN words than exist
        self.assertEqual(["animals"], getWordSuggestionsV2("animals", "test_dictionary.txt", 2, 3))
        #similar to first test, single letter
        self.assertEqual(["a"], getWordSuggestionsV2("a", "test_dictionary.txt", 1, 2))
        #test case for multiple output
        self.assertEqual(["Appelfrate", "Aperlprite"], getWordSuggestionsV2("Appleplate", "test_dictionary_2.txt", 2, 2))
        #test case for increased match, n requirement
        self.assertEqual(["Appelfrate"], getWordSuggestionsV2("Appleplate", "test_dictionary_2.txt", 3, 2))

    def test_getCombinedWordSuggestions(self):
        #checks for expected outcome
        self.assertEqual(["Appelfrate"], getCombinedWordSuggestions("Appleplate", "test_dictionary_2.txt"))
        #checks for non-existant case
        self.assertEqual([], getCombinedWordSuggestions("Apple", "test_dictionary_2.txt"))
        #checks for alternate casev
        self.assertEqual(["Animals"], getCombinedWordSuggestions("Animls", "test_dictionary_2.txt"))
unittest.main()
