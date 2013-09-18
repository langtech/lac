# L&C Project 2
# Firstname LASTNAME, STUDENT-ID
# Firstname LASTNAME, STUDENT-ID

r"""
Please replace this comment with approx 400 words of discussion about
what your grammar, the constructions it supports and the semantic
representations you have chosen, interspersed with examples as
follows. Use section headings to indicate which question you are
answering.

The next two examples illustrate the treatment of quantifiers.
The determiner introduces the overall logical expression, which
is filled in by semantic components from the rest of the sentence.
A consequence of this is that the semantics for "a dog" is not
\x.dog(x) but \P.exists x.(dog(x) & P(x)), which might be understood
as the set of properties that a dog has.

    >>> parse("every dog barks")
    all x.(dog(x) -> bark(x))

    >>> parse("a dog barks")
    exists x.(dog(x) & bark(x))

Question 1
----------

Next we look at transitive verbs...



Here is a case of ambiguity (note that multiple semantic
representations are produced)...

Our grammar correctly rejects the following
as ungrammatical, and so there is no output:

    >>> parse("dog barks")


"""

# Main program (it should not be necessary to change this)

from nltk import load_parser
parser = load_parser('grammar.fcfg', trace=0) # trace=1 for derivations

def parse(sentence):
    tokens = sentence.split()
    trees = parser.nbest_parse(tokens)
    for tree in trees:
        print(tree.node['SEM'])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
