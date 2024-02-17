
$(".product-image").attr("src", localStorage.getItem('productImage'));
$(".product-name").html(localStorage.productName);
$(".product-price").html(localStorage.productPrice);
$(".total").html(localStorage.productPrice);
$(".farmer-id").html(localStorage.farmerId);
var farmerId = $(".farmer-id").text();
$("#farmer2").val(farmerId);
$(".farmer2").attr("value", localStorage.getItem('farmerId'));
$(".delivery-option-input").on("click", function() {
    if (this.id == 1) {
        $(".shipping-charge").html("Rs.0.00");
        $(".delivery-date").html("Delivery date: Tuesday, June 21");
    } else if (this.id == 2) {
        $(".shipping-charge").html("Rs.4.99");
        $(".delivery-date").html("Delivery date: Wednesday, June 15");
    } else if (this.id == 3) {
        $(".shipping-charge").html("Rs.9.99");
        $(".delivery-date").html("Delivery date: Monday, June 13");
    }
    initPrice();});
initPrice();
function initPrice() {
    var total = parseFloat($(".total").html().slice(3));
    var shippingCharge = parseFloat($(".shipping-charge").html().slice(3));
    $(".total-before-tax").html("Rs." + (total + shippingCharge).toFixed(2));
    var totalBeforeTax = parseFloat($(".total-before-tax").html().slice(3));
    var taxValue = (10/100) * totalBeforeTax;
    $(".tax").html("Rs." + taxValue.toFixed(2));
    var tax = parseFloat($(".tax").html().slice(3));
    var orderTotalValue = totalBeforeTax + tax;
    $(".order-total").html("Rs." + orderTotalValue.toFixed(2));
    var orderTotal = parseFloat($(".order-total").html().slice(3));}
