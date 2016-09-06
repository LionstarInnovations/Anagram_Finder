########################################
######                            ######
######   Marcus Daniel McFarlane  ######
######                            ######
######   Student ID: 200912969    ######
######                            ######
########################################




##-------------------- Question 1 --------------------##


#-- The keyword "def" is used to create a function definition containing two arguments "str1" and "str2" in the parameters. --#
def anagram(str1, str2):

    #-- "str1_list" variable is used to convert the string argument into a list and store the value. --#
    str1_list = list(str1)

    #-- "str1_list.sort()" is used to sort the list in alphabetical order. --#
    str1_list.sort()

    #-- The same is repeated for the "str2_list" variable. --#
    str2_list = list(str2)
    str2_list.sort()

    #-- Returns the arguments with the "==" comparison operator, checking if "str1_list" is equal to "str2_list" --#
    #-- which returns "True" if str1_list is equal to "str2_list" and "False" if not. --#
    return (str1_list == str2_list)

#-- "input_1" variable is used for the built-in function "input()" to get input from the user. --#
##input_1 = input("Enter a string: ")

#-- The same is repeated for "input_2". --#
##input_2 = input("Enter another string: ")

#-- The "print()" built-in function is used, calling the "anagram" function and using the two arguments from the --#
#-- variables for the user input. --#
##print("String 1 is equal to string 2: ",anagram(input_1, input_2))


##-------------------- Question 2 --------------------##


def test_anagram():
    print("Testing the anagram using three positives and three negatives")
    # first positive
    str1 = ("ah")
    str2 = ("ha")
    anagram(str1, str2)
    print("Positive 1: ", str1, "+", str2, "=", anagram(str1, str2))
    # second positive
    str1 = ("rose")
    str2 = ("sore")
    anagram(str1, str2)
    print("Positive 2: ", str1, "+", str2, "=", anagram(str1, str2))
    # third positive
    str1 = ("rule")
    str2 = ("lure")
    anagram(str1, str2)
    print("Positive 3: ", str1, "+", str2, "=", anagram(str1, str2))
    # first negative
    str1 = ("ah")
    str2 = ("hi")
    anagram(str1, str2)
    print("Negative 1: ", str1, "+", str2, "=", anagram(str1, str2))
    # second negatiive
    str1 = ("rose")
    str2 = ("roll")
    anagram(str1, str2)
    print("Negative 2: ", str1, "+", str2, "=", anagram(str1, str2))
    # third negative
    str1 = ("rule")
    str2 = ("ruled")
    anagram(str1, str2)
    print("Negative 3: ", str1, "+", str2, "=", anagram(str1, str2))
    

##-------------------- Question 3 --------------------##
    

def get_dictionary_word_list():

    #-- The file "dictionary.txt" is opened using the "open()" built-in function and the "(r)" command is used to read the file. --#
    dicList = open('dictionary.txt', 'r')

    #-- The variable "word_list" is created which contains an empty list. --#
    word_list = []

    #-- A "while loop" is used with the "True" condition, which will keep looping if the condition is always true. --# 
    while True:

        #-- The "readline()" function is used for the "dicList" variable, which reads a line from the file --#
        line = dicList.readline()

        #-- The  "if" condition is used, which contains the codition that if a line that is read equals to blank then the indented code --#
        #-- containing the "break" condition will be executed, which breaks out of the while loop --#
        if line == "":
            break

        #-- The "else" condition is used, which contains indented code that is executed if the "if" condition is false. 
        else:

            #-- The method "rstrip()" returns a copy of the string in which all chars have been stripped. --#
            line2 = line.rstrip()

            #-- The "append()" method is used which passes an object to the end of the list --#
            word_list.append(line2)

    #-- The "close()" method is used to close the file and free up any system resources taken up by the file --#
    dicList.close()
    return word_list

#-- The "print()" funcion is used which calls the fucntion "get_dictionary__word_list()", which reeads the dictionary --#
#-- and prints the "dictionary.txt" file. --#
# print(get_dictionary_word_list())


##-------------------- Question 4 --------------------##


