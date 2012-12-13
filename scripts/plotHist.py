#plotXY by @jattenberg, Dec 2012
#


import sys
import matplotlib.pyplot as plt
from math import log
import pandas as pd
from optparse import OptionParser


#expects a list of pairs, x, #x

parser = OptionParser(usage ="""                                                                 
Generate a histogram from new-line separated numerical data of the form x1, x2, ...
each column containing values form a particular series to form a histogram over
Usage %prog [options]                                                                                
""")
parser.add_option('-f', '--file',
                  action = 'store', dest = 'filename', default=False)
parser.add_option('-b', '--bins', 
                  action='store', dest='bins', default=50)
parser.add_option('-L', '--logscale',                                                                                                                                                                                                                                                                                      
                  action = 'store_true', dest = 'log_scale', default=False)

(options, args) = parser.parse_args()
 
input = open(options.filename, 'r') if options.filename else sys.stdin


df = pd.read_csv(input)
pd.tools.plotting.hist_frame(df, bins=int(options.bins))
plt.show()
