def helper(letter, index, word):
    res = (word[index] >= letter and word[index] == word[index+1] and word[index+2] >= word[index+1] and word[index+2] == word[index+3])
    return res

def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    for i in range(0, len(word)):
        if(len(word)-i >= 6 and word[i] == word[i+1] and helper(word[i],i+2,word)):
            return True
            
    return False

#trifeca('zaaabbcckl')

if __name__ == '__main__':
    # Question 1
    word = 'zaaabbcckl'
    return_value = trifeca(word)

    print(f"Question 1 solution: {return_value}")
