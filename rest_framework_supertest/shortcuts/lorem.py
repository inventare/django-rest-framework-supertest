from ._utils import unique


def paragraph(fake, nb_sentences=3, variable_nb_sentences=True, ext_word_list=None):
    """
    Generate a paragraph.

    The nb_sentences argument controls how many sentences the paragraph
    will contain, and setting variable_nb_sentences to False will
    generate the exact amount, while setting it to True (default)
    will generate a random amount (+/-40%, minimum of 1) using
    randomize_nb_elements().

    Under the hood, sentences() is used to generate the sentences,
    so the argument ext_word_list works in the same way here as
    it would in that method.
    """
    return fake.paragraph(
        nb_sentences=nb_sentences,
        variable_nb_sentences=variable_nb_sentences,
        ext_word_list=ext_word_list,
    )

def unique_paragraph(fake, nb_sentences=3, variable_nb_sentences=True, ext_word_list=None):
    """
    Generate a unique paragraph.

    The nb_sentences argument controls how many sentences the paragraph
    will contain, and setting variable_nb_sentences to False will
    generate the exact amount, while setting it to True (default)
    will generate a random amount (+/-40%, minimum of 1) using
    randomize_nb_elements().

    Under the hood, sentences() is used to generate the sentences,
    so the argument ext_word_list works in the same way here as
    it would in that method.
    """
    return unique(
        fake,
        paragraph,
        nb_sentences=nb_sentences,
        variable_nb_sentences=variable_nb_sentences,
        ext_word_list=ext_word_list,
    )

def sentence(fake, nb_words=6, variable_nb_words=True, ext_word_list=None):
    """
    Generate a sentence.

    The nb_words argument controls how many words the sentence will contain,
    and setting variable_nb_words to False will generate the exact amount,
    while setting it to True (default) will generate a random amount
    (+/-40%, minimum of 1) using randomize_nb_elements().

    Under the hood, words() is used to generate the words,
    so the argument ext_word_list works in the same way
    here as it would in that method.
    """
    return fake.sentence(
        nb_words=nb_words,
        variable_nb_words=variable_nb_words,
        ext_word_list=ext_word_list,
    )

def unique_sentence(fake, nb_words=6, variable_nb_words=True, ext_word_list=None):
    """
    Generate a unique sentence.

    The nb_words argument controls how many words the sentence will contain,
    and setting variable_nb_words to False will generate the exact amount,
    while setting it to True (default) will generate a random amount
    (+/-40%, minimum of 1) using randomize_nb_elements().

    Under the hood, words() is used to generate the words,
    so the argument ext_word_list works in the same way
    here as it would in that method.
    """
    return unique(
        fake,
        sentence,
        nb_words=nb_words,
        variable_nb_words=variable_nb_words,
        ext_word_list=ext_word_list,
    )

def text(fake, max_nb_chars=200, ext_word_list=None):
    """
    Generate a text string.

    The max_nb_chars argument controls the approximate number of
    characters the text string will have, and depending on its value,
    this method may use either words(), sentences(), or paragraphs()
    for text generation. The ext_word_list argument works in
    exactly the same way it would in any of those methods.
    """
    return fake.text(max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)

def unique_text(fake, max_nb_chars=200, ext_word_list=None):
    """
    Generate a unique text string.

    The max_nb_chars argument controls the approximate number of
    characters the text string will have, and depending on its value,
    this method may use either words(), sentences(), or paragraphs()
    for text generation. The ext_word_list argument works in
    exactly the same way it would in any of those methods.
    """
    return unique(fake, text, max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)

def word(fake, part_of_speech=None, ext_word_list=None):
    """
    Generate a word

    This method uses words() under the hood with the nb argument set
    to 1 to generate the result.
    """
    return fake.word(part_of_speech=part_of_speech, ext_word_list=ext_word_list)

def unique_word(fake, part_of_speech=None, ext_word_list=None):
    """
    Generate a unique word

    This method uses words() under the hood with the nb argument set
    to 1 to generate the result.
    """
    return unique(fake, word, part_of_speech=part_of_speech, ext_word_list=ext_word_list)
