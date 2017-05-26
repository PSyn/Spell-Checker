#Phil K, Kevin M
def ignoreCaseAndPunc(word):
    """
        removes capitalization and punctuation from an input word
        and outputs the adjusted word
    """
    #lowers all letters in word
    word = word.lower()
    #Removes the punctuation
    word="".join([c for c in word if c not in('!','?',',',';',':','.')])
    return word

def findWordInDictionary(word, fileName):
    """
        checks to see if a word is present in the dictionary (fileName)
        after applying the ignoreCaseandPunc function
    """
    p=open(fileName,"r").read()#opens the file
    
    word=ignoreCaseAndPunc(word)#Removes  punctuations and makes the word lowercase

    #returns true if word in dictionary and false if not
    if word in p.split():	
        return True
    else:
        return False
        

def getWordsOfSimLength(word, fileName, n):
    """
        finds words with similar length +/- (n) to word
        from the dictionary (fileName), returns list
    """
    s =open(fileName).read()#opens the file
    wordslm=[]#initializes list of words with sim length
    
    for name in s.split():#splits the file lines as per spaces
        p=0
        while p<=n:#appends words  with similar length +/- (n)
            if len(name)+p==len(word) or len(name)-p==len(word):
                wordslm.append(name)
            p+=1
    return wordslm

def getWordsWithSameStart(word, wordList, n):
    """
        Given a word and a list of specific words, returns a
        list that match the first n characters
    """
    wordst=[]

    for name in wordList:
    
        if name[:n]==word[:n]:
                wordst.append(name)#appends words with first n letters
                    
    return wordst

def getWordsWithSameEnd(word, wordList, n):
    """
        Given a word and a list of specific words, returns a
        list that match the last n characters
    """
    wordst=[]#initializes the list
    

    for name in wordList:
        
        if word=='existt':
            name[-n:],word[-n:],n,'gghhh'
       
        if name[-n:]==word[-n:]:
            wordst.append(name)#appends words with last n letters
    return wordst
    
def getWordsWithCommonLetters(word, wordList, n):
    """
        returns a list with words that have n amount or more letters in common
        ignores repeat letters
    """
    dictionary = wordList[:]
    #creates an empty list
    word_ch = []
    #takes each character from the input word and adds it to the mepty list
    for ch in word:
        word_ch.append(ch)
    #converts the list into a unique set
    word_ch = set(word_ch)
    #creates an empty list
    word_list = []
    #goes through all words in the loaded list
    for dictionary_word in dictionary:
        dictionary_word_ch = []
        ch_list = []
        #takes each word and creates a set of unique characters
        for d_word_ch in dictionary_word:
            dictionary_word_ch.append(d_word_ch)
            dictionary_word_ch_set = set(dictionary_word_ch)
        #as long as the minumum required number of common characters is not greater than the word itself
        if len(dictionary_word_ch) >= n and n != 0:
            #loops through each character in the set
            for char in dictionary_word_ch_set:
                #checks to see if each character is in the set made from the word
                if char in word_ch:
                    #adds the character to a list 
                    ch_list.append(char)
            #if the amount of characters is equal to or greater than the required amount the
            #loaded list word is added to a new list
            if len(ch_list) >= n:
                word_list.append(dictionary_word)
    return word_list
def getWordsWithCommonPercent(word, wordList, commonPercent):
        '''Picks words from the wordlist which have n% or more or commonletters to the word'''
        wordco=[]#initializes the list containing the common percent words
        for name in wordList:
           k=float(len(set(name)&set(word)))#number of common letters
            
           distinct=float(len(set(name).union(set(word))))#number of distinct letters
            
           common_percent=(k/distinct)*100#percentage of letters that are common
            
           if common_percent>=commonPercent:#appends with equal or greater than n%
                   wordco.append(name)
        return wordco          

def getSimilarityMetric(word1, word2):
    """
        Returns two measures of similarity given two words and returns an average.
        These are numbers of letters that match up going from left to right and
        right to left.
    """
    #empty lists to hold characters
    ch_word1 =[]
    ch_word2 = []
    #maps characters from each word to lists
    for ch in word1:
        ch_word1.append(ch)
    for ch2 in word2:
        ch_word2.append(ch2)
    #records lengths for each word
    count1 = len(ch_word1)
    count2 = len(ch_word2)
    #sets iteration value to 0
    iteration = 0
    score_left = 0
    #sets while loop to iterate until all the letters have been compared
    while iteration < count1 and iteration < count2:
        #as long as the letters match a score value will be increased by one
        if ch_word1[iteration] == ch_word2[iteration]:
            score_left = score_left + 1
            iteration = iteration + 1
        else:
            iteration = iteration + 1
    #reverses the lists so can be read from right to left
    rt_ch_word1 = ch_word1[-1::-1]
    rt_ch_word2 = ch_word2[-1::-1]
    iteration = 0
    score_right = 0
    #same as above except records score for right to left
    while iteration < count1 and iteration < count2:
        if rt_ch_word1[iteration] == rt_ch_word2[iteration]:
            score_right = score_right + 1
            iteration = iteration + 1
        else:
            iteration = iteration + 1
    #calculates the similarity
    similarity = ((score_left + score_right) / 2.0)
    return similarity
    

