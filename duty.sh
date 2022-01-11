#!/bin/bash
python /data/project/getData.py
sleep .5
chmod 700 /data/project/data.json
cat /data/project/data.json
mongoimport -d station -c data --drop --file /data/project/data.json --jsonArray
sleep .5
/data/project/check_data.sh
