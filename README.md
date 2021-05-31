# Project : 주식 투자 자동화 (Stock Investment Automation)

<br/>

<img width="619" alt="20210522_002726" src="https://user-images.githubusercontent.com/57824945/119161739-9b65d380-ba94-11eb-83ba-3fa6f9a882d0.png">

<br/>

## 프로젝트 소개

2020년 **코로나19** 확산으로 전 세계 주식시장이 크게 하락한 뒤 급반등한 직후부터 이른바 **'동학개미 운동'** 으로 불리는 개인들의 주식 투자 열풍이 거세졌습니다.
통계에 따르면 기존 주식 운용액이 기존 금액에 비해 **3배** 이상 증가하여 사상 최대 금액을 기록 하였다고 합니다.

### 10명 중 4명은 코로나 확산 이후 주식 직접투자를 시작 하였다고 합니다.

<br/>

하지만 저처럼 주식 전문가가 아닌 이상,  어떤 주식 종목에 언제, 얼마나 투자하고, 나아가 수익을 낸 다는 것 자체가 부담 스럽기만 합니다.

그렇게하여 생각하게 된 것이 AI 기술을 접목한 이번 프로젝트 입니다. ~~(이미 많은 사람들이 구현, 개발을 하였지만)~~

주식에 관하여 전문적인 지식이 없는 저 또한 **파이썬**을 활용하여 주식 투자 전략을 구현해보고 **증권사API**
를 통해 주가가 **기술적 전략**에 부합할 때 **자동으로 매매하는 프로그램**을 개발 합니다. 또, **카카오톡 메신저**를 통해 거래 결과를 받아볼 수 있도록 만들어 보겠습니다.

<br/>

<img width="456" alt="20210522_002953" src="https://user-images.githubusercontent.com/57824945/119161987-d6680700-ba94-11eb-9b16-ffcc6f871ce1.png">



<br/>

## 프로젝트 구조

이번 프로젝트에서 사용할 대신증권의 크레온 비대면 계좌 개설하여 크레온 API 사용 설정 합니다.
그리고 주식 자동화 프로그램을 위해 파이썬 3.8버전의 64bit 가 아닌, 32bit를 설치 및 환경변수 세팅을 합니다.
크레온의 종목 조회 API 활용하여 파이썬 코드를 다룹니다.
그리고 카카오톡 메세지로 거래 결과를 받아 볼 수 있도록 합니다.

<br/>

## 사용기술

- Python

- Pandas

- Beautiful Soup

- urllib

- Selenium

- Kakao Chatbot

<br/>

## 리뷰

저는 주식은 매도, 매수 빼고 아무것도 모르는 주린이었습니다. 지금도 거의 아는게 없는 주린이입니다. 

하지만 인터넷에서 AI 자동 투자 봇을 만드는 클래스를 보고 호기심이 생겼는데, 클래스가 아직 안 열려서 고민하다가, 
저는 코딩을 할 줄 아니까 그냥 책 한 권 들고 주식 자동 거래 프로그램을 만들어봤습니다.

나만의 수익 머신이 되었으면 하는 바램으로 시작하긴 했지만, 아주 편한 마음으로 코딩을 했습니다.

오늘이 딱 1주일째인데, 그동안 남는 시간에 이 프로젝트에만 매달려서 주식 트레이딩, 간단한 백테스팅까지 구현했습니다. 
이번 포스팅에서는 제가 주식 거래 봇을 만든 방법, 어려웠던 점을 간단히 적어보려고 합니다.