main	: getData.py
	python /data/project/getData.py
	mongoimport -d station -c data --drop --file /data/project/data.json --jsonArray
mongo	:
	mongo -u root -p 1234
clean :
	rm /data/project/data.json
