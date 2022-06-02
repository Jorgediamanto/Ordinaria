%matplotlib inline
import pandas as pd
import random 
from plotly import graph_objs as go 
import plotly.express as px 
import plotly.figure_factory as ff 
from collections import Counter

from PIL import Image 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import nltk 
from nltk.corpus import stopwords

from tqdm import tqdm 
import os 
import nltk 
import spacy 
import random 
from spacy.util import compounding 
from spacy.util import minibatch

import warnings 
warnings.filterwarnings("ignore")

import os 
for dirname, _, filenames in os.walk('/kaggle/input'):
     for filename in filenames:
          print(os.path.join(dirname, filename))


def funcion_auxiliar_colores(): #crea un color aleatorio con sus tres componentes y lo devuelve
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = [r,g,b]
    return rgb

def jaccard(str1, str2):
    a = set(str1.lower().split())
    b = set(str2.lower().split()) 
    c = a.intersection(b) 
    return float(len(c)) / (len(a) + len(b) - len(c)) 

train = pd.read_csv('/kaggle/input/tweet-sentiment-extraction/train.csv')
test = pd.read_csv('/kaggle/input/tweet-sentiment-extraction/test.csv') 
ss = pd.read_csv('/kaggle/input/tweet-sentiment-extraction/sample_submission.csv')

train.shape
test.shape
ss.shape


print(train.isnull()) #se verifica cuantos valores nulos hay

modifiedTrain = train.dropna()

modifiedTrain.isnull().sum() #se verifica que se han eliminado los valores nulos

modifiedTrain.to_csv('modifiedTrain.csv',index=False) #devuelve el csv sin los valores nulos

x111 = len(train.index)

fig = px.funnel(modifiedTrain, x='x11', y='sentiment',color=funcion_auxiliar_colores())
fig.show()






