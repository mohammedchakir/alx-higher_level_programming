(document).ready(function () {
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (e) {
    if (e.keyCode === 13) {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
