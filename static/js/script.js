// Show By Scrolling
window.addEventListener("scroll", rv);

function rv() {
	var x = document.querySelectorAll(".rv");
	for (var i = 0; i < x.length; i++) {
		var windowheight = window.innerHeight;
		var rvl = x[i].getBoundingClientRect().top;
		var rvPo = 170;
		// console.log(rvl);
		if (rvl < windowheight - rvPo) {
			x[i].classList.add("act");
		} else {
			x[i].classList.remove("act");
		}
	}
}
document.body.style.display = "none";
