

import os
player = 'bob'

filename = player+'.txt'

if os.path.exists(filename):
    append_write = 'a'
else:
    append_write = 'w'

highscore = open(filename,append_write)
highscore.write("Username: " + player + '\n')
highscore.close()
