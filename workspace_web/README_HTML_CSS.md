22년 10월 TIL 요약본 및 index

day 09 Jupyter 연습파일 repository 생성후 복습



---

day10

HTML HyperText Markup Langage

- 정의
  - HyperText Markup Langage로
  - 데이터를 태그로 구조화시키는 언어
- <tag> 사이에 내용을 태그라고 한다
- 블록 요소
- 인라인 요소
- f12 개발자 도구
- 주석 <!---->
- a 링크 만드는 태그
- 이미지 
  - 이미지에 링크걸기
  - 이미지 맵 사용해서 이미지에 특정 부분에 링크 걸기
- div는 레이아웃을 나눌 때 쓰는 태그

# HTML

1. start
2. title
   1. 글자 크기 지
   2. style 지정
   3. div / p 구간 나누기
3. text
   1. 진하게 강조 첨자 내용추가/삭제
4. img
   1. 이미지 불러오기
   2. 이미지 링크걸기(부분만 가능)
5. anchor
   1. a와 id 를 통해 원하는 줄로 이동
6. list
   1. 순차적 / 비순차적 / 정의형 목록
      1.  순차적 : <ol> <il>
      2. 비순차적 : <ul> <il>
      3. 정의 : <dl> 시작<dt>제목<dd>
7. table
   1. table에도 head body foot이 존재
   2. rowspan="2" 로 2개 열 또는 행(colspan="2")을 병합가능
8. layout
9. layout2
10. form
    1. form을 통해 frame 제작
    2. legend를 통해  frame 제목 만들기
    3. id pw type을 잘 지정해서 입력받기
    4. name=이 key의 역할 value= 값
       1. 위의 키와 값을 action으로 전
       2. 수신 여부 등을 할 때에는 name을 같게 해서 하나만 선택되도록
    5. input=checkbox는 여러 개 선택할 수 있다.
    6. textarea는 string을 입력받을 수 있는 상자 제공
    7. 버튼은 button , reset , submit 으로 여러 기능을  사용 가능
11. selectbox
    1. 선택할 수 있는 box 생성
    2. optgroup을 사용해서 목록을 지정할 수 있다
    3. option을 통해서 선택할 내용을 적는다

12. index
    1. a를 사용해서 각 html 예제를 모아서 볼 수있다 

#  CSS (10/5)

1. basic

   - style p { } : 모든 p태그 안에 적용

   - 경로 지정

     - ```html
        <link rel="stylesheet" href="./css/css01.css">
       ```

   - 스타일시트 3종료

     - 인라인 스타일시트
     - 내부 스타일시트
     - 외부 스타일시트

2. selector-prac

   - #s-id01 {} : s-id01를 찾는다는 의미

   - .class {} : 클래스는.을 붙혀서 찾는다 c

   - ```css
     * { }
     ```

     -  전체는 * 로 한다 

   - 자식  #atc > p {}

     1. article id가 atc인 경우에 그 하위 p 에는 적용이 되지만  div 안에 있는 p에는 적용이 되지 않는다

   - 속성 선택자

     - ```html
               <p title="a">속성이 정의된</p>
               <p title="b">태그만 선택</p>
               <p>속성 없음</p>
               p[title]{ }
       ```

     - p[title]{ } 로 선택하면된다

   - tag + tag 옆애 있는애 선택

   - 가상 클래스

     - ```
       a:link{
           color: green;
           font-size: 20px;
       }
       a:visited{
           color: hotpink;
       }
       /* 마우스 올려놨을때 색 바뀜 */
       a:hover{
           background-color: darkmagenta;
           color: yellowgreen;
       }
       /* 클릭하는 순간 */
       a:active{
           background-color: black;
           color: yellow;
       }
       input:checked{
           width: 100px;
           height: 100px;
       }
       ```

     - 링크 색 / 이미 방문했을 때 / 마우스를 올려놓았을 때 / 클릭하는 순간 / 체그했을 때(체크버튼)

3. font

   - 특정 요소만 지정하기 
     - div > h1 { } div아래 h1을 선택해서 스타일 지정
   - font 등록
     - @font-face{ }
     - src : url("./fonts/cat_ttf/Goyang.ttf") format("truetype");

4. box 만들기

   - style을 지정할 때 태그를 여러 개 선택할 수 있다
   - ,box를 통해 틀을 만든다
   - .line{} 박스의 하단 테두리 지정

5. 글 사이에 이미지 넣기

   - img src="이미지 주소"
   - float = left, right를 지정하면 그 쪽으로 이미지/속성이 이동한다

6. clear

   - float = left, right를 지정하면 지정하지 않은 글은 밀려서 써지는데 그 영향을 받지 않게 해 준다

7. display

   - display를 inline으로 지정하면 가로로 정렬된다

8. overflow

   - 내용이 넘치면 overflow된다
   - hidden,scroll을 지정하여 보완할 수 있다

9. position

   - 위치가 어떻게 지정되는지
   - z축이 있어서 어떤 게 먼저 보이는지 주의해야한다
   - relative는 박스 왼쪽위가 기준이다
   - absolute는 현재 위치 기준
   - fixed는 브라우저에 위치가 고정되어있다

10. border

    - border-radius 끝을 깎아내는 느낌 원을 만드는 데 사용할 수 있다

11. transform

    - 변형 / 이동이 가능하다
    - translate 위치 이동
    - rotate 회전
    - scale 크기 변화
    - skew 비트는 느낌 (대각선으로 당긴느낌/앞뒤로 이동)
    -  transition 이
      - 이
