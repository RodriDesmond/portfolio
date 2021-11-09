document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    var elems2 = document.querySelectorAll('.parallax');
    var instances2 = M.Parallax.init(elems2);
    var elems3 = document.querySelectorAll('.slider');
    var instances3 = M.Slider.init(elems3);
    var elems4 = document.querySelectorAll('.carousel');
    var instances4 = M.Carousel.init(elems4, {
        indicators: true,

    });
});