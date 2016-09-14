### Docker Auth
```sh
openssl genrsa -out config/ca.key 4096
openssl req -new -x509 -text -subj '/CN=docker-auth/' -key config/ca.key -out config/ca.crt

docker build -t docker-auth .

docker run -it --rm -p 5001:5001 -v `pwd`/config:/config docker-auth
```

### Client Test
```sh
curl -k https://127.0.0.1:5001/auth
```
