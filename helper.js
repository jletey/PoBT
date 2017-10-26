document.addEventListener("DOMContentLoaded", function(event) {

});

function buttonClick(){
	var mytextbox = document.getElementById("mytextbox");
	var myheader = document.getElementById("myheader");
	var input = mytextbox.value;
	myheader.innerHTML = input;
}

function explainationClick(){
	var mybutton = document.getElementById("wantanexplaination");
	var myexplaination0 = document.getElementById("explaination0");
	var myexplaination1 = document.getElementById("explaination1");
	var myexplaination2 = document.getElementById("explaination2");
	var myexplaination3 = document.getElementById("explaination3");
	var myexplaination4 = document.getElementById("explaination4");
	var myexplaination5 = document.getElementById("explaination5");
	var myexplaination6 = document.getElementById("explaination6");
	var myexplaination7 = document.getElementById("explaination7");
	var myexplaination8 = document.getElementById("explaination8");
	var myexplaination9 = document.getElementById("explaination9");
	var myexplaination10 = document.getElementById("explaination10");
	if (mybutton.innerHTML == "Explaination is hidden"){
		mybutton.innerHTML = "Explaination is visible";
		myexplaination0.style.display = 'block';
		myexplaination1.style.display = 'block';
		myexplaination2.style.display = 'block';
		myexplaination3.style.display = 'block';
		myexplaination4.style.display = 'block';
		myexplaination5.style.display = 'block';
		myexplaination6.style.display = 'block';
		myexplaination7.style.display = 'block';
		myexplaination8.style.display = 'block';
		myexplaination9.style.display = 'block';
		myexplaination10.style.display = 'block';
	}
	else{
		mybutton.innerHTML = "Explaination is hidden";
		myexplaination0.style.display = 'none';
		myexplaination1.style.display = 'none';
		myexplaination2.style.display = 'none';
		myexplaination3.style.display = 'none';
		myexplaination4.style.display = 'none';
		myexplaination5.style.display = 'none';
		myexplaination6.style.display = 'none';
		myexplaination7.style.display = 'none';
		myexplaination8.style.display = 'none';
		myexplaination9.style.display = 'none';
		myexplaination10.style.display = 'none';
	}
}

function fastaFilenameClick(){
	var input = document.getElementById("fastaFile");
	var fileID = open(input.value);
}