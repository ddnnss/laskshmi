function quick_view(item_id)
{

   var url = '/item/quick_view/';
   var csrf_token = $('#dummy_form [name="csrfmiddlewaretoken"]').val();
   var data = {};
   data.item_id = item_id;
   data['csrfmiddlewaretoken'] = csrf_token;
   $.ajax({
            url:url,
            type:'POST',
            data: data,
            cache:true,
            success: function (data) {
                console.log('OK');
                $('.product-title').html(data.item_name);
                $('.product-code').html('АРТИКУЛ : ' + data.item_article);

                if (data.item_discount > 0){
                     $('.price-standard').html(data.item_price + ' &#8381;');
                     $('.price-sales').html(data.item_price_discount + ' &#8381;');
                }
                else {
                     $('.price-standard').html('');
                     $('.price-sales').html(data.item_price + ' &#8381;');
                }
                $('.details-description p').html(data.item_description);
                $('.product-largeimg-link img').attr('src',data.item_images[0]);
                $('.modal-product-thumb').html('');

                 $.each(data.item_images,function (i,v) {
                     $('.modal-product-thumb').append(' <a  class="thumbLink">\n' +
                         '            <img  data-large='+data.item_images[i]+' alt="img" class="img-responsive" src='+ data.item_images[i] +'>\n' +
                         '        </a>');


                 })


                $('#productSetailsModalAjax').modal('show');





            },
            error: function () {
                console.log('ERROR')
            }
        });


}

function show_thumb(i,img) {
    console.log(img);

}
