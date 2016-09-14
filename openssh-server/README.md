### OpenSSH Server
```sh
docker build -t openssh-server .

docker run -it --rm -p 8022:22 -v ${HOME}:/mnt openssh-server

ssh -oUserKnownHostsFile=/dev/null root@0.0.0.0 -p 8022
```

