$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (resp, status) {
    if (status === 'success') {
      let films = resp.results;
      for (let i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
i});