def test_get_dictionary_word_list():

    #-- The vairiable "dic_words" is used which calls the function "get_dictionary_word_list" --#
    dic_words = get_dictionary_word_list()

    #-- The "print()" function contains the "len()" function which returns the number of items --#
    #-- of the object; "dic_words" variable, and outputs the result--#
    print("The number of words in the list: ", len(dic_words))

    #-- A "for loop" is used with "k" as the item name "in" the "range()" built-in function, which is used --#
    #-- for arithmatic progression. The "range()" fucntion starst at 0 and ends at 11. This causes the indented --#
    #-- code in the "for loop" to only be looped 10 times. --#
    print("The first 10 words are: ")
    for k in range(0,11):

        #-- The "k" item name from the "for loop" condition is then used to print items from the "dic_words" variable. --#
        print(dic_words[k])

#-- The function "test_dictionary_word_list" is called --#
##test_get_dictionary_word_list()


##-------------------- Question 5 --------------------##

        
#-- A function is defined containing two arguments in the parameters --#
def find_anagrams_in_word_list(str, str_list):

    #-- The variable "words" is used which contains a list comprehension to make the code look more compact --#
    #-- and neater, which contains an expression and a for loop. The list comprehension works using the --#
    #-- variable "words" as an empty string. Then the "w" item name for the for loop, is used to loop through --#
    #-- the items contained in the object "str_list" argument, applying the function "rstrip" --#
    #-- which strips all the default whitespace characters from the end of each string. --#
    words = [w.rstrip() for w in str_list]

    #-- The "sorted_word" variable contains the "sorted()" built-in funciton which is used for the "str" argument --#
    #-- and sorts the string in alphabetical order --#
    sorted_word = sorted(str)

    #-- The "returned" keyword contains the list comprehension, which loops through the items in the object variable --#
    #-- "words" list and uses the "if" condition. Putting the items from the list in alphabetical order and returning --#
    #-- the items from the list that are equal to the vairable "sorted_word" --# 
    return [w for w in words if sorted(w) == sorted_word]


##str = input("Enter a word: ")
##
##str_list = []
##maxLengthList = 5
##while len(str_list) < maxLengthList:
##    item = input("Enter another word in a list: ")
##    str_list.append(item)

##print(find_anagrams_in_word_list(str,str_list))


##-------------------- Question 6 --------------------##


def find_anagrams(str):

    #-- The function "get_dictionary_word_list" is called and inputted into the vairable "dic_list" --#
    dic_list = get_dictionary_word_list()

    #-- Returns the previous made function "find_anagrams_in_word_list" with two arguments, which includes --#
    #-- an argument for the string from the user input, and the argument for the variable "dic_list". --#
    #-- This returns all anagrams of the inputted string from the user input --#
    return find_anagrams_in_word_list(str, dic_list)


##str = input('Enter a word: ')
##
##print( find_anagrams( str ) )

   
##-------------------- Question 7 --------------------##


def test_find_anagrams(str_list):

    #-- Uses the "print()" function, that calls the function "find_anagrams" containing the argument --#
    #-- "str_list" for the user input, and uses the "len()" built-in function  to count the number of anagrams --#
    #-- for the user input, and print the output --#
    print(len(find_anagrams(str_list)))

    return find_anagrams(str_list)

#-- The variable "inputList" contains an empty list --#    
##inputList = []

#-- The variable "maxLengthList" contains the integer 6 --#
##maxLengthList = 6

#-- The "while loop" condition contains the "len()" function which is used to count the number of items in the "inputList" --#
#-- and the comparison operator "<" the variabel "maxLengthList" which keeps the while loop looping and executing the indented --#
#-- script until the loop has been executed 5 times. --# 
##while len(inputList) < maxLengthList:
    
    
    str_list = input("Enter a word in a list: ")

    #-- The "append()" built-in function is used to add a found anagram to the end of the list, which is repeated in the loop --#
    ##inputList.append(str_list)

    #-- The "print()" function calls the "test_find_anagrams" function which contains the argument "str_list", to print the argument --#
    #-- for the "inputList". Printing a maximum of 6 anagrams that are releavant to the user's inputted string --#
    ##print(test_find_anagrams(str_list))


##-------------------- Question 8 --------------------##


