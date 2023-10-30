from typing import Optional, Sequence

from ._utils import unique


def paragraph(
    fake: object,
    *,
    nb_sentences: int = 3,
    variable_nb_sentences: bool = True,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a paragraph.

    Under the hood, sentences() is used to generate the sentences,
    so the argument ext_word_list works in the same way here as
    it would in that method.

    Args:
        fake: The `Faker` instance.
        nb_sentences: controls how many sentences the paragraph will contain.
        variable_nb_sentences: if is False, this function will generate the
          exact amount of sentences from the `nb_sentences` argument. While setting
          it to True (default) will generate a random amount (+/-40%, minimum of 1)
          using randomize_nb_elements().
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return fake.paragraph(
        nb_sentences=nb_sentences,
        variable_nb_sentences=variable_nb_sentences,
        ext_word_list=ext_word_list,
    )

def unique_paragraph(
    fake: object,
    *,
    nb_sentences: int = 3,
    variable_nb_sentences: bool = True,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a unique paragraph.

    Under the hood, sentences() is used to generate the sentences,
    so the argument ext_word_list works in the same way here as
    it would in that method.

    Args:
        fake: The `Faker` instance.
        nb_sentences: controls how many sentences the paragraph will contain.
        variable_nb_sentences: if is False, this function will generate the
          exact amount of sentences from the `nb_sentences` argument. While setting
          it to True (default) will generate a random amount (+/-40%, minimum of 1)
          using randomize_nb_elements().
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return unique(
        fake,
        paragraph,
        nb_sentences=nb_sentences,
        variable_nb_sentences=variable_nb_sentences,
        ext_word_list=ext_word_list,
    )

def sentence(
    fake: object,
    *,
    nb_words: int = 6,
    variable_nb_words: bool = True,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a sentence.

    Args:
        fake: The `Faker` instance.
        nb_words: controls how many words the sentence will contain.
        variable_nb_words: if is set to False, the function will generate
          the exact amount of `nb_words`. While setting it to True (default)
          will generate a random amount (+/-40%, minimum of 1) using
          randomize_nb_elements().
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return fake.sentence(
        nb_words=nb_words,
        variable_nb_words=variable_nb_words,
        ext_word_list=ext_word_list,
    )

def unique_sentence(
    fake: object,
    *,
    nb_words: int = 6,
    variable_nb_words: bool = True,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a unique sentence.

    Args:
        fake: The `Faker` instance.
        nb_words: controls how many words the sentence will contain.
        variable_nb_words: if is set to False, the function will generate
          the exact amount of `nb_words`. While setting it to True (default)
          will generate a random amount (+/-40%, minimum of 1) using
          randomize_nb_elements().
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return unique(
        fake,
        sentence,
        nb_words=nb_words,
        variable_nb_words=variable_nb_words,
        ext_word_list=ext_word_list,
    )

def text(
    fake: object,
    max_nb_chars: int = 200,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a text string.

    Args:
        fake: The `Faker` instance.
        max_nb_chars: controls the approximate number of characters the
          text string will have, and depending on its value, this method
          may use either words(), sentences(), or paragraphs() for text
          generation.
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return fake.text(max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)

def unique_text(
    fake: object,
    max_nb_chars: int = 200,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a unique text string.

    Args:
        fake: The `Faker` instance.
        max_nb_chars: controls the approximate number of characters the
          text string will have, and depending on its value, this method
          may use either words(), sentences(), or paragraphs() for text
          generation.
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return unique(fake, text, max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)

def word(
    fake: object,
    part_of_speech: Optional[str] = None,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a word.

    Args:
        fake: The `Faker` instance.
        part_of_speech: is a parameter that defines to what part of speech
          the returned word belongs. If `ext_word_list` is not `None`, then
          `part_of_speech` is ignored. If the value of `part_of_speech` does
          not correspond to an existent part of speech according to the set locale,
          then an exception is raised.
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return fake.word(part_of_speech=part_of_speech, ext_word_list=ext_word_list)

def unique_word(
    fake: object,
    part_of_speech: Optional[str] = None,
    ext_word_list: Optional[Sequence[str]] = None,
) -> str:
    """
    Generate a unique word.

    Args:
        fake: The `Faker` instance.
        part_of_speech: is a parameter that defines to what part of speech
          the returned word belongs. If `ext_word_list` is not `None`, then
          `part_of_speech` is ignored. If the value of `part_of_speech` does
          not correspond to an existent part of speech according to the set locale,
          then an exception is raised.
        ext_word_list: if ``ext_word_list`` is provided, words from that list will be
          used instead of those from the locale provider's built-in word list.
    """
    return unique(
        fake,
        word,
        part_of_speech=part_of_speech,
        ext_word_list=ext_word_list,
    )
