import opensmile
import pandas as pd
import numpy as np 
from sklearn.neural_network import MLPClassifier
import sounddevice as sd
import os
import sys

import subprocess



# print(os.getcwd())

smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.Functionals,
    )



def TrainModel():
    title = []
    
    for i in range(89):
        title.append("Feature "+str(i))

    angry_csv = os.path.join("D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/bin/angry.csv")
    sad_csv = os.path.join("D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/bin/sad.csv")
    happy_csv = os.path.join("D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/bin/happy.csv")
    calm_csv = os.path.join("D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/bin/calm.csv")

    angry_df = pd.read_csv( angry_csv ,names = title).drop('Feature 88', axis=1)
    sad_df   = pd.read_csv( sad_csv   ,names = title).drop('Feature 88', axis=1)
    happy_df = pd.read_csv( happy_csv ,names = title).drop('Feature 88', axis=1)
    calm_df  = pd.read_csv( calm_csv  ,names = title).drop('Feature 88', axis=1)
    
    
    feature_df = pd.concat([angry_df,sad_df,happy_df,calm_df],axis=0)
    feature_reset_df = feature_df.reset_index().drop('index', axis=1)

    minmax_data_df = pd.DataFrame()
    min_list=[]
    max_list=[]
    minus_list=[]
    for i in title[:88]:
        min_data = np.min(feature_reset_df[i])
        max_data = np.max(feature_reset_df[i]) 
        min_list.append(min_data)
        max_list.append(max_data)
        minus_list.append(max_data-min_data)
        normlist = (feature_reset_df[i]-min_data)/(max_data - min_data)
        minmax_data_df=pd.concat([minmax_data_df,normlist],axis=1)
    DataFeature = minmax_data_df.to_numpy()

    Datalabels=[]
    for i in range(20):
        Datalabels.append(0)
    for i in range(20):
        Datalabels.append(1)
    for i in range(20):
        Datalabels.append(2)
    for i in range(20):
        Datalabels.append(3)   
    Datalabels = np.array(Datalabels)

    MLP_clf = MLPClassifier(solver='adam', alpha=0.001,activation='relu',
                            hidden_layer_sizes=(10),max_iter=800,random_state=1)
    MLP_clf.fit(DataFeature, Datalabels)

    return MLP_clf, min_list, minus_list


def RealTimeRecognition(MLP_clf=1,min_list=1,minus_list=1):
    duration = 5  # seconds
    fs = 44100

    # Start recording
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    print("Recording started.")
    sd.wait()  # Wait for the recording to finish
    print("Recording finished.")
    test_audio = smile.process_signal(signal =recording.T,sampling_rate=fs)
    test_audio = (test_audio-min_list)/minus_list
    labels=['angry','sad','happy','Neutral']
    print(labels[MLP_clf.predict(test_audio)[0]])


def test():
    print('START')

    MLP_clf, min_list, minus_list = TrainModel()
    RealTimeRecognition(MLP_clf,min_list,minus_list)
    
    # # RealTimeRecognition()
    # # a, b, c = TrainModel()
    # # print( RealTimeRecognition(a,b,c) )
    print('END')


    # Check sys path

    #D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script 

# test()

# if __name__ == __main__:
#     print('Importing!!')