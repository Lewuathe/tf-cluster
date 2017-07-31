#!/usr/bin/env python

import sys
import json
import tensorflow as tf

def run_job():

  with open('./config/cluster_spec.json') as f:
    cluster_spec = json.load(f)

  with tf.device('/job:ps/task:0'):
    v = tf.Variable([1,2,3], dtype=tf.int32)
  with tf.device('/job:worker/task:0'):
    c = tf.constant([2,3,4])
    x = v + c
  with tf.device('/job:worker/task:1'):
    ret = x * tf.constant([[1,2,3], [2,3,4]])
  with tf.Session("grpc://localhost:2222") as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print("Start session")
    res = sess.run(ret)
    print(res)


if __name__ == '__main__':
  run_job()