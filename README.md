tf-cluster [![Docker Pulls](https://img.shields.io/docker/pulls/lewuathe/tf-cluster.svg)](https://hub.docker.com/r/lewuathe/tf-cluster/)
===

TensorFlow distributed cluster on Docker

## Usage

Launch a cluster by using docker compose

```
$ make run
```

Shutdown cluster

```
$ make down
```

## Example

```
$ python example/tf_dist_sample.py
Start session
[[ 3 10 21]
 [ 6 15 28]]
```