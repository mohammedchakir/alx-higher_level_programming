(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: function (xhr, status, error) {
      console.error('Error fetching translation:', error);
    }
  });
});
