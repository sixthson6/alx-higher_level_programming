$(document).ready(function(){
    $("#add_item").click(function(){
       $("<li>Item</li>").insertBefore(".my_list li")
    });
});