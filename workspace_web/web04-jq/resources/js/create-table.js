function makeTable(elem){
	// elem = empRowList
	var $table = $("<table border=1>");
	
	for(var i =0; i<1;i++){
		var $tr=$("<tr>");
		

		//맨 위 이름 가져오기
		for(var j=0; j<elem.eq(0).children().length;j++){
			//elem.eq(0).children()
			//S.fn.init(5) [EMPLOYEE_ID, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, prevObject: S.fn.init(1)]
			//elem.eq(0).children().length = 5 그러므로  j=5

			var $td=$("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
			//elem.eq(0).children().eq(0).prop("tagName") = EMPLOYEE_ID
			//elem.eq(0).children().eq(1).prop("tagName") = LAST_NAME		

			$tr.append($td);
		}
		$table.append($tr);
	}
	
	// 값 가져오기	
	for(var i =0; i<elem.length;i++){
		//elem.length = 107개 ROW를 가지고 있음
		var $tr=$("<tr>");
		for(var j=0; j<elem.eq(i).children().length;j++){
			//elem.eq(i).children().length = 5 
			var $td=$("<td>").append(elem.eq(i).children().eq(j).text());
			$tr.append($td);
		}		
		$table.append($tr);
	}
	for (var j =0; j<5; j++){
		console.log(elem.eq(0).children().eq(j).text())
		/*
		100
		King
		SKING
		515.123.4567
		1987. 6. 17 오전 12:00:00
		*/	
	}
	return $table;
}
