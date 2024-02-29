$(document).ready(function () {
  $.$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $('UL#list_movies').prepend(data.title);
    });
});
