function filetest(){
    window.alert("외부 js file에서 실행됨!");
}

// 인터프리터  
// 컴파일러 
window.onload=function(){
    //가장 마지막에 호출됨
    alert("윈도우가 로딩 된 이후 호출");    
}