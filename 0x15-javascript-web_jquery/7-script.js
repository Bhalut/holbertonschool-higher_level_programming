var swapiAPI = "https://swapi-api.hbtn.io/api/people/5/?format=json";
$.getJSON(swapiAPI).done(function (data) {
  $("DIV#character").text(data.name);
});
