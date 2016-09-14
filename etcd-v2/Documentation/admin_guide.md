# Administration

### Lifecycle

For maximum safety, if an etcd member suffers any sort of data corruption or loss, it must be removed from the cluster.
Once removed the member can be re-added with an empty data directory.

### Lifecycle

If you are spinning up multiple clusters for testing it is recommended that you specify a unique initial-cluster-token for the different clusters.
This can protect you from cluster corruption in case of mis-configuration because two members started with different cluster tokens will refuse members from each other.

#### Health Monitoring

At lowest level, etcd exposes health information via HTTP at `/health` in JSON format. If it returns `{"health": "true"}`, then the cluster is healthy. Please note the `/health` endpoint is still an experimental one as in etcd 2.2.

```
$ curl -L http://127.0.0.1:2379/health

{"health": "true"}
```

### Optimal Cluster Size

The recommended etcd cluster size is 3, 5 or 7, which is decided by the fault tolerance requirement. A 7-member cluster can provide enough fault tolerance in most cases. While larger cluster provides better fault tolerance the write performance reduces since data needs to be replicated to more machines.

#### Changing Cluster Size

After your cluster is up and running, adding or removing members is done via [runtime reconfiguration][runtime-reconfig], which allows the cluster to be modified without downtime. The `etcdctl` tool has `member list`, `member add` and `member remove` commands to complete this process.

### Member Migration

When there is a scheduled machine maintenance or retirement, you might want to migrate an etcd member to another machine without losing the data and changing the member ID.

The data directory contains all the data to recover a member to its point-in-time state. To migrate a member:

* Stop the member process.
* Copy the data directory of the now-idle member to the new machine.
* Update the peer URLs for the replaced member to reflect the new machine according to the [runtime reconfiguration instructions][update-a-member].
* Start etcd on the new machine, using the same configuration and the copy of the data directory.

This example will walk you through the process of migrating the infra1 member to a new machine:

|Name|Peer URL|
|------|--------------|
|infra0|10.0.1.10:2380|
|infra1|10.0.1.11:2380|
|infra2|10.0.1.12:2380|

```sh
$ export ETCDCTL_ENDPOINT=http://10.0.1.10:2379,http://10.0.1.11:2379,http://10.0.1.12:2379
```

```sh
$ etcdctl member list
84194f7c5edd8b37: name=infra0 peerURLs=http://10.0.1.10:2380 clientURLs=http://127.0.0.1:2379,http://10.0.1.10:2379
b4db3bf5e495e255: name=infra1 peerURLs=http://10.0.1.11:2380 clientURLs=http://127.0.0.1:2379,http://10.0.1.11:2379
bc1083c870280d44: name=infra2 peerURLs=http://10.0.1.12:2380 clientURLs=http://127.0.0.1:2379,http://10.0.1.12:2379
```

#### Stop the member etcd process

```sh
$ ssh 10.0.1.11
```

```sh
$ kill `pgrep etcd`
```

#### Copy the data directory of the now-idle member to the new machine

```
$ tar -cvzf infra1.etcd.tar.gz %data_dir%
```

```sh
$ scp infra1.etcd.tar.gz 10.0.1.13:~/
```

#### Update the peer URLs for that member to reflect the new machine

```sh
$ curl http://10.0.1.10:2379/v2/members/b4db3bf5e495e255 -XPUT \
-H "Content-Type: application/json" -d '{"peerURLs":["http://10.0.1.13:2380"]}'
```

Or use `etcdctl member update` command

```sh
$ etcdctl member update b4db3bf5e495e255 http://10.0.1.13:2380
```

#### Start etcd on the new machine, using the same configuration and the copy of the data directory

```sh
$ ssh 10.0.1.13
```

```sh
$ tar -xzvf infra1.etcd.tar.gz -C %data_dir%
```

```
etcd -name infra1 \
-listen-peer-urls http://10.0.1.13:2380 \
-listen-client-urls http://10.0.1.13:2379,http://127.0.0.1:2379 \
-advertise-client-urls http://10.0.1.13:2379,http://127.0.0.1:2379
```

