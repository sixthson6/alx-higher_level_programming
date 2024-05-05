$(document).ready(function() {
    const url = "http://stefanbohacek.com/hellosalut/?";

    $("#btn_translate").click(function() {

        $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function(data) {
            $("#hello").html(data.hello)
        });
    });
});