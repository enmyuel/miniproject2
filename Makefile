main	: getData.py
	python /data/project/getData.py
	mongoimport -d station -c data --drop --file /data/project/data.json --jsonArray
clean :
	rm /data/project/data.json
