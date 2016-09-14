### Flask Web Server
```sh
docker build -t python3-flask .

docker run -it --rm -p 8080:8080 python3-flask

curl -L http://0.0.0.0:8080
```

