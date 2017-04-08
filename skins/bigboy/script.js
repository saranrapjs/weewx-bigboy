var sets = document.querySelectorAll('.images-set');
var clickers = document.querySelectorAll('.images-selector > a');

function select(selectedPeriod) {
	for (var i = 0; i < sets.length; i++) {
		var el = sets[i];
		var clicker = clickers[i];
		var period = el.getAttribute('data-period');
		if (period === selectedPeriod) {
			el.classList.add('period-selected');
			clicker.classList.add('period-selected');
		} else {
			el.classList.remove('period-selected');
			clicker.classList.remove('period-selected');
		}
	}
}

for (var i = 0; i < clickers.length; i++) {
	clickers[i].addEventListener('click', function() {
		select(this.textContent.toLowerCase());
	});
}

select('day');