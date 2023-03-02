$(function() {
    $(window).on("scroll", function() {
        if($(window).scrollTop() > 50) {
            $(".head").addClass("active");
        } else {
            //remove the background property so it comes transparent again (defined in your css)
           $(".head").removeClass("active");
        }
    });
});
$("#timeline").mouseenter(function(){
    document.getElementById("mainpicture").style = "background: url(/static/image/sbcharya1.jpg) center center; background-attachment: fixed; background-size: cover;";
});
$("#work").mouseenter(function(){
    document.getElementById("mainpicture").style = "background: url(/static/image/sbcharya2.jpg) center center; background-attachment: fixed; background-size: cover;";
});
$("#mainhero").mouseenter(function(){
    document.getElementById("mainpicture").style = "background: url(/static/image/sbcharya.jpg) center center; background-attachment: fixed; background-size: cover;";
});

$("#close-tigger").click(function(){
    $("#navitems").css('right','-99999px');
    $("#close-tigger").css('right','-99999px');
});
$("#open-trigger").click(function(){
    $("#navitems").css('right','-36px');
    $("#close-tigger").css('right','10px');
});

$(".mobilemenus").click(function(){
        $("#navitems").css('right','-99999px');
    $("#close-tigger").css('right','-99999px');
});