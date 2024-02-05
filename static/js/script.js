function openMenu() {
    if ($("#left-menu").hasClass("extended"))
   {
     $("#left-menu").removeClass('extended');
   }
   else
   {
    $("#left-menu").addClass('extended');
   }
   $('.age_modal').css('display', 'none');
}

$("#btn-form").on('click', function (e) {
    $('.account').fadeOut();
    setTimeout(function() {
        $('.section-user-info').fadeIn();
    }, 1000);
})

$('.back-form').on('click', function (e) {
    $('.section-user-info').fadeOut();
    setTimeout(function() {
        $('.account').fadeIn();
    }, 1000);
})

function copy(text) {
    navigator.clipboard.writeText(text);
}