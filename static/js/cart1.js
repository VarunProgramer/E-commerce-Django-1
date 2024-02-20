document,addEventListener("DOMContentLoaded", function(event){
    const btnplus = document.getElementById("btnplus");
    const btnMinus = document.getElementById("btnMinus");
    const txtQty = document.getElementById("txtQty");
    const btnCart = document.getElementById("btnCart");

    btnplus.addEventListener("click", function(){
        let qty = parseInt(txtQty.value,10);
        qty = isNaN(qty)?0:qty;

        if (qty<10){
            qty++
            txtQty.value = qty
        }
    });
    btnMinus.addEventListener("click", function(){
        let qty = parseInt(txtQty.value,10);
        qty = isNaN(qty)?0:qty;

        if (qty>1){
            qty--
            txtQty.value = qty
        }
    });
    btnCart.addEventListener("click", function(){
        let qty = parseInt(txtQty.value, 10);
        qty = isNaN(qty)?0:qty;
        var pid = this.dataset.product
        var action = this.dataset.action
        console.log(' product id : ', pid, '\n\n', 'action :', action, '\n\n' , 'product_qty : ', qty, '\n')

        console.log('USER : ', user)
        if (user === 'AnonymousUser'){
            console.log('user is not login, so please login first')
        }else{
            add_to_cart(pid, qty, action);
        };
    });
});
function add_to_cart(pid, qty, action){
    console.log('user is login, so proses the data')
    var url = '/AddToCart'

    fetch(url, {
        method:'POST',
        credentials: 'same-origin',
        headers:{
            'Accept' : 'application/json',
            'X-Requested-With' : 'XMLHttpRequest',
            'X-CSRFToken' : "{{ csrf_token }}",
        },
        body: JSON.stringify({
            'product_id' : pid,
            'action' : action,
            'product_qty' : qty,
        })
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log("data : ", data);
        })
};