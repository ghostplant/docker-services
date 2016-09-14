### Registry Server
```sh
openssl genrsa -out export/ca.key 4096
openssl req -new -x509 -text -subj '/CN=docker-registry/' -key export/ca.key -out export/ca.crt
cd ..

docker build -t docker-registry .

htpasswd -nbB user pass >> export/htpasswd

docker run -it --rm -p 8080:5000 \
	-v `pwd`/export:/export \
	docker-registry
```

### Docker Client
```sh
echo "${SERVER_IP:-127.0.0.1} docker-registry" >> /etc/hosts

mkdir -p /etc/docker/certs.d/docker-registry:8080

openssl s_client -connect docker-registry:8080 -showcerts < /dev/null 2>/dev/null | openssl x509 -outform PEM | sudo tee /etc/docker/certs.d/docker-registry:8080/ca.crt

docker login docker-registry:8080
docker tag example docker-registry:8080/example
docker push docker-registry:8080/example
```
