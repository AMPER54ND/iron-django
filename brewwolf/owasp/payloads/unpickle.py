from  pickle import loads
import sys
import base64

loads(base64.b64decode(sys.argv[1]))
print("done")