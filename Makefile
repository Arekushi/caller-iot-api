start:
	python wsgi.py

freeze:
	pip freeze > requirements.txt

create-cert:
	openssl req -config "F:\Anaconda\envs\caller-iot-api\Library\ssl\openssl.cnf" -x509 -days 365 -newkey rsa:1024 -keyout ./cert/key.pem -nodes -out ./cert/cert.pem
