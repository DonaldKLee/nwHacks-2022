function countdown() {
	minutes = document.getElementById("minutes").innerHTML
	seconds = document.getElementById("seconds").innerHTML

	if (seconds <= 00) {
		document.getElementById("minutes").innerHTML -= 1; 
		document.getElementById("seconds").innerHTML = 59;
	}
	document.getElementById("seconds").innerHTML -= 1;
}

function start_timer() {
	setInterval(countdown,1000);
}