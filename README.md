# CP 1: RUD+:Rescue Using Detection

증가하는 정신 건강의 위험성과 관련 서비스 접근성이 낮은 현실에 도움이 되고자 기획하였습니다.

접근성을 높여 조기진단과 조기치료가 좀 더 쉬워지도록,

좀 더 쉽게 어떤 환경이 날 힘들게 하는 지 인지할 수 있도록

하기 위해 고안한 웹 서비스 입니다.

## ver_1 : submit ver.
- model 
  - classification model : building model using LSTM, dropout
  - keyword model : import library using keyBERT
 
- web
  - flask
  - html

## ver_2 : model change
 - model
    - nltk vader 이용 : sentiment analysis 
