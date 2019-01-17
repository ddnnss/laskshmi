function sort_filter(var1,filter,subcat) {
    console.log(var1,filter,subcat);

    setGetParam('filter',filter);
    setGetParam('subcat',subcat);

    function setGetParam(key,value) {
  if (history.pushState) {
    var params = new URLSearchParams(window.location.search);
    params.set(key, value);
    var newUrl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?' + params.toString();

    window.history.pushState({path:newUrl},'',newUrl);
  }
}

      var data = {};

        var url ='/cart/sort_filter?' + location.href.split('?')[1];
        console.log(data);
        $.ajax({
            url:url,
            type:'GET',
            data: data,
            cache:true,
            success: function (data) {
                console.log('OK');

            },
            error: function () {
                console.log('ERROR')
            }
        })

}