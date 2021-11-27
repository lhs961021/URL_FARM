from konlpy.tag import Okt
import pandas as pd
import numpy as np
import tensorflow as tf
tf.random.set_seed(777)
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict_category():
    pass

def okt_pos(doc):
    noun=[]
    okt=Okt()
    
    for i in okt.pos(doc, stem=True):
        if i[1] in ['Noun']:
            noun.append(i[0])
    print(noun)
    return noun