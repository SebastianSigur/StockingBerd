import tensorflow as tf


def create_padding_mask(seq):
    seq = tf.cast(tf.math.equal(seq, 0), tf.float32)  # 1 where it equals 0, 0 otherwise

    return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)


def create_look_ahead_mask(size):
    mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
    # [[0,1,1,1],
    #  [0,0,1,1]]
    #  [0,0,0,1]]
    #  [0,0,0,0]]
    return mask  # (seq_len, seq_len)

