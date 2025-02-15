"""Module defining inputters.

Inputters implement the logic of transforming raw data to vectorized inputs,
e.g., from a line of text to a sequence of embeddings.
"""
from onmt.inputters.inputter import get_fields, build_vocab, filter_example
from onmt.inputters.iterator import max_tok_len, OrderedIterator
from onmt.inputters.dataset_base import Dataset
from onmt.inputters.text_dataset import text_sort_key, TextDataReader
from onmt.inputters.keyphrase_dataset import kp_sort_key, KeyphraseDataReader, KeyphraseDataset
from onmt.inputters.datareader_base import DataReaderBase


str2reader = {
    "text": TextDataReader, "keyphrase": KeyphraseDataReader}
str2sortkey = {
    'text': text_sort_key, "keyphrase": text_sort_key
}
str2dataset = {
    'text': Dataset, "keyphrase": KeyphraseDataset
}

__all__ = ['Dataset', 'get_fields', 'DataReaderBase', 'filter_example',
           'build_vocab', 'OrderedIterator', 'max_tok_len',
           'text_sort_key', 'TextDataReader',
           'kp_sort_key', 'KeyphraseDataReader',
           'Dataset', 'KeyphraseDataset']
