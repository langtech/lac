from nltk import parse_cfg, ChartParser
from nltk.draw import draw_trees

grammar = parse_cfg("""
  S -> NP V NP
  NP -> NP Sbar
  Sbar -> NP V 
  NP -> 'fish'
  V -> 'fish'
""")

for i in range(3,23,2):
    tokens = ["fish"] * i
    cp = ChartParser(grammar)
    print len(cp.nbest_parse(tokens)),
