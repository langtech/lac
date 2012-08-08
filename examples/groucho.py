from nltk import parse_cfg, ChartParser

groucho_grammar = parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot' 
P -> 'in' 
""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = ChartParser(groucho_grammar) 
trees = parser.nbest_parse(sent)
for tree in trees:
    print tree
