info : https://www.notion.so/95224e0e3bab4489b45bfa620d330c16
root : copy version of /var/spool/cron/crontabs/root
full_data.json : 2573

작업 내역

1. **AWS EC2 인스턴스 내 개발환경 구축**
    - Python
        - Bottle(웹 프레임워크), Folium(지도 시각화), pymongo(MongoDB 접근 및 제어) 패키지 사용
    - MongoDB
        - 공공데이터 정보 및 회원 정보를 담기 위해 사용
    - Makefile
        - 복수의 명령어를 한번에 편하게 사용하기 위해 사용
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a10ccc5f-5755-4dd8-bc60-f4a7a90d1af0/Untitled.png)
    
    - Git, Github
        - 협업 및 형상관리를 위해 사용
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ce02e73d-d212-4e38-b259-2a7069e028bc/Untitled.png)
    

1. **공공데이터 불러오기 기능 자동화**
    - crontab 명령어를 사용하여 1분에 한 번씩 자전거 대여소 정보를 가져오는 쉘 스크립트(duty.sh)를 실행한다.
    - 원활한 디버깅을 위해 쉘 스크립트의 실행결과를 로그(duty.log)로 남기게끔 설계했다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9670ec31-8a5a-4a2c-9bda-13af33678922/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7af789d3-25cb-4b3b-b17e-7332c77b93ac/Untitled.png)
    
                                                     < 1분마다 실행되는 쉘 스크립트 >
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3c4d12ae-b9f1-4c8a-b14f-ddd6a9285101/Untitled.png)
    
                                                              < duty.log의 앞 부분 >
    
2. **가져온 공공 데이터를 MongoDB에 import**
    - 2번 과정에서 볼 수 있듯이 가져온 데이터를 MongoDB의 “Station” Collection으로 import 시킨다.
    - 가져온 JSON 데이터를 그대로 사용할 수 없기 때문에 형식에 맞게 파싱을 했다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7d54081-ed2a-42fe-b1c6-907077319eb3/Untitled.png)
    
                                        < 공공데이터를 가져와서 파싱하는 코드의 일부분 >
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ebc9b7b-b2ce-4341-9bfc-63e65fed5a92/Untitled.png)
    
                                        < MongoDB 쉘에서 db.data.find()을 입력한 모습 >
    
    1. **Python Bottle web framework**
        - Backend 작업을 Python으로 진행해서 연동하기 쉽게 Bottle을 사용했다.
        - 공식 문서 및 다양한 레퍼런스를 참고하여 개발을 진행했다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2971ca40-9fbc-4473-ab28-3cb1471b9dad/Untitled.png)
    
                                          < Bottle로 URL을 매핑하는 코드의 일부 > 
    

1. **자전거 대여소 시각화 기능 자동화**
    - 데이터베이스에 저장된 데이터 수에 따라 대여소를 지도로 시각화하는 rent.html에서 사용한다.
    - 1분마다 변하는 데이터에 따라 지도에 나타나는 대여소의 숫자도 달라진다.
    - 예시로 기존 30개 였던 자전거 대여소의 수를 1000개로 늘렸을 때 페이지를 새로고침하게 되면 그 결과가 즉시 반영되는 것을 알 수 있다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/78f0ab60-bc63-405f-9c3a-3a80690fd0b4/Untitled.png)
    

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76e4fb67-2611-4f05-9ec3-6a2dfb5fd4e6/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b0f45563-4616-44d3-b785-c3e16232e54d/Untitled.png)

1. **로그인 및 회원가입 기능 처리**
    - ID와 비밀번호를 받아 데이터베이스 내의 사용자 정보와 비교해 인증의 성공/실패 여부를 판단한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97a26391-08f8-4e69-9a13-fadd42fb6748/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0b4c3a4-0559-4c56-a0ba-32276c984eb0/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41d3fa47-3fd7-42c5-b6bc-759563bb931e/Untitled.png)

                                                < 로그인 실패/성공 시 보이는 로그 >

- 회원가입 시 얻는 사용자의 정보는 member Collection에 담긴다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbe856f7-83f3-4fba-8f61-ef0a1d538671/Untitled.png)

                                       <MongoDB 내의 사용자 가입 정보 Collection >

- 느낀 점 및 향후 개선 방향
    - 커뮤니케이션 도구로 카카오톡과 디스코드를 사용하는 것이 전부였기에 커뮤니케이션에서 어려움이 있었다.
    - API를 통해 데이터를 가져올 때 에러코드에 따른 예외 처리를 진행하지 못 했던 점이 아쉬웠다.
    - 비밀번호를 salt값과 함께 해싱해서 DB에 저장하는 방법을 구현하는 방법을 시도하지 못 했던 점이 아쉬웠다.
