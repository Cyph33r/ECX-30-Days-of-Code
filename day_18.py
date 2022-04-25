from re import compile


def reverse(sentence):
    assert isinstance(sentence,
                      str), f'Expected one parameter of class int, you pass in a {sentence.__class__}'  # sanitise input
    pattern = compile(r"([A-Za-z]+[-'.]?\w+)")
    words = pattern.findall(sentence)  # get all the words in the sentence
    index_correction = 0  # index correction for every word that is replaced
    for match in pattern.finditer(sentence):
        to_insert = words.pop()  # take a word from the word list
        to_insert_length = len(to_insert)  # get its length
        match_length = match.end() - match.start()  # get the length of the word in sentence
        sentence = sentence[:match.start() + index_correction] + to_insert + sentence[
                                                                             match.end() + index_correction:]  #
        # replace word
        index_correction += to_insert_length - match_length  # correct the index i.e. increase if word added is longer than what was there and vice versa
    return sentence


if __name__ == '__main__':
    print(reverse("What time is it? Hammer time."))