def partial_anagram(str1, str2):

    #-- A "for loop" is used which contains "s" for the item name and the argument "str1" for the object. --#
    #-- The "s" is used to loop through every letter contained in the string --#
    for s in str1:

        #-- A variable "num1" which contains the "count()" method, which counts how many letters occur in --#
        #-- the string "str1". --#
        num1 = str1.count(s)

        #-- The same is repeated for thr string "str2" --#
        num2 = str2.count(s)

        #-- The "if" condition with the comparison operator ">", stating that if every letter that occurs in --#
        #-- "str1" occurs more then in "str2" then the indented code will be executed which returns "False". --#
        if num1 > num2:
            return False

    #-- Otherwise the function returns "True", which means that "str1" occurs --#
    #-- at least as many times in "str2". --#
    return True

##str1 = input('Enter a word: ')
##str2 = input('Enter a word: ')
##
##print(partial_anagram(str1, str2))


##-------------------- Question 9 --------------------##


def find_partial_anagrams_in_word_list(str, str_list):
    
    result = []

    #-- The "if" condtion contains "x" for the item name and "str_list" for the list name to loop through --#
    for x in str_list:

        #-- The "if" condition contains the function "partial_anagram" which is being called with two arguments --#
        #-- The "x" loops through the letetrs in "str", and if any of the letters occur at least as many times --#
        #-- in words in "str_list" then the indented code will be executed which adds those words to the list "result" --#
        if partial_anagram(x, str):
            result.append(x)
    return result


##-------------------- Question 10 --------------------##
   

def test_find_partial_anagrams_in_word_list():

   #-- The variable "wordlist" contains the function call "get_dictionary_word_list". --#
   wordlist = get_dictionary_word_list()

   #-- The "print()" built-in function calls the function "find_partial_anagrams_in_word_list" with two arguments. --#
   #-- The called function loops through every letter in the first argument, then loops through the second argument --#
   #-- "word_list", and if any letters occur at least as many times in words in "word_list" then the words will be --#
   #-- appended to the list and printed --#
   print("This is the first test for 'brandon': ")
   print( find_partial_anagrams_in_word_list("brandon", wordlist, "\n") )
   print("This is the second test for 'marcus': ")
   print( find_partial_anagrams_in_word_list("marcus", wordlist, "\n") )
   print("This is the third test for 'seabird': ")
   print( find_partial_anagrams_in_word_list("seabird", wordlist, "\n") )
   print("This is the fourth test for 'earth': ")
   print( find_partial_anagrams_in_word_list("earth", wordlist) )


##-------------------- Question 11 --------------------##


def remove_letters(str1, str2):

    #-- The variable "str1" contains the "list()" function which converts the argument "str1" into a list --#
    #-- and stores it in the variable. This is used to convert the letters into a list --#
    str1 = list(str1)

    #-- The for loop contains "x" for the item name which iterates through the "range()" function, starting at 0 --#
    #-- and ending at the length of the string which is found using the "len()" function.
    for x in range(0,len(str1)):

        #-- The "replace()" function is used which loops through "str1" list and replaces any of the same letetrs that --#
        #-- occur in "str2" with an empty string. Removing the letters from "str2" and storing the new string in --#
        #-- the variable "str2". --#
        str2 = str2.replace(str1[x],"",1)

    return str2

   


##-------------------- Question 12 --------------------##
        

def test_remove_letters():
    print("This is a test for 'seabird' and 'seabirdsing': ")
    print(remove_letters('seabird','seabirdsing'))
    print("This is a test for 'mocking' and 'mockingbird': ")
    print(remove_letters('mocking','mockingbird'))
    print("This is a test for 'eagle' and 'eagle': ")
    print(remove_letters('eagle','eagle'))
    print("This is a test for ''Leeds' and 'University': ")
    print(remove_letters('Leeds','University'))


##-------------------- Question 13 --------------------##


