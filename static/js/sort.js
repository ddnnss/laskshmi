var last_filter = '';
var last_order = '';
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


    console.log(order,subcat);
    setGetParam('order',order);

}