$(document).ready(function(){
    $(".color-tag").select2({ tags: true });
    $(".size-tag").select2({ tags: true });
  
    $(".delete-product").click(function(){
        product_id = $(this).attr('data-id')
            $.ajax({
            url: `/products/${product_id}`,
            type: 'DELETE',
                success: function(){
            this.parent.parent.remove();
            }});
        });

    $(".create-size-variants").click(function(){
        $( ".new-size" ).clone().prependTo( ".buttons" );
    }); 

}); 




