$(document).ready(function(){
    console.log("JQuery ready to kick ass!");
    var state_filter = $("#state_filter");

    $("#submit_filter_button").click(function() {
        console.log("filter submitted");
        url = state_filter.val();

        $(location).attr("href", url);
    });
});