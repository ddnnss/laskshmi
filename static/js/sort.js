var last_filter = '';
var last_order = '';
var last_search = '';
function setGetParam(key,value) {
        if (history.pushState) {
            var params = new URLSearchParams(window.location.search);
            params.set(key, value);
            var newUrl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?' + params.toString();

            window.history.pushState({path:newUrl},'',newUrl);
        }
    }

function removeParam(parameter)
{
  var url=document.location.href;
  var urlparts= url.split('?');

 if (urlparts.length>=2)
 {
  var urlBase=urlparts.shift();
  var queryString=urlparts.join("?");

  var prefix = encodeURIComponent(parameter)+'=';
  var pars = queryString.split(/[&;]/g);
  for (var i= pars.length; i-->0;)
      if (pars[i].lastIndexOf(prefix, 0)!==-1)
          pars.splice(i, 1);
  url = urlBase+'?'+pars.join('&');
  window.history.pushState('',document.title,url); // added this line to push the new url directly to url bar .

}
return url;
}

function filter(filter,subcat) {

    console.log(filter,subcat);
    if (last_filter == filter){
        console.log('filter used');
    }
    else{
        if ($('#search_string').val()){
            console.log('search not empty');
        }
        else {
            console.log('search empty');
            removeParam("search");

        }
        setGetParam('filter',filter);
        last_filter = filter;

      // var data = {};

        var url =location.href.split('?')[1];

        window.location.href = '?'+url;
        // console.log(data);
        // $.ajax({
        //     url:url,
        //     type:'GET',
        //     data: data,
        //     cache:true,
        //     success: function (data) {
        //         console.log('OK');
        //
        //     },
        //     error: function () {
        //         console.log('ERROR')
        //     }
        // })

    }

}

function order(order,subcat) {
     if (last_order == order){
        console.log('order used');
    }
    else{
       console.log(order,subcat);
       setGetParam('order',order);
       last_order = order;
       var url =location.href.split('?')[1];

        window.location.href = '?'+url;
       // var data = {};

        //var url ='/cart/sort_filter?subcat='+subcat+'&'+ location.href.split('?')[1];
        // console.log(data);
        // $.ajax({
        //     url:url,
        //     type:'GET',
        //     data: data,
        //     cache:true,
        //     success: function (data) {
        //         console.log('OK');
        //
        //         $('#subcat_items').html('');
        //
        //
        //
        //     },
        //     error: function () {
        //         console.log('ERROR')
        //     }
        // })

     }




}

function search(subcat) {
    var search_string = $('#search_string').val();

    if (last_search == search_string){
        console.log('search used');
    }
    else{
        console.log(search_string,subcat);
        setGetParam('search',search_string);
        last_search=search_string;
        var url =location.href.split('?')[1];

        window.location.href = '?'+url;
        // var data = {};

       // var url ='/cart/sort_filter?subcat='+subcat+'&'+ location.href.split('?')[1];
        // console.log(data);
        // $.ajax({
        //     url:url,
        //     type:'GET',
        //     data: data,
        //     cache:true,
        //     success: function (data) {
        //         console.log('OK');
        //
        //     },
        //     error: function () {
        //         console.log('ERROR')
        //     }
        // })

     }




}