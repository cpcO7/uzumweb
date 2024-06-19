document.getElementById('showCities').addEventListener('click', function() {
    let citySelector = document.querySelector('.city-selector');
    citySelector.classList.remove('hidden');
    setTimeout(function() {
        citySelector.classList.add('show');
    }, 10);
});

document.body.addEventListener('click', function(event) {
    let citySelector = document.querySelector('.city-selector');
    if (!citySelector.contains(event.target) && !document.getElementById('showCities').contains(event.target)) {
        citySelector.classList.remove('show');
        setTimeout(function() {
            citySelector.classList.add('hidden');
        }, 500);
    }
});
