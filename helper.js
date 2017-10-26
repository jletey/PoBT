document.addEventListener("DOMContentLoaded", function(event) {

});

function buttonClick(){
	let mytextbox = document.getElementById("mytextbox");
	let myheader = document.getElementById("myheader");
	let input = mytextbox.value;
	myheader.innerHTML = input;
}

function explanationClick(){
	let mybutton = document.getElementById("wantanexplanation");
	let myexplanation0 = document.getElementById("explanation0");
	let myexplanation1 = document.getElementById("explanation1");
	let myexplanation2 = document.getElementById("explanation2");
	let myexplanation3 = document.getElementById("explanation3");
	let myexplanation4 = document.getElementById("explanation4");
	let myexplanation5 = document.getElementById("explanation5");
	let myexplanation6 = document.getElementById("explanation6");
	let myexplanation7 = document.getElementById("explanation7");
	let myexplanation8 = document.getElementById("explanation8");
	let myexplanation9 = document.getElementById("explanation9");
	let myexplanation10 = document.getElementById("explanation10");
	if (mybutton.innerHTML == "Explanation is hidden"){
		mybutton.innerHTML = "Explanation is visible";
		myexplanation0.style.display = 'block';
		myexplanation1.style.display = 'block';
		myexplanation2.style.display = 'block';
		myexplanation3.style.display = 'block';
		myexplanation4.style.display = 'block';
		myexplanation5.style.display = 'block';
		myexplanation6.style.display = 'block';
		myexplanation7.style.display = 'block';
		myexplanation8.style.display = 'block';
		myexplanation9.style.display = 'block';
		myexplanation10.style.display = 'block';
	}
	else{
		mybutton.innerHTML = "Explanation is hidden";
		myexplanation0.style.display = 'none';
		myexplanation1.style.display = 'none';
		myexplanation2.style.display = 'none';
		myexplanation3.style.display = 'none';
		myexplanation4.style.display = 'none';
		myexplanation5.style.display = 'none';
		myexplanation6.style.display = 'none';
		myexplanation7.style.display = 'none';
		myexplanation8.style.display = 'none';
		myexplanation9.style.display = 'none';
		myexplanation10.style.display = 'none';
	}
}

function fastaFilenameClick(){
	let input = document.getElementById("fastaFile");
	console.log(input.value);
	//let fileID = open(input.value);
}