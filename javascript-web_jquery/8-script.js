/* global $ */
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (const film of data.results) {
    $('#list_movies').append($('<li>').text(film.title));
  }
});
