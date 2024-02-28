(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('<li>').text(movie.title).appendTo('#list_movies');
      });
    },
    error: function (xhr, status, error) {
      console.error('Error fetching movies:', error);
    }
  });
});
