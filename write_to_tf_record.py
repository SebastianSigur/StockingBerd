import tensorflow as tf
import csv_data_Read

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def _floats_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def create_TFRecords(dictionary):
    tfrecord_writer = tf.io.TFRecordWriter('/Users/sebastiansebastian/TFRecords/stocks.tfrecord')
    for day in dictionary:
        x = tf.random.uniform(minval=0, maxval=100, shape=[], dtype=tf.int32)
        feature = {
            'open': _floats_feature(dictionary[day]['open']),
            'high': _floats_feature(dictionary[day]['high']),
            'low': _floats_feature(dictionary[day]['low']),
            'close': _floats_feature(dictionary[day]['close']),
            'volume': _floats_feature(dictionary[day]['volume']),
            'x': _int64_feature(x)
        }

        features = tf.train.Features(feature=feature)
        example = tf.train.Example(features=features)
        example_to_string = example.SerializeToString()
        tfrecord_writer.write(example_to_string)

    tfrecord_writer.close()


