import pandas as pd
import numpy as np


import seaborn as sns

import neattext.functions as nfx

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

#Transformers
from  sklearn.feature_extraction.text import CountVectorizer
from  sklearn.model_selection import train_test_split
from  sklearn.metrics import accuracy_score,classification_report,confusion_matrix

from sklearn.pipeline import Pipeline

df = pd.read_csv("emotion_dataset_2.csv")

df.head()

# Vlaue Counts
df['Emotion'].value_counts()

#plot
sns.countplot(x='Emotion',data=df)

# Data Cleaning
dir(nfx)

#User Handles
df['Clean_Text']=df['Text'].apply(nfx.remove_userhandles)

#User StopWords
df['Clean_Text']=df['Clean_Text'].apply(nfx.remove_stopwords)

# Features & Lables
Xfeatures = df['Clean_Text']
ylabels = df['Emotion']

# Split data
x_train,x_test,y_train,y_test = train_test_split(Xfeatures,ylabels,test_size=0.3,random_state=42)

pipe_lr = Pipeline (steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])

pipe_lr.fit(x_train,y_train)

pipe_lr.score(x_test,y_test)

# Make Prediction
exl = " This book is sop interesting to read"

pipe_lr.predict([exl])

pipe_lr.predict_proba([exl])

pipe_lr.classes_

# Save Model and Pipeline
import joblib 
pipeline_file = open("emotion.pkl","wb")
joblib.dump(pipe_lr,pipeline_file)
pipeline_file.close()