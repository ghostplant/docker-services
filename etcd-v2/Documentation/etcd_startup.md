### ETCD Startup Example

```sh
ETCD_NAME=etcd_1
ETCD_ADVERTISE_CLIENT_URLS="http://192.168.1.200:2379"
ETCD_LISTEN_CLIENT_URLS="http://192.168.1.200:2379"
ETCD_INITIAL_ADVERTISE_PEER_URLS="http://192.168.1.200:2380"
ETCD_LISTEN_PEER_URLS="http://192.168.1.200:2380"
ETCD_INITIAL_CLUSTER="etcd_1=http://192.168.1.200:2380,etcd_2=http://192.168.1.201:2380,etcd_3=http://192.168.1.202:2380"

etcdctl --peers http://192.168.1.200:2379

curl -L http://localhost:2379/v2/stats/leader 2>/dev/null | grep -v not >/dev/null && echo 'As leader.'
```

