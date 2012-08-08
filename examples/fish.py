from nltk import parse_cfg, ChartParser
from nltk.draw import draw_trees

grammar = parse_cfg("""
  S -> NP V NP
  NP -> NP Sbar
  Sbar -> NP V 
  NP -> 'fish'
  V -> 'fish'
""")

tokens = ["fish"] * 11
cp = ChartParser(grammar)
trees = cp.nbest_parse(tokens)

draw_trees(*trees)
