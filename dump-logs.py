# /bin/python

import boto
import boto.s3.connection
import glob
import ntpath
import socket
#import key
from key import *

conn = boto.connect_s3(aws_access_key_id = access_key,aws_secret_access_key = secret_key,port=port_number, debug=2,host = hostname, is_secure=False, calling_format = boto.s3.connection.OrdinaryCallingFormat(),)
bucket = conn.create_bucket('log_bucket')
L = list()
count = 0
for key in bucket.list():
    if "radosgw" in key.name:
        L.append(key.name)
        print key.name
        keyname = bucket.get_key(key.name);
        key.get_contents_to_filename('/home/obj_team/' + key.name);


