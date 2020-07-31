let clipboard = new Clipboard('.copy-icon');

$(document).ready(function(){

    // Success message when user has copied URL from footer
    clipboard.once('success', function(e) {
        $('.copy-icon').append('<p class="copy-success">Copied!</p>');
    });

    // If copy to clipboard function is unavailable, an error is triggered here
    clipboard.on('error', function(e) {
        alert("Oops, it looks like this function isn't supported on your browser! Manually copy this url for the same effect: http://ms3-move-on.herokuapp.com/index");
    });

    // Adds background color to navbar on scroll down past 20px, inspired by source code found on here: https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling
    $(function () {
        $(document).scroll(function () {
        var $nav = $(".sticky-top");
        $nav.toggleClass('scrolled', $(this).scrollTop() > 20);
        });
    });

    // Fades out flash message gradually after user has read it
    $("#current-message").delay(5000).fadeOut("slow");

    // Function required for the date/time picker in the task forms
    $(function () {
        $('.datepicker').datepicker({
            todayHighlight: true,
            clearBtn: true,
            format: "dd/mm/yyyy"
        });
    });

    // Smooth scroll to top function courtesy of: https://codepen.io/deveb22/pen/QxPmGz
    var scrollBtn = $('#scroll-top-button');

    $(window).scroll(function() {
        if ($(window).scrollTop() > 80) {
            scrollBtn.addClass('show');
        } else {
            scrollBtn.removeClass('show');
        }
    });

    scrollBtn.on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop:0}, '80');
    });

});







