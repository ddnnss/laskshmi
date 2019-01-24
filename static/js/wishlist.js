function wishlist_add(item_id) {
    console.log(item_id);
      var csrf_token = $('#dummy_form [name="csrfmiddlewaretoken"]').val();
    // console.log($(form).attr('action'));
    //  console.log(csrf_token);
        var data = {};
        if (item_id){
            data.item_id = item_id;
        }
        else{
            data.item_id = $('#item_id').val();
        }

        data['csrfmiddlewaretoken'] = csrf_token;
        var url = '/cart/wishlist_add/';
        console.log(data);
        $.ajax({
            url:url,
            type:'POST',
            data: data,
            cache:true,
            success: function (data) {
                console.log('OK');
                console.log(data.result);

                if (data.result){
                    $.amaran({
                            'theme'     :'colorful',
                            'content'   :{
                               bgcolor:'#38f28d',
                               color:'#fff',
                               message:'Товар добавлен в закладки !'
                            },
                            'position'  :'bottom right',
                            'outEffect' :'slideBottom'
                        });
                }
                else
                {
                     $.amaran({
                            'theme'     :'colorful',
                            'content'   :{
                               bgcolor:'#f23c3a',
                               color:'#fff',
                               message:'Недоступно для незарегистрированных пользователей !'
                            },
                            'position'  :'bottom right',
                            'outEffect' :'slideBottom'
                        });
                }


            },
            error: function () {
                console.log('ERROR')
            }
        })
}

function wishlist_delete(id) {
    console.log(id);
     var csrf_token = $('#dummy_form [name="csrfmiddlewaretoken"]').val();
    // console.log($(form).attr('action'));
    //  console.log(csrf_token);
        var data = {};
        data.id = id;
        data['csrfmiddlewaretoken'] = csrf_token;
        var url = '/cart/wishlist_delete/';
        console.log(data);
        $.ajax({
            url:url,
            type:'POST',
            data: data,
            cache:true,
            success: function (data) {
                console.log('OK');
                console.log(data.result);

                if (data.result){
                    $('#wl_'+id).remove();
                    $.amaran({
                            'theme'     :'colorful',
                            'content'   :{
                               bgcolor:'#38f28d',
                               color:'#fff',
                               message:'Товар удален из закладок !'
                            },
                            'position'  :'bottom right',
                            'outEffect' :'slideBottom'
                        });
                }



            },
            error: function () {
                console.log('ERROR')
            }
        })

}