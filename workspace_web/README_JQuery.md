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


10. class 
    1. 클래스를 on/off해서 css를 변화시키키
11. insert 내부 추가
    1. //$("<p>") 는 document.createElement(p)과 동일
    2. prepend / append
       1. $("div").prepend($("<p>").addClass("prepend").text("prepend")); 자식요소중 가장 처
       2. $("div").append($("<p>").addClass("append").text("append")); 자식요소 중 가장 마지막
    3. html / text
       1. $("div").html("<b>html요소를 변경</b>") 두껍게 처리됨(innerHTML) 태그가 사용됨
       2. $("div").text("<b>text요소를 변경</b>") 문자열로 b가 들어간다(textContent)
12. insert 외부 추가
    1. [after](https://api.jquery.com/after/#after-content-content) / insertAfter
       1. afer **Description:** *Insert content, specified by the parameter, after each element in the set of matched elements.*
          1. .after( content [, content ] )
          2. Type: htmlString or Element or Text or Array or jQuery
          3. .after( function )
       2. insertAfter  
          1. taget :  Type: Selector or htmlString or Element or Array or jQuery
          2. 타겟이 앞에 있는지 뒤에 있는지의 차이





​	

