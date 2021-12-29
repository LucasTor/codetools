from uuid import uuid4
from hashlib import md5
from datetime import datetime

def echo_secret_key():
    now_md5 = md5(datetime.now().isoformat().encode()).hexdigest()
    return (f'{now_md5}-{uuid4()}')

if __name__ == '__main__':
    print(echo_secret_key())