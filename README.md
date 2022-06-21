# RUD+:Rescue Using Detection

It is designed to help the reality of increasing mental health risks and low access to related services.</br>
- To make early diagnosis and treatment easier by increasing accessibility</br>
- We can easily recognize what kind of environment is giving us a hard time


## ver_1 : submit ver.
- Data [🧷Link](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch)

  ![image](https://user-images.githubusercontent.com/50479962/174747838-1e6b918f-aed3-4b78-b64f-107132e932ae.png)
  - 232074 rows x 2 columns (dtypes: str)
    - target 1 : suicide
    - target 0 : non-suicide
      
- Model 
  - classification model : building model using LSTM, dropout </br>
  
     -> 불안정: ver_2 개발 이유</br>
     
       target을 기준으로 label 1은 심각하게 우울한 사람, label 0은 경미한 상태의 우울한 사람으로 </br>
       target을 판단하여 LSTM을 이용하여 점수화 시키고자 했으나 모델을 훈련시키기에 정보가 너무 부족하다고 판단 </br>
     ![image](https://user-images.githubusercontent.com/50479962/174748864-58f18b15-fefd-4b72-a855-e9bb311f3e10.png)

  - keyword model : import library using keyBERT
 
## ver_2 : model change __ this is current version
 - Model
    - sentiment analysis : nltk vader 이용 
 - Web
    - flask
    - html
 - Play
   ![rudplus](https://user-images.githubusercontent.com/50479962/174746562-90730cdd-7760-40b8-bcc4-1f430dbb25aa.gif)
 

## ver_3 : imporve the project
- topic model experiment
  - LSA
  - LDA
  - keyBERT
  - BERTopic
  - combinend topic model
- sentiment analysis for classification

## plan to
- apply korean
- deploy
