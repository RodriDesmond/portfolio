document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    var elems2 = document.querySelectorAll('.parallax');
    var instances2 = M.Parallax.init(elems2);
    var elems3 = document.querySelectorAll('.carousel');
    var instances3 = M.Carousel.init(elems3);
});