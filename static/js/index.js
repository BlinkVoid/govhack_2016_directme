function init() {
    // Init checkboxes
    $('.ui.checkbox')
    .checkbox();
}

window.onload=init;

function initGoogleMaps() {
    autocompleteLocations();
}

function autocompleteLocations() {
    var input1 = /** @type {!HTMLInputElement} */(
        document.getElementById('locationstart'));
    var input2 = /** @type {!HTMLInputElement} */(
        document.getElementById('locationend'));
    var types = document.getElementById('type-selector');
    var autocomplete_start = new google.maps.places.Autocomplete(input1);
    var autocomplete_end = new google.maps.places.Autocomplete(input2);
}
