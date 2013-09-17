"""
This module is used to test a grammar using a set of sentences.
Run "python gde.py -h" to see the usage instructions.

The default name for the grammar file is english.fcfg.

The default name for the test sentence file is sentences.txt.
Here's a sample file.  We use an initial asterisk to mark
ungrammatical sentences.  Empty lines, and lines beginning with #,
are ignored.

----
# test sentences
Kim walks
*Kim walk
----

Unless the verbose flag is set, the program reports only
the mismatches, i.e. sentences that were incorrectly
accepted or rejected.  Empty output means there were
no errors.
"""

from __future__ import print_function

from nltk import FeatureChartParser
from nltk.data import load

# check if the parser accepts the input sentence
# (if it does, it will build one or more parse trees)
def check_line(parser, line):
    if line[0] == '*':
        line = line[1:]
    tokens = line.split()
    return len(parser.nbest_parse(tokens, 1)) > 0

# create a parser from the grammar file
def load_parser(grammar_file, verbose=False):
    grammar = load('file:' + grammar_file, cache=False)
    if verbose:
        trace = 1
    else:
        trace = 0
    parser = FeatureChartParser(grammar, trace=trace)
    return parser

# Test each sentence in the file against the grammar
# and report any mismatches (i.e. sentences that were
# incorrectly accepted or rejected).
def check_file(sentence_file, grammar_file, verbose=False):
    sentences = open(sentence_file).readlines()
    parser = load_parser(grammar_file, verbose)
    correctly_accepted = 0
    correctly_rejected = 0
    falsely_accepted = 0
    falsely_rejected = 0
    for line in sentences:
        if len(line) > 0 and line[0] != '#':
            expected = (line[0] != '*')
            accepted = check_line(parser, line)
            if expected and accepted:
                correctly_accepted += 1
                if verbose:
                    print("Correctly accepted:", line, end=' ')
            elif not expected and not accepted:
                correctly_rejected += 1
                if verbose:
                    print("Correctly rejected:", line, end=' ')
            elif expected and not accepted:
                falsely_rejected += 1
                print("Incorrectly rejected:", line, end=' ')
            elif not expected and accepted:
                falsely_accepted += 1
                print("Incorrectly accepted:", line, end=' ')
            if verbose:
                print()
               
    print("\nSUMMARY:")
    print("correctly accepted: %d;\tincorrectly accepted: %d" % (
           correctly_accepted, falsely_accepted))
    print("correctly rejected: %d;\tincorrectly rejected: %d" % (
           correctly_rejected, falsely_rejected))
    print("total accepted: %d;\ttotal rejected: %d" % (
           correctly_accepted + falsely_accepted, correctly_rejected + falsely_rejected))
    print("total correct: %d;\ttotal incorrect: %d" % (
           correctly_accepted + correctly_rejected, falsely_accepted + falsely_rejected))
    print("Correctly accepted or rejected %d out of %d (%0.1f%%)" % (
           correctly_accepted + correctly_rejected, len(sentences),
           100 * float(correctly_accepted + correctly_rejected) / len(sentences)))
   
if __name__ == '__main__':
    from optparse import OptionParser
    op = OptionParser()

    op.add_option("-s", "--sentences", dest="sentences",
                  help="load test sentences from file SENTS", metavar="SENTS",
                  default="sentences.txt")
    op.add_option("-g", "--grammar", dest="grammar",
                  help="load grammar from file GRAMMAR", metavar="GRAMMAR",
                  default="english.fcfg")
    op.add_option("-v", "--verbose", dest="verbose", action="store_true",
                   default=False, help="produce verbose output")

    (options, args) = op.parse_args()
    
    check_file(options.sentences, options.grammar, options.verbose)
