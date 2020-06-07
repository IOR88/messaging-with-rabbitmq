"""
Providing utilities in regards to know papers/concepts which allow to select better hyperparameters depending on the
dataset.
"""


def find_embedding_dimension(text: str):
    """
    After reading the paper https://www.aclweb.org/anthology/I17-2006.pdf I will implement technique
    presented there to find out the lower bound of embedding dimension which will not break equality constraint
    which exist in dataset.

    "Depending  on  the  corpus,  its  vocabulary,  and the  context  through  which  the  differences  are
    elicited  during  training  of  word  embedding,  we are  bound  to  obtain  a  certain  number  of  words,
    say n, that are pairwise equidistant.  Such words impose an equality constraint that the embedding algorithm
    has to uphold." Citat from https://www.aclweb.org/anthology/I17-2006.pdf.

    Additional materials:

    https://en.wikipedia.org/wiki/Clique_(graph_theory)
    https://en.wikipedia.org/wiki/Cosine_similarity
    http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/
    https://arxiv.org/pdf/1507.05523.pdf

    :param text:
    :return:
    """
