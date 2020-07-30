let clipboard = new Clipboard('.copy-icon');

$(document).ready(function(){

    //Allows user to smooth scroll to top from footer, inspired by source code found on here: https://www.journaldev.com/5446/how-to-create-scroll-to-top-animation-in-jquery
    $("a[href='#container']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 700);
            return false;
        });

    // Success message when user has copied URL from footer
    clipboard.once('success', function(e) {
        $('.copy-icon').append('<p class="copy-success">Copied!</p>');
    });

    // If copy to clipboard function is unavailable, an error is triggered here
    clipboard.on('error', function(e) {
        alert("Oops, it looks like this function isn't supported on your browser! Manually copy this url for the same effect: http://ms3-move-on.herokuapp.com/index");
    });

    // Adds background color to navbar on scroll down, inspired by source code found on here: https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling
    $(function () {
        $(document).scroll(function () {
        var $nav = $(".sticky-top");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
        });
    });

    // Fades out flash message gradually after user has read it
    $("#current-message").delay(5000).fadeOut("slow");

});