def getSimilarityDict(word, wordList):
    """
        creates a dictionary of similar words, uses getSimilarityMetric to
        create values that have keys which are in wordList
    """
    dictionary = wordList
    #creates empty dictionary
    word_dict = {}
    for dictionary_word in dictionary:
        score = getSimilarityMetric(word, dictionary_word)
        word_dict[dictionary_word]=score
    return word_dict

def sortIn2D(tup1, tup2):
    """takes two tuples and compares the second component"""
    #compares the last component of each tuple and outputs different values
    #based on the arguments
    if tup1[-1] < tup2[-1]:
        return -1
    elif tup1[-1] == tup2[-1]:
        return 0
    else:
        return 1

def getListOfFirstComponents(tupleList):
    """takes in a list of tuples and returns a list with just the first components"""
    #creates a list to store the new values
    new_list = []
    #removes the first value from each tuple in the tupleList and adds it to the new_list
    for a_tuple in tupleList:
        new_list.append(a_tuple[0])
        
    return new_list
    
def getBestWords(SimilarityDictionary, n):
    """Uses a similarity dictionary and outputs a list of the top n terms by sorting."""
    list_of_tuples = SimilarityDictionary.items()
    list_of_tuples.sort(sortIn2D, reverse=True)
    return getListOfFirstComponents(list_of_tuples)[0:n]

def getWordSuggestionsV1(word, fileName, n, commonPercent, topN):
    """
        If the input word is incorrect returns a list of suggested words
        based on a +/i n argument (length) and having at least commonPercent
        in common.  The topN (number) of suggestions are returned.
    """
    
    
    wordlist=getWordsOfSimLength(word,fileName,n)#gives a list of words with almost similar length
    
    winners=getWordsWithCommonPercent(word, wordlist,commonPercent)#words with commonletters from the list provided
    
    similarityDictionary=getSimilarityDict(word,winners)#gives the words that meets the similarity criteria
    return getBestWords(similarityDictionary, topN)#returns the tobN best words
        

def getWordSuggestionsV2(word, fileName, n, topN):
    """
        If the input is an incorrect word, provides a list of words from
        fileName, finds words +/- one in length.  Words that begin/end with the same
        n letters. Generates list and orders the list and returns the topN words.
    """
    #find words that are within +/- 1 in length with respect to the given word.
    wordlist=getWordsOfSimLength(word,fileName,1)

    
    #find words that begin with the same n letters as the given word
    
    wordstart=getWordsWithSameStart(word, wordlist, n)
    
    
    
    #find words that end with the same n letters as the given word.
    wordend=getWordsWithSameEnd(word, wordlist, n)
    
    
    #makes a list that contains the words that are in all the above lists
    winners=set(wordend).intersection(set(wordstart))
    
    #order the list based on the word similarity measure
    similarityDictionary=getSimilarityDict(word,list(winners))
    #returns a list of the topN words
    
   
    return getBestWords(similarityDictionary, topN)
    
def getCombinedWordSuggestions(word, fileName):
    """
        Combines V1 and V2 output lists, takes 7 from each function, uses
        75% as a threshold for the first
    """
    #stores the list outputed by function V1
    lst1 = getWordSuggestionsV1(word, fileName, 2, 75, 7)
    
    #stores the list outputed by function V2
    lst2 = getWordSuggestionsV2(word, fileName, 1, 7)
   
    #find words in both the above lists
    prerank_list=list(set(lst2).intersection(set(lst1)))
    
    #ranks the list according tot he getBestWords function using a newly created similarity dictionary
    ranked_list = getBestWords((getSimilarityDict(word, prerank_list)), 10)
    return ranked_list
    '''def getCombinedWordSuggestions(word, fileName):
    lst1 = getWordSuggestionsV1(word, fileName, 2, 75, 7)
    
    lst2 = getWordSuggestionsV2(word, fileName, 1, 7)
    print lst1,'lst1'
    print lst2,'lst2'
    lst=list(set(lst2).intersection(set(lst1)))
    print lst,'lst'
    similarityDictionary=getSimilarityDict(word,lst)
    print similarityDictionary,'dict'
    return getBestWords(similarityDictionary, 10)'''
    
