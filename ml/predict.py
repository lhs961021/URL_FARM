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

from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from wordcloud import WordCloud
import platform 
from django.conf import settings
import os
# import matplotlib.pyplot as plt


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

def tfidfwordcloud(doc,id):
    l=[]
    l.append(doc)
    d={}
    d["본문"]=l
    d=pd.DataFrame.from_dict(d)
    
    vectorizer=TfidfVectorizer()
    matrix=vectorizer.fit_transform(d['본문'])
    
    word2id = defaultdict(lambda : 0)
    for idx, feature in enumerate(vectorizer.get_feature_names_out()):
        word2id[feature] = idx
        
    ll=[]
    for i, sent in enumerate(d['본문']):
        print('====== document[%d] ======' % i)
        ll.append([ (token, matrix[i, word2id[token]]) for token in sent.split() ] )
        
    dic={}
    dic['tf-idf']=ll
    dic=pd.DataFrame.from_dict(dic)
    
    if platform.system() == 'Darwin': #맥
        wordcloud=WordCloud(font_path="AppleGothic",width=800,height=800,background_color='white',max_font_size=2000)
    elif platform.system() == 'Windows': #윈도우
        wordcloud=WordCloud(font_path="Malgun Gothic",width=800,height=800,background_color='white',max_font_size=2000)
        
    elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        wordcloud=WordCloud(font_path="Malgun Gothic",width=800,height=800,background_color='white',max_font_size=2000)
        
    wordcloud.generate_from_frequencies(dict(dic['tf-idf'][0]))
    path=settings.STATICFILES_DIRS
    path="".join(path)
    path=os.path.join(path,'img')
    path=os.path.join(path,'wordcloud')
    # print(path)
    pathname=f'wordcloud{id}-1.jpg'
    path=os.path.join(path,pathname)
    print(path)
    wordcloud.to_file(path)
