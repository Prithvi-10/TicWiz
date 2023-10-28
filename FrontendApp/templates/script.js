let selectedSeats = [];

// Function to handle seat selection
function selectSeat(seatElement) {
    seatElement.classList.toggle('selected');
    const seat = seatElement.getAttribute('data-seat');

    if (selectedSeats.includes(seat)) {
        selectedSeats = selectedSeats.filter(s => s !== seat);
    } else {
        selectedSeats.push(seat);
    }

    document.getElementById('selected-seats').value = selectedSeats.join(',');
}

// Add click event listeners to seat options
const seatOptions = document.querySelectorAll('.seat');
seatOptions.forEach(seatOption => {
    seatOption.addEventListener('click', () => selectSeat(seatOption));
});