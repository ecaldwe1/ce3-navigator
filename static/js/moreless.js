$( document ).ready(function() {

    $('.show_all').click(function() {
        var div_id=$(this).attr('data-long-id');
        $(this).parent().slideUp();
        $('#' + div_id).slideDown();
    });

    $('.show_less').click(function() {
        var div_id=$(this).attr('data-short-id');
        $(this).parent().slideUp();
        $('#' + div_id).slideDown();
    });
    
});
