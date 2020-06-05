from string import punctuation
from collections import Counter


def preprocess(text: str) -> str:
    """
    The main data pre processing logic
    """
    text = text.lower()  # lowercase, standardize
    text = ''.join([c for c in text if c not in punctuation])  # remove punctuation
    return text


def encoding(text: str) -> tuple:
    """
    Words encoding - embedding
    :return:
    """
    vocabulary = tuple(set(text))
    int_to_vocab = dict(enumerate(vocabulary))
    vocab_to_int = {ch: ii for ii, ch in int_to_vocab.items()}

    # to optimize we could try with subsampling created by Mikolov in order to reduce noise by removing words which has
    # very high frequency and doesn't provide any semantic to the text meaning.

    return vocab_to_int, int_to_vocab
