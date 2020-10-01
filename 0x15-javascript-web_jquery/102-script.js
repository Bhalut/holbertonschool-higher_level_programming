var fourtonfish = "https://www.fourtonfish.com/hellosalut/";

$(document).ready(() => {
  $("INPUT#btn_translate").on("click", () => {
    var value = $("INPUT#language_code").first().val();
    $.getJSON(`${fourtonfish}?lang=${value}`).done((data) =>
      $("DIV#hello").text(data.hello).show()
    );
  });
});
