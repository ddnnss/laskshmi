function add_to_cart(form) {


        console.log(form.elements["items_number"].value);
        console.log(form.elements["item_id"].value);
        console.log(form.elements["item_name"].value);
        console.log(form.elements["item_price"].value);
        console.log(form.elements["item_image"].value);
        var item_number = form.elements["items_number"].value
        var item_id = form.elements["item_id"].value
        var item_name = form.elements["item_name"].value
        var item_price = form.elements["item_price"].value
        var item_image = form.elements["item_image"].value
        var csrf_token = form.elements["csrfmiddlewaretoken"].value



    console.log($(form).attr('action'));
     console.log(csrf_token);
        var data = {};
        data.item_id = item_id;
        data.item_number = item_number;
        data['csrfmiddlewaretoken'] = csrf_token;
        var url = $(form).attr('action');
  console.log(data);
        $.ajax({
            url:url,
            type:'POST',
            data: data,
            cache:true,
            success: function (data) {
                console.log('OK');
                console.log(data.total_items_in_cart);
                console.log(data.all_items);

                $('#cart_table_lg').empty();

             //   $.each(data.all_items,function (k,v) {
                    $('#cart_table_lg').append('<tr class="miniCartProduct">\n' +
                        '                                    <td style="width:20%" class="miniCartProductThumb">\n' +
                        '                                        <div><a href="product-details.html"> <img src="'+ item_image +'" alt="img">\n' +
                        '                                        </a></div>\n' +
                        '                                    </td>\n' +
                        '                                    <td style="width:40%">\n' +
                        '                                        <div class="miniCartDescription">\n' +
                        '                                            <h4><a href="product-details.html"> TSHOP Tshirt DO9 </a></h4>\n' +
                        '                                            <span class="size"> 12 x 1.5 L </span>\n' +
                        '                                            <div class="price"><span> $22 </span></div>\n' +
                        '                                        </div>\n' +
                        '                                    </td>\n' +
                        '                                    <td style="width:10%" class="miniCartQuantity"><a> X 1 </a></td>\n' +
                        '                                    <td style="width:15%" class="miniCartSubtotal"><span> $33 </span></td>\n' +
                        '                                    <td style="width:5%" class="delete"><a> x </a></td>\n' +
                        '                                </tr>');


             //   })

                $.amaran({
                        'theme'     :'user blue',
                        'content'   :{
                            img: item_image,
                            user:'Добавлено :',
                            message: item_number + ' шт. - ' + item_name
                        },
                        'position'  :'bottom right',
                        'outEffect' :'slideBottom'
                    });
            },
            error: function () {
                console.log('ERROR')
            }
        }





           )
    }