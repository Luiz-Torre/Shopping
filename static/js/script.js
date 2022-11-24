/// <reference path="../typings/globals/jquery/index.d.ts" />


function showToast() {
    $("#myToast").toast("show");

}

$(function(){
  $("#botao-enviar").click(function(event){
    event.preventDefault();
    let validaCampos = validaCamposFunction()
    // if(validaCampos){
    //     event.preventDefault();
    //     $("#myAlert").css("display", "");
    //     setTimeout(function () {
    //         $("#form_contato").submit();
    //
    //
    //     }, 5000);
    // }

  }
  )  
},
    $(".btn_like").click(function(){
    let nome_btn = $("#" + this.id);

    let nome_datalike = $("#" + $(this).closest('content').find('span')[0].id);
    let like_data = $(nome_datalike).data("like");

    let dislike = $("#" + $(this).closest('content').find('i')[1].id)
    let nome_datadislike = "#" + $(this).closest('content').find('span')[1].id
    let dislike_data = $(nome_datadislike).data("dislike");

    $(nome_datadislike).text(dislike_data)


    if(nome_btn.hasClass("far")){
    $(nome_datalike).text(like_data+1)
    nome_btn.removeClass("far")
    dislike.removeClass("fas")
    dislike.addClass("far")
    nome_btn.addClass("fas")
    }
    else{
    $(nome_datalike).text(like_data)
    nome_btn.removeClass("fas")
    nome_btn.addClass("far")

    }



    }),
    $(".btn_dislike").click(function(){
        let nome_btn = $("#" + this.id);
    
        let nome_datalike = "#" + $(this).closest('div').find('span')[0].id;
    
        let like_data = $(nome_datalike).data("like");
        let nome_datadislike = "#" + $(this).closest('content').find('span')[1].id
        let dislike_data = $(nome_datadislike).data("dislike");
    
        $(nome_datalike).text(like_data)
    
    
        let like = $("#" + $(this).closest('content').find('i')[0].id)

        
        if(nome_btn.hasClass("far")){
        $(nome_datadislike).text(dislike_data+1)
        nome_btn.removeClass("far")
        like.removeClass("fas")
        like.addClass("far")
        nome_btn.addClass("fas")
        }
        else{
        $(nome_datadislike).text(dislike_data)
        nome_btn.removeClass("fas")
        nome_btn.addClass("far")
    
        }
    }),
)

//Aqui eu valido o formulario da pagina de contatos
function validaCamposFunction(){
    let nome = $("#nome")
    let sobrenome = $("#sobrenome")
    let email = $("#email")
    let telefone = $("#telefone")
    let fullfeedback = $("#fullfeedback")
    let verifica = true;
    if(nome.val() == ''){
        nome.addClass("is-invalid")
        nome.removeClass("is-valid")
        verifica = false;

    }
    else{
        nome.addClass("is-valid")
        nome.removeClass("is-invalid")
    }
    if(sobrenome.val() == ''){
        sobrenome.addClass("is-invalid")
        sobrenome.removeClass("is-valid")
        verifica = false

    }
    else{
        sobrenome.addClass("is-valid")
        sobrenome.removeClass("is-invalid")
    }
    if(email.val() == ''){
        email.addClass("is-invalid")
        email.removeClass("is-valid")
        verifica = false

    }
    else{
        email.addClass("is-valid")
        email.removeClass("is-invalid")
    }

    if(telefone.val() == ''){
        telefone.addClass("is-invalid")
        telefone.removeClass("is-valid")
        verifica = false

    }
    else{
        telefone.addClass("is-valid")
        telefone.removeClass("is-invalid")
    }

    
    if(fullfeedback.val() == ''){
        fullfeedback.addClass("is-invalid")
        fullfeedback.removeClass("is-valid")
        verifica = false

    }
    else{
        fullfeedback.addClass("is-valid")
        fullfeedback.removeClass("is-invalid")
    }
    return verifica;
}
