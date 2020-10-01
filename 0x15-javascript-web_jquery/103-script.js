var fourtonfish = "https://www.fourtonfish.com/hellosalut/";

$(document).ready(() => {
  $("INPUT#language_code").keypress((e) => {
    if (e.keyCode === 13) {
      $("INPUT#btn_translate").click();
    }
  });
  $("INPUT#btn_translate").click(() => {
    var value = $("INPUT#language_code").first().val();
    $.getJSON(`${fourtonfish}?lang=${value}`).done((data) =>
      $("DIV#hello").text(data.hello).show()
    );
  });
});
