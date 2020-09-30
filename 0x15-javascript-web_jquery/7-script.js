var swapiAPI = "https://swapi-api.hbtn.io/api/people/5/?format=json";
$.getJSON(swapiAPI).done((data) => {
  $("DIV#character").text(data.name);
});
