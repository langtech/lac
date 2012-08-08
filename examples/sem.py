from nltk import parse_fcfg, FeatureChartParser
grammar = parse_fcfg(open('grammar.fcfg'))
parser = FeatureChartParser(grammar, trace=1)
sent = 'Cyril bites an ankle'.split()
parser.nbest_parse(sent)

