# L&C Project 1
# Firstname LASTNAME
# STUDENT-ID

"""
<approximately 400 words of discussion about what your program does,
and what problems you tacked and solved (or could not solve).
Are there other sources of linguistic information that would have
been useful? Briefly describe a possible application of this software.
"""

# optionally import NLTK modules here (e.g. tokenizer or corpus)

def truecase(s):
    # put your code here

    return t

def evaluate(s):
    t = s.lower()
    # put your code here

    return 0.0
    

# Main program: read in the data, process it, and print the result
if __name__ == '__main__':

    # get the filename
    import sys
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        exit("Usage: " + sys.argv[0] + " filename")

    # get the data out of the file
    try:
        input = open(filename).read()
    except IOError:
        exit("Cannot open: " + filename)

    # process the data
    result = evaluate(input)
    print(result)
