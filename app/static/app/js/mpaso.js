$(document).ready(function () {
    $('.animated-card').each(function () {

        // animate on enter
        $(this).on('mouseenter', function (evt) {
            $(this).find('.sliding-card').css({
                'top': '0px',
                'height': '337.5px'
            });
            $(this).find('.slides-up').css('visibility', 'visible');
            var img = $(this).find('img');
            img.css('filter', 'blur(5px)');
            img.css('transform', 'scale(2.5)');
        })

        //animate on exit
        $(this).on('mouseleave', function (evt) {
            $(this).find('.sliding-card').css({
                'top': '225px',
                'height': '168.75px'
            });
            $(this).find('.slides-up').css('visibility', 'hidden');
            var img =$(this).find('img');
            img.css('filter', 'blur(0px)');
            img.css('transform', 'scale(1)');

        })
    })

})

