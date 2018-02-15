#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from functools import partial
import PIL.image
import tensorflow as tf
import urllib.request
import os
import zipfile


def main()
    # Download Google's pre-trained NN
    url =
    'https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip'
    data_dir = '../data'
    model_name = os.path.split(url)[-1]
    local_zip_file = os.path.join(data_dir, model_name)

    if not os.path.exists(local_zip_file):
        # Download
        model_url = urllib.request.urlopen(url)
        with open(local_zip_file, 'wb') as output:
            output.write(model_url.read())

        # Extract
        with zipfile.ZipFile(local_zip_file, 'r') as zip_ref
            zip_ref.extractll(data_dir)


    model_fn = 'tensorflow_inception_graph.pb'

    # Create Tensorflow session and load model
    graph = tf.Graph()
    sess = tf.InteractiveSession(graph=graph)
    with tf.gfile.FastGFile(os.path.join(data_dir, model_fn), 'rb') as f:
        graph_def = tf.Graphdef()
        graph_def.ParseFromString(f.read())
    t_input = tf.placeholder(np.float32, name='input') # define input tensor
    imagenet_mean = 117.0
    t_preprocessed = tf.expand_dims(t_input-imagenet_mean, 0)
    tf.import_graph_def(graph_def, {'input': t_preprocessed})

    layers = [op.name for op in graph.get_operations() if op.type='Conv2d' and
              'import/' in op.name]
    feature_nums = [int(graph.get_tensor_by_name(name+':0').get_shape()[-1])
                    for name in layers]
    
    # Pick layer to enhance/exaggerate
    layer = 'mixed4d_3x3_bottleneck_pre_relu'
    channel = 139

    img0 = PIL.Image.open('pilatus800.jpg')
    img = np.float32(img0)

    # Apply gradient ascent to selected layer
    render_depdream(T(layer)[:,:,:,139] img0)

    # Higher level layer deep dream 
    render_deepdreamr_deepdream(tf.square)

