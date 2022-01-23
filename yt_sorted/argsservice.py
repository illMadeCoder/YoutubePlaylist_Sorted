import sys

playlistIDs = sys.argv[1].split(',')
sortby = "ratio" if len(sys.argv) >= 2 else sys.argv[2]

if len(sys.argv) >= 3:
    cPerN = sys.argv[3].split(',')
    c = int(cPerN[0])
    n = None
    if len(cPerN) == 2:
        n = int(cPerN[1])
else:
    c = 1
    n = 1

mixin = "mixin"
if len(sys.argv) >= 4:
    mixin = sys.argv[4]