def prettyPrint(lst):
    """
        Displays words in numbered order
    """
    iteration = 1
    #loops through the length of the list and appends words to numbers
    while iteration <= len(lst):
        for a_word in lst:
            print str(iteration)+".", a_word
            iteration = iteration + 1
            
def docu_correction(fileName):
    """
        This function is for the jabberwocky analysis only
    """
    #opens the file to be corrected
    fileName = open(fileName, "r").readlines()
    write_new_file = open("corrected_file.txt", "w")
    dictionary = "engDictionary.txt"
    #loops through each word
    for line in fileName:
        
        for word in line.split():
            #removes punctuation
            new_word = ignoreCaseAndPunc(word)
            #checks to see if the new_word exists in the dictionary
            check = findWordInDictionary(word, dictionary)
            if check == True:
                write_new_file.write(new_word + " ")
            else:
                #takes the engDictionary.txt file and loops through the words to find the best match
                word_list = getCombinedWordSuggestions(new_word, "engDictionary.txt")
                if word_list != []:
                #writes the new suggested word to the file
                    write_new_file.write(word_list[0]+" ")
                else:
                    write_new_file.write(word + " ")
        write_new_file.write("\n")
    write_new_file.close()
    

def main():
	
    filer=raw_input("Which file would you like to correct? Please include the file extension:\n")
    f=open(filer,'r')#opens the new file
    lines = f.readlines()
    fileName='engDictionary.txt'
    
    ref_file=raw_input("Current reference list is 'engDictionary.txt',type 'y' to keep it or type a name for a new reference file.\n")

    if ref_file!='y':
            fileName=ref_file
    #creates a new file to be corrected
    corr_user_file_w=open(filer[:-4]+'-chk.txt','w')
    #cycles through each line and then by word
    for line in lines:
        for word in line.split():
            word=ignoreCaseAndPunc(word)#removes punctuations and appends
            #checks if the word exists in the dictionary, and if it does, appends it to the writable file
            if findWordInDictionary(word,fileName)==False:
                #finds alternatives from the dictionary if the word is mispelled
                options=getCombinedWordSuggestions(word, fileName)
                if len(options)!=0:
                    print "The word,", word, "is not spelled correctly."
                    print "The following are available suggestions:"
                    #converts the options to a user friendly output
                    prettyPrint(options)
                    #asks the user what they want to do
                    user_option = raw_input("Press ""r"" for replace, ""a"" for accept as is, ""t"" for type in manually\n")
                    #makes sure the input makes sense
                    while user_option != "r" and user_option != "a" and user_option != "t":
                        print "You have typed an incorrect key, please try again."
                        user_option = raw_input("Press ""r"" for replace, ""a"" for accept as is, ""t"" for type in manually\n")
                    #for the r-case, makes sure that the user uses a number that is allowed and then appends that to the writable file
                    if user_option == "r":
                        user_option_2 = input("Select the number corresponding to the word you wish to replace:\n")
                        while user_option_2 > len(options):
                            print "You have typed an incorrect key, please try again"
                            user_option_2 = input("Select the number corresponding to the word you wish to replace:\n")
                        #adds the word to the file, note a space is added between each word    
                        corr_user_file_w.write(options[user_option_2-1] + " ")
                    #accepts and adds the word to the file
                    elif user_option == "a":
                        corr_user_file_w.write(word + " ")
                    #takes whatever input is given by the user and adds it to the file
                    elif user_option == "t":
                        user_manual = raw_input("Please type the word you would like to enter instead:\n")
                        corr_user_file_w.write(user_manual + " ")
                else:
                    #similar to above with "r" option removed
                    print "The word,", word, "is not spelled correctly."
                    print "There are 0 suggestions in the dictionary available."
                    user_option_3 = raw_input("Press ""a"" for accept as is, ""t"" for type in manually\n")
                    while user_option_3 != "a" and user_option_3 != "t":
                        print "You have typed an incorrect key, please try again."
                        user_option_3 = raw_input("Press ""a"" for accept as is, ""t"" for type in manually\n")
                    if user_option_3 == "a":
                        corr_user_file_w.write(word + " ")
                    elif user_option_3 == "t":
                        user_manual = raw_input("Please type the word you would like to enter instead:\n")
                        corr_user_file_w.write(user_manual + " ")		
            else:
                 corr_user_file_w.write(word + " ")
        #adds correct format to output file
        corr_user_file_w.write("\n")
    print '\n'
    print "SpellCheck complete"
    print '\n'
	
    f.close()
    corr_user_file_w.close()
    
if __name__=='__main__':
	main()
