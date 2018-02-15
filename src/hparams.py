from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import numpy as np


class Iwslt16EnDeBpe32Params(object):
  """For small experiments."""

  dataset = "IWSLT 2016 En-De with BPE 32K"
  data_path = "data/bpe_32k/en-de"

  train_limit = None
  source_train = "train.bpe.en"
  target_train = "train.bpe.de"

  source_valid = "dev2010.bpe.en"
  target_valid = "dev2010.bpe.de"

  source_vocab = "en.bpe.32000.vocab"
  target_vocab = "de.bpe.32000.vocab"

  vocab_size = 32000
  max_train_len = 400  # None

  unk = "<unk>"
  bos = "<s>"
  eos = "</s>"
  unk_id = 31997
  eos_id = 31998
  bos_id = 31999

  pad = bos
  pad_id = bos_id

  cuda = True

  d_word_vec = 256  # size of word and positional embeddings
  d_model = 256  # size of hidden states
  d_inner = 512  # hidden dimension of the position-wise ff
  d_k = 64  # dimension of attention keys
  d_v = 64  # dimension of attention values

  n_layers = 5  # number of layers in a Transformer stack
  n_heads = 2   # number of attention heads

  dropout = 0.1  # probability of dropping

  share_emb_and_softmax = True  # share embedding and softmax

  # training
  batch_size = 50
  learning_rate = 0.00035
  warmup_step = 4000
  label_smoothing = 0.1

  n_epochs = 50
  n_train_steps = 100000
  n_warm_ups = 4000


class Iwslt16EnDeBpe16Params(object):
  """For small experiments."""

  dataset = "IWSLT 2016 En-De with BPE 16K"
  data_path = "data/bpe_16k/en-de"

  train_limit = None
  source_train = "train.bpe.en"
  target_train = "train.bpe.de"

  source_valid = "dev2010.bpe.en"
  target_valid = "dev2010.bpe.de"

  source_vocab = "en.bpe.16000.vocab"
  target_vocab = "de.bpe.16000.vocab"

  vocab_size = 16000
  max_train_len = 600

  unk = "<unk>"
  bos = "<s>"
  eos = "</s>"
  unk_id = 15997
  eos_id = 15998
  bos_id = 15999

  pad = bos
  pad_id = bos_id

  cuda = True

  d_word_vec = 256  # size of word and positional embeddings
  d_model = 256  # size of hidden states
  d_inner = 512  # hidden dimension of the position-wise ff
  d_k = 64  # dimension of attention keys
  d_v = 64  # dimension of attention values

  n_layers = 5  # number of layers in a Transformer stack
  n_heads = 2   # number of attention heads

  dropout = 0.1  # probability of dropping

  share_emb_and_softmax = True  # share embedding and softmax

  # training
  batch_size = 64
  learning_rate = 0.00035
  warmup_step = 4000
  label_smoothing = 0.1

  n_epochs = 50
  n_train_steps = 100000
  n_warm_ups = 4000


class Iwslt16EnDeTinyParams(Iwslt16EnDeBpe16Params):
  """Shrinks Iwslt16EnDeBpe16Params for sanity check."""

  dataset = "Tiny IWSLT 2016 En-De with BPE 16K"
  train_limit = 5000 # None
  max_train_len = 300

  batch_size = 144
  n_epochs = 10
  n_train_steps = 20000
  cuda = True

  d_word_vec = 128
  d_model = 128
  d_inner = 256

  d_k = 64
  d_v = 64

  n_layers = 4
  n_heads = 2

