import functools

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

words = "These are indeed interesting, an obvious understatement, times. What say you?"


def convert_to_word_list(text):
    """
    the sentence is split at the special characters
    stored in a list
    """
    text_list = split(",?:;. ", text.lower())
    new_text_list = list(filter(None,text_list))
    return new_text_list


def words_longer_than(length, text):
    """
    it iterates through the list checking the legnth of each word
    the words with that legnth or more is returned
    """
    text_list = convert_to_word_list(words)
    new_text_list = list(filter(lambda words: len(words) > length, text_list))
    return new_text_list

def words_lengths_map(text):
    """
    it returns a dictionary that maps a word length
    """
    new_list = [len(x) for x in convert_to_word_list(text)]
    my_dict = {k:new_list.count(k) for k in sorted(new_list)}
    return my_dict


def letters_count_map(text):
    """
    checks how many times a letter repeats throughout the statement
    returns it in dictionary form, letters from a to z
    """
    text = convert_to_word_list(text)
    text = ''.join(text)
    new_list = [x for x in text]
    alpha = [letter for letter in list(map(chr,range(97,123)))]
    my_dict = {k:new_list.count(k) for k in sorted(alpha)}
    return my_dict


def most_used_character(text):
    """
    checks which letter repeats the most
    """
    count = letters_count_map(text)
    numbers = max(count, key = count.get)
    if not text:
        return None
    else:
        return(numbers)
        
