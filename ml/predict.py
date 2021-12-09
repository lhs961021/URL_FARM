from konlpy.tag import Okt
import pandas as pd
import numpy as np
import tensorflow as tf
# tf.random.set_seed(777)
# from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle



def predict_category(doc):
    category=['IT', 'Economy', 'International', 'Culture', 'Society', 'Sports', 'Politics', 'Area']
    loaded_model = load_model('ml/best_model',compile=False)
    
    pos=okt_pos(doc)
    l=[]
    l.append(pos)
    docu={}
    docu['본문']=l
    data=pd.DataFrame.from_dict(docu)
 
    
    with open('ml/tokenizer.pickle', 'rb') as handle:
        tokenizer= pickle.load(handle)
    
    tokenizer.fit_on_texts(data['본문'])
    sequence=tokenizer.texts_to_sequences(data['본문'])
    max_len=72 #학습할때 시퀀스 최대길이
    padding=pad_sequences(sequence,maxlen=max_len, truncating='post', padding='post')
    #truncating='post', padding='post' 앞에꺼는 길이가 안맞을때 뒤에 0으로 채운다는거, 뒤에꺼는 넘어갈때 뒤에 자른다는거
    result=loaded_model.predict(padding)
    result=np.argmax(result,axis=1)[0]
    print(category[result])
    return category[result]
    

def okt_pos(doc):
    pos=[]
    okt=Okt()
   
    for i,j in okt.pos(doc, stem=True):
        if j in ['Noun','Adjective']:
            pos.append(i)
    
    return pos