22년 10월 6일 

---

# JavaScript

1. basic
   - script 사이에 적는다
   - 기본문법
     - inline 작성방식
     - 내부 작성 방식
     - 외부 작성 방식
2. var 변수
   - var01 함수
     - variable += 5
     - getElementById("value01") 찾아서 배경 노랑 글자 빨강의 variable 변수 출력 

   - val02 함수
     - innerVal 변수에 variable +10 저장
     - getElementById("value01") 찾아서 배경 노랑 글자 빨강의 innerVal 변수 출력

   - jsType 함수 
     - string type 변수 inferVal 선언
     - 타입 확인 
       - 문자 / 숫자 / true / null / 객체(Object object )/function
       - string / number / boolean / object / Object object /function



15. check
    1. 버튼 체크헀을 때 그 색이 칠해지도록 하기
    2. 전체선택 했을때 모든 체크박스를 체크
       1. 모든 chk를 전부 가져와서 checked의 속성 바꾸기
    3. 선택된 체크박스가 가리키는 박스의 색 바꾸기
       1. 체크되어있으면 value값을 가져와서 색을 바꿈
       2. 체크되어있지 않으면 value 값을 가져와서 색을 빈 값으로 지정
    4. clear 버튼으로는 모든 체크박스와 색을 제거
    5. 모든 체크박스가 체크되어있아야지 모두에 체크되도록

16. dom01
    1. 이미지 파일을 불러와서 클릭할때마다 이미지 경로 바꾸기
    2. 이미지 n개 와 왼쪽 화살표 오른쪽 화살표 이미지 가져오기
    3. 왼쪽 화살표 이미지를 클릭하면 img0n 의 이름이 적은 이미지가 출력되도록

17. dom02
    1. 자식태그의 tagName인 p를 찾아서 부모를 탐색하면 div가 나오는 것을 확인할 수 있다(대문자로 나옮)
    2. 부모태그를 찾아서 childNode를 탐색하면 배열로 출력된다
       1. 부모태그를 찾을 때 (getElementsByTagName) 한 개만 있어도 이것도 배열로 나옮으로 주의해야 한다
    3. childNodes

18. dom03
    1. html 상에 없는 문서를 javascript로 생성하기
    2. 첫번쨰 방법
       1. createElement("div")를 사용하면 div 에 들어간다
       2.  var attr = document.createAttribute("style") 속성요소를 만들어준다
       3. div.appendChild(txt); 를 통해 txt 전달 / 자식요소로 넣어준다
       4. document.body.appendChild(div); 로 body에 전달
    3. 두번째 방법
       1. var attr = document.createAttribute를 만들지 않는다
          1. Attributenode를 만들지 않고 div바에 넣어준다
       2. div.setAttribute("style", "border: 2px solid red")
       3. setAttribute로 한번에 한다

19. dom04

    1. 정해진 공간에 이미지를 생성하고 삭제하기

    2. getElementsByName으로 name 들을 불러온다

    3. 경로와 value값을 더해서 총 경로를 만들어준다
       1. radioVal = "resources/imgs/"+radios[i].value;

    4. 이미지 태그를 생성한다
       1. var img = document.createElement("img");
       2. img.setAttribute("src", radioVal);

    5. 코드 의미 찾아보기 
       1. var div = document.getElementById("imgView");

       2.  var chd = document.querySelector("#imgView > img");

       3.  div.replaceChild(img,chd);

20. dom05

    1. a를 사용해서 이미지 변경
       1. Uncaught TypeError: Cannot set properties of undefined
       2. body가 없기 때문에 발생하는 에러 onload를 사용해준다

    2. alt를 사용해서 
    3. getAttribute
    4. setAttribute

21. dom06

    1. appendChild 자식요소 중 마지막에 붙여넣는다
    2. move
       1. document.querySelector("fieldset").children[1];이므로 
       2. fieldset의 두번쨰이므로 legend를 제외한 첫번째를 이동한다

22. dom07

    1. tableVal() 함수 실행

       1. 첫번째 form을 가져와서 doc에 저장한다

       2. id , pw , addr , phone 의 value값을 vals에 저장한다

       3. for문 역할 : 유효성 검사

          1. 전부 입력해야지 다음 단계로 갈 수 있도록 지정

       4. 테이블에 값을 전달한다

          1. vals값들을 createRow함수에 전달한다

          2. createRow

             1. tr을 생성한다
             2. td를 vals길이만큼 생성한다
             3. textContent = vals[i] 생성된 td안에 vals값들을 넣는다
             4. tr에 td추가

          3. 삭제 버튼 추가

             1. td값을 dTd에 추가한다
             2.  삭제 버튼을 만들기 input type = 'button' value='삭제' onclick='delRow(this)'
             3. 삭제 버튼을 tr에 추가한다
             4. tr 리턴한다
             5. document.getElementById("addtr").appendChild(tr) 에 전달된다

             

          4. delrow 함수

             1. var delTr = ele.parentNode.parentNode; 
             2. 삭제 버튼이 td안에 있으므로 row전체를 삭제하기 위해서는 tr을 삭제해야 하기 때문에 상위의 상위까지 삭제해야 한다

          5. 전체 삭제 버튼

             1. deleteVal
             2. hasChildNodes를 사용해서
             3. tbody 내의 값이 존재하지 않아야 false가 되기 때문에 while문으로 전부 제거해준다

23. ajax(Asynchronous Javascript And Xml) 비동기 요청

    1. 동기 통신 / 비동기 통신
       1. 동기 : 요청 후 기다림
       2. 비동기 : 요청 후 할일 함
          1. 주소표시창이 변하지 않는다 (다시그리지 않는다)

    2. XML(eXtensible Markup Language)
       1. 간단하게 태그를 만들어서 확장한 언어

    3. 비동기 통신 emplist.xml 과 하기
       1. XMLHttpRequest : javascript object, http를 통한 데이터 송수신 지원
       2. onreadystatechange
          1. readystate가 바뀔때마다(change) 함수 호출

       3. readystate
          1. 0 : uninitallized - 실행되지 않음
          2. 1 : loading - 로딩중
          3.  2 : loaded - 로딩 완료
          4.  3 : interactive - 통신됨
          5.  4 : complete - 통신 완료 (클라이언트와 서버가 서로 연결됨)
       4. status
          1. 200 : 성공
          2. 400 : bad request
          3. 401 : anauthorized
          4. 403 : forbidden
          5. 404 : not found (경로 잘못 요청)
          6. 500 : internal server error 

       5. send 
          1. form action = "경로" method = "방식"
          2. input type = "submit"
          3. /form 과 동일하다
          4.  xhr.open("GET", "emplist.xml");
          5.  xhr.send();

       6. xhr.onreadystatechange = function(){
          1. xhr.readyState == 4 통신이 되었을 때
          2. xhr.status == 200 status도 정상이면 xhr.responseText 출력
             1. responseText 응답된 데이터 텍스트

          3. 정상이 아니면 status 출력

       7. 정상적으로 통신되면 응답받은 xml객체를 table에 넣기
          1. var respXML = xhr.responseXML;
          2. var table = document.getElementById("tb"); 테이블 가져오기
          3. var rows = respXML.getElementsByTagName("ROW");
             1. 각각의 ROW가 들어있는 nodelist를 가져오기
          4. nodename 가져오기
             1. tr 생성 th 생
             2. rows[0].children[i].nodeName 가져와서 append한다
          5. textContent 가져오기
             1. tr 생성 td 생성
             2. rows[i].children[j].textContent 가져와서 append한




















중요 포인트

- 함수가 값으로 사용된다.
- 



