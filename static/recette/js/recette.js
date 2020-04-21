jQuery(document).ready(function($){
    $("#addIngre input[type='text']").click(function(){
        var nbre = 0;
        $('#addIngre input[type="text"]').each(function () {
            if ($(this).val() === ''){
            }else{
            nbre++;
            }
        });
        $('#addIngre input[type="submit"]').each(function () {
            if ($(this).val() === ''){
            }else{
            nbre++;
            }
        });
        $('input[name="form-INITIAL_FORMS"]').val(nbre);
    });
});