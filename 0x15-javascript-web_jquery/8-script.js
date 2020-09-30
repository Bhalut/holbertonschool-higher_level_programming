var swapiAPI = "https://swapi-api.hbtn.io/api/films/?format=json";
$.getJSON(swapiAPI).done((data) => {
  $.each(data.results, (x, dat) => {
    $("UL#list_movies").append(`<li>${dat.title}</li>`);
  });
});
