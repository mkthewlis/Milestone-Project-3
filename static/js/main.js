let clipboard = new Clipboard('.copy-icon');

$(document).ready(function(){

    //Scrolltop inspired by source code found on here: https://www.journaldev.com/5446/how-to-create-scroll-to-top-animation-in-jquery
    $("a[href='#container']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 700);
            return false;
        });

    // Notifies user the url has successfully been copied
    clipboard.on('success', function(e) {
        $('.copy-icon').append('<p class="copy-success">Copied!</p>');
    });

    // Triggers an alert so the user knows to copy the url themselves
    clipboard.on('error', function(e) {
        alert("Oops, it looks like this function isn't supported on your browser! Manually copy this url for the same effect: http://ms3-move-on.herokuapp.com/index");
    });

});



    //$('.expand-btn').click(function(){
        //$(".btn-container").find((".expand-btn").not($(this)).addClass(".collapse"));
    //});





