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

function filter(filter,subcat) {

    console.log(filter,subcat);
    if (last_filter == filter){
        console.log('filter used');
    }
    else{
        setGetParam('filter',filter);
        last_filter = filter;

      var data = {};

        var url ='/cart/sort_filter?subcat='+subcat+'&'+ location.href.split('?')[1];
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

}

function order(order,subcat) {
     if (last_order == order){
        console.log('order used');
    }
    else{
       console.log(order,subcat);
       setGetParam('order',order);
       last_order = order;
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
     }




}