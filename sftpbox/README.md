### Portable SFTP server.

*Example:*

```sh
# Create a new SFTP server that stores files on home folder of current user.
sudo docker run -it --rm \
	-v ${HOME}/data:/data \
	-p 5022:22 \
	-e ROOT_PASS=badmin \
	ghostplant/sftpbox
```

```sh
# Use SFTP to connect to it (Login password references from above ROOT_PASS)
sftp -P 5022 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -q root@localhost
```

```sh
# Use SSHFS to mount SFTP as a local directory
echo ${ROOT_PASS} | sshfs -o port=5022 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o reconnect -o password_stdin -o compression=yes -o workaround=all root@localhost:/ /mnt
```
