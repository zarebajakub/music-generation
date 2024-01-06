from collections import Counter
import glob
from pprint import pprint
from music21 import converter, instrument

notes = []
instrs = []

for file in glob.glob("dataset/rock/*.mid"): #HERE
    score = converter.parse(file)

    print("Parsing %s" % file)

    notes_to_parse = []
    
    for id, part in enumerate(instrument.partitionByInstrument(score)):
        instrs.append(part.getInstrument().__class__)
    
print(len(instrs))
pprint(Counter(instrs))