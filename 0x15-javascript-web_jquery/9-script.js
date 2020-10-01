var fourtonfish = "https://fourtonfish.com/hellosalut/?lang=fr";
$.getJSON(fourtonfish).done((data) => $("DIV#hello").text(data.hello));
