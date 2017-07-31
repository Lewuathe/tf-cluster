import json

import tensorflow as tf

tf.flags.DEFINE_string(
    'job', 'worker', 'Specify job type in your cluster spec'
)
tf.flags.DEFINE_integer(
    'task', 0, 'Specify task with 0-based index'
)

FLAGS = tf.flags.FLAGS

def main(argv):
  with open('./config/cluster_spec.json') as f:
    spec = json.load(f)

  cluster = tf.train.ClusterSpec(spec)
  print("job_name: {}, task_index: {}".format(FLAGS.job, FLAGS.task))
  server = tf.train.Server(cluster, job_name=FLAGS.job, task_index=FLAGS.task)

  server.join()

if __name__ == '__main__':
  tf.app.run()