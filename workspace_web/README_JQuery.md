jQuery is a fast, small, and feature-rich JavaScript library

library,module : 기능을 구현하는 코드(함수) 모음 

1. basic
   1. jq-min 가져오기 
   2. 새로운 script에 jq로 클릭시 이벤트 발생 function 
   3. .css()
      1. .css( propertyName ) :get
      2. .css( propertyName , value) : set

2. selector
   1. 

3. input

4. checkbox

5. dom1

6. dom2

7. dom3

8. dom4

9. event 이벤트 발생

   1. 클릭 이벤트가 발생하면 a태그는 요청한다

   2. 요청 전에 함수 먼저 실행하고 이동한다

   3. 이벤트 전파

      1. 이벤트 전파 : 각 요소가 서포 포함관계(중첩)인 경우, 요소 중 하나에 이벤트가 발생되면 

         ​             중첩된 요소들도 이벤트가 전파된다

      2. stopPropagation() : 이벤트 요소의 전파 막기

      3. preventDefalt() : 이벤트에 의한 기본 동작 막기         

      4. return false : 둘 다 막기

   4. bind() 두 가지 방법

      1. **Description:** *Attach a handler to an event for the elements.*

      2. #### .bind( eventType [, eventData \] [, preventBubble ] )

      3. #### .bind( events )

      4. unbind를 사용해 bind했던 것을 풀 수 있다

   5. addEventListener

   6. on을 사용해서 이벤트를 엮는다

   7. body 에 새로 생성된 p에서도 클릭 이벤트를 연결해보기

      1.  $("body").on("click","p",function(){alert("new p!")});

10. accodian

11. class 

    1. 클래스를 on/off해서 css를 변화시키키

12. insert 내부 추가

    1. //$("<p>") 는 document.createElement(p)과 동일
    2. prepend / append
       1. $("div").prepend($("<p>").addClass("prepend").text("prepend")); 자식요소중 가장 처
       2. $("div").append($("<p>").addClass("append").text("append")); 자식요소 중 가장 마지막
    3. html / text
       1. $("div").html("<b>html요소를 변경</b>") 두껍게 처리됨(innerHTML) 태그가 사용됨
       2. $("div").text("<b>text요소를 변경</b>") 문자열로 b가 들어간다(textContent)

13. insert 외부 추가

    1. [after](https://api.jquery.com/after/#after-content-content) / insertAfter
       1. afer **Description:** *Insert content, specified by the parameter, after each element in the set of matched elements.*
          1. .after( content [, content ] )
          2. Type: htmlString or Element or Text or Array or jQuery
          3. .after( function )
       2. insertAfter  
          1. taget :  Type: Selector or htmlString or Element or Array or jQuery
          2. 타겟이 앞에 있는지 뒤에 있는지의 차이

14. replace

15. slotmachine

    1. 기본원리
       1. 클래스를 만들고 클래스의 첫번째 요소를 div에 마지막에 insert한다 
          1. $(".active").first().appendTo(div);

       2. 원래 문서에 있었던 요소를 다시 삽입하면 이동하기 때문에 반복해주면 계속해서 바뀐다
       3. toggleClass를 사용해서 클래스를 생성하고 지우기를 반복한다
       4. 이 때 setInterval를 사용해서 계속해서 생성하고 지우도록 된다
       5. 버튼은 처음에 start라고 쓰여 있다
       6. 버튼을 누르면 start가 stop으로 바뀐다
       7. stop 버튼을 누르면 현재 위치eq(2)에 이미지의 alt값을 alert하고 버튼을 다시 start로 바꾼다

    2. setInterval : 일정 시간동안 함수를 반복시키는 함수
    3. .first() : 첫번째 요소
    4. .appendTo(div); : 자식 요소 가장 마지막에 insert한다
    5. toggleClass("active"); : 버튼을 누를때마다 active클래스를 지우거나 만든다

16. menu

    1. 클래스를 만들어서 div로 감싸기
    2. ![image-20221013152452001](../../images/README_JQuery/image-20221013152452001.png)
    3. 다른 곳을 클릭했을 때는 부모의 box클래스가 없는지를 확인해서 unwrap한다
    4. 전부 upwrap되면 기존 클릭했던 메뉴가 wrap된다
    5. wrapInner을 사용하면 안쪽으로 들어간다
    6. $("a").wrapAll("<b></b>");
       1. b태그안에 a태그를 전부 넣는다

17. delete 삭제 : 엘리먼트 제거하기

    1. remove : 선택된 객체가 지워진다
    2. detach : 복사 붙혀넣기
       1. .append(detach 변수)하면 없어지고 바뀐다

    3. empty : 선택된 객체의 자식이 지워진다

18. ajax01

    1. 언제

       1. 비동기통신 클라이언트가 서버에 요청했을 때 
       2. 특정 데이터 부분만 바꾸고 싶을 때

    2. $.ajax()

       1. url: "emplist.xml",     // 요청할 주소

       2. method: "get",          // 요청 방식

       3. data : {"key":"value"}    // 요청하면서 함께 보내는 데이터(보낼 데이터가 있다면)

       4. dataType: "xml",         // 응답받는 데이터 타입

       5. success: function(data){ }    // 비동기 통신이 성공했을 때

       6. error: function(request, error){ // 비동기 통신이 실패했을 때

       7. ```
          // 전체에서EMPLOYEE_ID를 찾아서 (empid:입력값)를 가지고 있다면 그 부모를 선택
          if((empInfo).is("ROW")){
          	$("table input").each(function(i){
          		$(this).val($(empInfo).children().eq(i).text());
          	})
          } else {
          	alert("검색대상이 존재하지 않음")
          }
          ```

       8. 

19. ajax02

    1. 사원 전체 데이터 가져오기
    2. 비동기통신을 성공했을 때 가져오는 데이터(empRowList)를 makeTable 함수에 전달한다
    3. makeTable 함수
       1. 맨 위 이름 가져오기
          1. elem.eq(0).children().length은 ROW안의 값들이 몇 개 들어있는지 확인한다
          2. elem.eq(0).children().eq(j).prop("tagName")은 tagName의 속성값을 가져온다
          3. 값을 td에 각각 넣고 다시 tr에 넣는다

       2. 값 가져오기
          1. elem.eq(i).children().length 은 i번째 Row의 자식의 길이를 리턴한다
          2. elem.eq(i).children().eq(j).text()은 Row 안에 j번째 값을 리턴한다
          3. 위의 값을 다시 td에 넣고 tr에 전달한후 테이블에 전달 후 리턴








​	

