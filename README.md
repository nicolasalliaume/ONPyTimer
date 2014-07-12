ONPyTimer
=========

ONPyTimer allows to monitor time difference between the lines of a Python script in a stopwatch-like manner

Usage
---------

```python

from ONPyTimer import *

ONPyTimer.check(flag='A')   # will show current time and flag name
...
ONPyTimer.check(flags=['A']) # will show time diff from flag 'A'
...
ONPyTimer.check(flag='B', flags=['A']) # will show new flag name and time diff
... 								   # from flag 'A'
...
ONPyTimer.check(flags=['A', 'B']) # will show time diff from flags 'A' and 'B'
```

Author
---------

Author: Nicolas Alliaume - ON Lab
GitHub: http://github.com/nicolasalliaume/ONPyTimer
@ 2014
