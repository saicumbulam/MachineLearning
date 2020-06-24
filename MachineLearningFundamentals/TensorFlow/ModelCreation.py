import tensorflow as tf

def init_labels(output_size):
  labels = tf.placeholder(
    tf.int32, shape=(None, output_size), name='labels')
  return labels

def init_inputs(input_size):
  inputs = tf.placeholder(
    tf.float32, shape=(None, input_size), name='inputs')
  return inputs


def model_layers(inputs, output_size):
  logits = tf.layers.dense(inputs, output_size,
                           name='logits')
  return logits