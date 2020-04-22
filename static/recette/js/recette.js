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
    $("#liste_ingredients li").click(function(){
        if (this.value != 0){
            $.ajax({
                url : '../'+this.value+'/supprimer_ingredient/',
                type : 'GET',
                data_type : 'html'
            });
            $(this).text('Ingrédient supprimé');
            $(this).hide(1000);
        }
    });
    $("#comments span.suppr").click(function(){
            $.ajax({
                url : '../'+$(this).data('id')+'/supprimer_commentaire/',
                type : 'GET',
                data_type : 'html'
            });
            $(this).parentsUntil('li').text('Commentaire supprimé');
            $(this).parentsUntil('li').hide(1500);
    });
});