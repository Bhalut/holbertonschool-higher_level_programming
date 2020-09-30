var swapiAPI = "https://swapi-api.hbtn.io/api/films/?format=json";
$.getJSON(swapiAPI).done(function (data) {
  $.each(data.results, function (x, dat) {
    $("UL#list_movies").append(`<li>${dat.title}</li>`);
  });
});
