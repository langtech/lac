from nltk import ConditionalFreqDist
from nltk.corpus import inaugural

cfd = ConditionalFreqDist(
          (target, fileid[:4])
          for fileid in inaugural.fileids()
          for w in inaugural.words(fileid)
          for target in ['america', 'citizen']
          if w.lower().startswith(target))

cfd.plot()
