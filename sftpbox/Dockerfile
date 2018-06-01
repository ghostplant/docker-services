FROM alpine:3.4
MAINTAINER CUI Wei <ghostplant@qq.com>

ENV ROOT_PASS="badmin"

RUN apk --update add openssh && rm -r /var/cache/apk
RUN /bin/echo -e "Port 22\nProtocol 2\nHostKey /data/sftpbox-data/ssh_host_rsa_key\nHostKey /data/sftpbox-data/ssh_host_dsa_key\nHostKey /data/sftpbox-data/ssh_host_ecdsa_key\nHostKey /data/sftpbox-data/ssh_host_ed25519_key\nUsePrivilegeSeparation yes\nKeyRegenerationInterval 3600\nServerKeyBits 1024\nSyslogFacility AUTH\nLogLevel INFO\nChrootDirectory /data/sftpbox-data/share\nX11Forwarding no\nForceCommand internal-sftp\nLoginGraceTime 30\nPermitRootLogin yes\nStrictModes yes\nRSAAuthentication yes\nPubkeyAuthentication no\nIgnoreRhosts yes\nRhostsRSAAuthentication no\nHostbasedAuthentication no\nIgnoreUserKnownHosts yes\nPermitEmptyPasswords no\nChallengeResponseAuthentication no\n#PasswordAuthentication yes\nPrintMotd no\nTCPKeepAlive yes\nAcceptEnv LANG LC_*\nSubsystem sftp /usr/lib/ssh/sftp-server\nClientAliveInterval 60\nClientAliveCountMax 1" > /etc/ssh/sshd_config

VOLUME ["/data"]
EXPOSE 22/tcp

CMD ["sh", "-ce", "mkdir -p /data/sftpbox-data/share; echo root:${ROOT_PASS} | chpasswd; [ -e /data/sftpbox-data/ssh_host_rsa_key ] || ( ssh-keygen -A && mv /etc/ssh/ssh_host_* /data/sftpbox-data/ ); /usr/sbin/sshd -D"]
