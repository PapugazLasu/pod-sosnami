
$('#search-form').on('submit', function(e) {
  e.preventDefault();
  $.ajax({
    url: '/search/',
    method: 'GET',
    data: {search: $('#search-text').val()},
    success: function(json){
      //alert(JSON.stringify(json))
      var element = $('#result-list');
      element.empty()
      for (var i = 0, l = json.results.length; i < l; i++ ){
        element.append('<li class="list-group-item">' + '<a href="' + json.results[i].link +'">' + json.results[i].name + '</a></li>')
      }
    }
  })
})
