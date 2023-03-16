let dishesInCart = []
let dishesAmount = 0

$("#order-button").click(function() {
    if($(this).hasClass('active')){
        $(this).removeClass('active');
        $('#order').addClass('d-none');
        $(this).html('Hide Order');
    } else {
        $(this).addClass('active');
        $('#order').removeClass('d-none');
        $(this).html('Show Order');
    }
})

function addToCart(btn) {
    let dishValues = btn.value.split(',');
    dishesInCart.push(dishValues[0]);
    dishesAmount = dishesAmount + parseInt(dishValues[2]);
    $('#order-menu').append(`<div class="d-flex justify-content-between mb-2" id="`+dishValues[0]+`">
                                <h2>`+ dishValues[1] +` | `+ dishValues[2] +`$</h2> <button class="btn btn-danger px-2" onclick="removeFromCart(`+dishValues[0]+`,`+dishValues[2]+`)">Remove</button>
                            </div>`);
    $('#amount').html('<h1>'+dishesAmount+'$</h1>')
    $('#add-to-cart-'+dishValues[0]).prop('disabled', true);
    $('#add-to-cart-'+dishValues[0]).html('In Cart!');
}

function removeFromCart(dishIndex, dishPrice){
    $('#'+dishIndex).remove();
    dishesAmount = dishesAmount - parseInt(dishPrice);
    $('#amount').html('<h1>'+dishesAmount+'$</h1>')
    $('#add-to-cart-'+dishIndex).prop('disabled', false);
    $('#add-to-cart-'+dishIndex).html(dishPrice + '$<br>Add To Cart');
}