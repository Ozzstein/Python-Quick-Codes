# Open the `/data/500-worst-passwords.txt.bz2` file and list the first 10. Hint: You will need to set a parameter called encoding equal to utf8, i.e. `encoding=utf8` in the open function.

import bz2

with bz2.open("/data/500-worst-passwords.txt.bz2", "rt") as inf:
    lines = inf.readlines()

print(lines[:10])
