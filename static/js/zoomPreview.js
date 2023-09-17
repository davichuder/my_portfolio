$(function () {
    $('.zoom').on('click', function () {
        if ($(window).width() >= 768) {
            $('.image-preview').attr('src', this.src);
            $('#imagemodal').modal('show');
        }
    });
});


$(function () {
    $('.modal-body button').on('click', function () {
        $('#imagemodal').modal('hide');
    });
});