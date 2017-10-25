document.addEventListener("DOMContentLoaded", function(event) {

});

function buttonclick(){
	var mytextbox = document.getElementById("mytextbox");
	var myheader = document.getElementById("myheader");
	var input = mytextbox.value;
	myheader.innerHTML = input;
}

function explainationclick(){
	var mybutton = document.getElementById("wantanexplaination");
	var myexplaination1 = document.getElementById("explaination1");
	var myexplaination2 = document.getElementById("explaination2");
	if (mybutton.innerHTML == "Explaination hidden"){
		mybutton.innerHTML = "Explaination visible";
		myexplaination1.innerHTML = "Contributors: John M. Letey (John.Letey@colorado.edu) and David A. Knox (David.Knox@colorado.edu).";
		myexplaination2.innerHTML = ""
	}
	else{
		mybutton.innerHTML = "Explaination hidden";
		myexplaination1.innerHTML = "";
	}
}