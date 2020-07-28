  
//Only runs function when page is ready
$(document).ready(function(){

    //Inspired by source code found on here: https://www.journaldev.com/5446/how-to-create-scroll-to-top-animation-in-jquery
    $("a[href='#container']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 700);
        return false;
    });

    $("a[href='#container']").click(function () {
    //  Get the text field

    console.log("Hejsan!")

    });

});



    //$('.expand-btn').click(function(){
        //$(".btn-container").find((".expand-btn").not($(this)).addClass(".collapse"));
    //});





