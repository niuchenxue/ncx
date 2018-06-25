
function ajaxToGetData() {
	url = "/s";
	var postParam ="userName=" + document.getElementById("uid").value + "&postclass=" + document.getElementById("area").value;
	var ajax = false;
	console.log(postParam);
	//开始初始化XMLHttpRequest对象
	if (window.XMLHttpRequest) { //Mozilla 浏览器
		ajax = new XMLHttpRequest();
		if (ajax.overrideMimeType) { //设置MiME类别
			ajax.overrideMimeType("text/xml");
		}
	} 
	else if (window.ActiveXObject) { // IE浏览器
		try {
			ajax = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				ajax = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
			}
		}
	}
	if (!ajax) { // 异常，创建对象实例失败
		window.alert("不能创建XMLHttpRequest对象实例.");
		return false;
	}
	//通过Post方式打开连接
	ajax.open("POST", url, true);
	//定义传输的文件HTTP头信息
	ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	//发送POST数据
	ajax.send(postParam);
	//获取执行状态
	ajax.onreadystatechange = function() {
		//如果执行状态成功，那么就把返回信息写到指定的层里
		if (ajax.readyState == 4 && ajax.status == 200) {
			var jsonList = eval(ajax.responseText); //Yolanda
			console.log(jsonList.length);
			
			var div = document.getElementById("breakNewsList1");
			while(div.hasChildNodes()) //当div下还存在子节点时 循环继续
			    {
			        div.removeChild(div.firstChild);
			    }
			for(var i = 0; i < jsonList.length; i++){
				
				var li = document.createElement("li");
				li.id = ("li-" + i);
				var str = jsonList[i].TiteName;
				var str1 = jsonList[i].Urll;
				var str2 = jsonList[i].authorName;
				var str3 = jsonList[i].bookAbstract;
				

				console.log(str)
				li.innerHTML = "<a href='"+str1+"' target='_blank'>"+str+"</a>"+","+str2+'\r'+"abstact:"+str3;

				
				document.getElementById("breakNewsList1").appendChild(li);
			}
	 	}
	}
}