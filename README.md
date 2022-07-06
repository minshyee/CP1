# RUD+:Rescue Using Detection

이 프로젝트는 정신건강에 대한 관심도가 높아짐에 따라 진행하게 된 프로젝트입니다.</br>
현재 관련 건강서비스 이용 시, 많은 사람들의 선입견을 피할 수 없습니다.</br>
그 결과로 낮은 정신건강치료 서비스 이용율이 낮아지는 것을 깨달았습니다.</br>
이러한 현실을 탈피해 보고자 해당 서비스를 기획하였습니다.</br>

- 접근성을 높여 조기 진단 및 치료 연결이 가능하도록 하는 서비스
- 적어도, 현재 나를 괴롭히는 키워드가 무엇인지 알 수 있도록 도와주는 서비스
 

## ver_1 : submit ver.
- Data [🧷Link](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch)

  ![image](https://user-images.githubusercontent.com/50479962/174747838-1e6b918f-aed3-4b78-b64f-107132e932ae.png)
  - 232074 rows x 2 columns (dtypes: str)
    - target 1 : suicide
    - target 0 : non-suicide
- Visualization
  ![image](https://user-images.githubusercontent.com/50479962/175191504-1e85ef85-6238-4a30-b4b4-80ab6dc36115.png)

      
- Model 
  - classification model : building model using LSTM, dropout </br>
  
     -> 불안정: ver_2 개발 이유</br>
     
       target을 기준으로 label 1은 심각하게 우울한 사람, label 0은 경미한 상태의 우울한 사람으로 </br>
       target을 판단하여 LSTM을 이용하여 점수화 시키고자 했으나 모델을 훈련시키기에 정보가 너무 부족(feature 2개)하다고 판단 </br>
     ![image](https://user-images.githubusercontent.com/50479962/174748864-58f18b15-fefd-4b72-a855-e9bb311f3e10.png)

  - keyword model : import library using keyBERT
      - 실시간으로 예측 시, 좀 더 빠르게 작동할 수 있는 모델
      
## ver_2 : model change __ this is current version
 - Model
    - sentiment analysis : nltk vader 이용 
      - 사용이유 : 문장 그대로인 상태로 감정점수를 매김. feature를 기반으로 예측하는 것보다 신뢰도가 높다고 
    - keyword model : import library using keyBERT
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
