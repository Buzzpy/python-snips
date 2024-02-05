def anagram(word1, word2):
    word1.lower() # so that this doesn't differentiate with lower and upper cases
    word2.lower()

    word1_list = list(word1)  # to split the letters— easy to sort and find len
    word2_list = list(word2)

    if len(word1_list) == len(word2_list):
        word1_list.sort()
        word2_list.sort()

        if word1_list == word2_list:
          print("True")
        else:
            print("False")
    else:
        print("False")

anagram(input(str("word 1 please")), input(str("word 2 please")))
