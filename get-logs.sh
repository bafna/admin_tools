#!/bin/bash -xe

rm -f rgw.log
python dump-logs.py
zcat /home/obj_team/radosgw.log*gz* | grep -v "s3:GET /:" >> rgw.log
cat  /home/obj_team/radosgw.log-dss* | grep -v "s3:GET /:" >> rgw.log 