def find_two_word_anagrams_in_word_list(str, str_list):

    #-- A variable "two_word_anagrams" which conatins an empty list --#
    two_word_anagrams = []

    #-- A variable "remainder_letters" which conatins an empty list --#
    remainder_letters = []

    #-- A variable "str_list" which calls the function "get_dictionary_word_list" --#
    str_list = get_dictionary_word_list()
    #-- A variable "part_anagrams" which calls the function "find_partial_anagrams_in_word-list" --#
    part_anagrams = find_partial_anagrams_in_word_list(str, str_list)

    #-- The function "find_partial_anagrams_in_word_list" is called to get the list of partial anagrams --#
    #-- of the string in the word list. The "for loop" then selects each object in the list one by one.
    for x in part_anagrams:

        #-- The function "remove_letters" is called which removes the letters from the string "str" --#
        #-- to get a string, which is the remaining letters after taking away the partial anagram. --#        
        remainder_letters = remove_letters(x, str)

        #-- The function "find_anagrams_in_word_list" is called on the remaining string --#
        #-- and the input word list, to get a list of anagrams of the reamining letters --#
        
        remains_anagram = find_anagrams_in_word_list(remainder_letters, str_list)

        #-- The "for loop" iterates through each remains_anagram of the reamining letters --#
        #-- and forms the string "part_anagrams + " " + remaining_anagram" and adds it to the --#
        #-- list two_word_anagrams.
        for y in remains_anagram:
            two_word_anagrams.append(x + " " + y)

    #-- The "two_word_anagrams" function is returned which contains all the two word anagrams --#
    #-- the two word anagrams in it --#
    return two_word_anagrams


##-------------------- Question 14 --------------------##


def test_find_two_word_anagrams():
    str_list = get_dictionary_word_list()

    #-- The "print()" calls the function "find_two_word_anagrams_in_word_list" for a number of strings --#
    #-- using the word list from the file "dictionary.txt". --#
    print("Testing for 'ace': ")
    print(find_two_word_anagrams_in_word_list('ace', str_list), "\n\n")
    print("Testing for 'apple': ")
    print(find_two_word_anagrams_in_word_list('apple', str_list), "\n\n")
    print("Testing for 'mountain': ")
    print(find_two_word_anagrams_in_word_list('mountain', str_list), "\n\n")
    print("Testing for 'yorkshire")
    print(find_two_word_anagrams_in_word_list('yorkshire', str_list), "\n\n")
    print("Testing for 'programmer")
    print(find_two_word_anagrams_in_word_list('programmer', str_list), "\n\n")
    print("Testing for 'communications")
    print(find_two_word_anagrams_in_word_list('communications', str_list))      


##-------------------- Question 15 --------------------##


def student_names_and_anagrams():
    import csv
    first_names = []
    last_names = []
    full_names = []
    sorted_anagrams = []
    anagram_names = []
    word_list = get_dictionary_word_list()
    counter = 0

    #-- The file is opened whcih contains --#
    with open ('students.txt') as students_file:
        csv_reader = csv.reader(students_file)

        for line in csv_reader:  

            #-- The "split()" function is used to split the lists into two elements. --#
            #-- This is done for 
            last_names_in_line = line[0].split()[1]
            first_names_in_line = line[1].split()[1]

            #-- The "append()" function is used to add the split element to the "last_names" list --#
            last_names.append(last_names_in_line)
            #-- The same is done for "first_names" list. --#
            first_names.append(first_names_in_line)

            #-- The "append()" function is used to add the enclosed variable values to a list "full_names". The --#
            #-- "lower()" fucntion is used to convert the strings into lower case. Then the "title()" --#
            #-- function is used to captalist the first letter of each individual string. --#
            full_names.append(first_names[counter] + ' ' + last_names[counter].lower().title())

            #-- The "append()" function is used to append the enclosed values to the list "anagram_names". --#
            
            anagram_names.append(full_names[counter].replace(' ','').replace(' ','').replace(' ','').lower())

            print('Full name of the student:\n', full_names[counter], '\n')
            print('First and last names of the student:\n', first_names[counter], last_names[counter], '\n')
            print('Letters in firstname and last name:\n', anagram_names[counter], '\n')

            
            one_word_anagrams = find_anagrams(anagram_names[counter])

            
            if (one_word_anagrams == []):
                print('One word anagram of firstname and surname:\n', "Doesn't exist.", '\n')
            else:
                print('One word anagram of firstname and surname:\n', one_word_anagram, '\n')

            two_word_anagrams = find_two_word_anagrams_in_word_list(anagram_names[counter], word_list)
            if (two_word_anagrams == []):
                print('Two word anagram of firstname and surname:\n', "Doesn't exist.", '\n')
            else:
                print('Two_word_anagrams of firstname and surname:\n', two_word_anagram, '\n')

            
            counter += 1
