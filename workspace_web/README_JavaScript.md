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
       3. for문 역할
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

          4. delrow 함수
             1. var delTr = ele.parentNode.parentNode; 
             2. 삭제 버튼이 td안에 있으므로 row전체를 삭제하기 위해서는 tr을 삭제해야 하기 때문에 상위의 상위까지 삭제해야 한다

          5. 전체 삭제 버튼
             1. deleteVal
             2. hasChildNodes를 사용해서
             3. tbody 내의 값이 존재하지 않아야 false가 되기 때문에 while문으로 전부 제거해준다







중요 포인트

- 함수가 값으로 사용된다.
- 



