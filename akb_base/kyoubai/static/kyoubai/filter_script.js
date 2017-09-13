$(document).ready(function(){
    console.log("JQuery-kun ready to kick ass!");
    var state_filter = $("#state_filter");
    var min_price_filter = $("#min_price_filter")
    var min_price_filter_value;
    var max_price_filter = $("#max_price_filter");
    var max_price_filter_value;


    function update_values() {
    console.log("updating");
        min_price_filter_value = min_price_filter.val();
        max_price_filter_value = max_price_filter.val();

        if (min_price_filter_value == "") {
        min_price_filter_value = "0";
        }
        if (max_price_filter_value == "") {
            max_price_filter_value = "1000000";
        }
    }

    $("#submit_filter_button").click(function() {
        console.log("filter submitted");
        update_values();
        var url = state_filter.val() +"-" +min_price_filter_value +"-" +max_price_filter_value;

        $(location).attr("href", url);
    });
});