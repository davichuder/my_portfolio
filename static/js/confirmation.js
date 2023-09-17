var digits_num1 = 2;
var digits_num2 = 1;
var confirmation_num1 = Math.floor(Math.random() * (9 * 10 ** (digits_num1 - 1))) + 10 ** (digits_num1 - 1);
var confirmation_num2 = Math.floor(Math.random() * (9 * 10 ** (digits_num2 - 1))) + 10 ** (digits_num2 - 1);
var confirmation_sum = confirmation_num1 + confirmation_num2;
var text_confirmation = "¿Eres un robot?<br>¿Cual es la suma entre " + confirmation_num1 + " y " + confirmation_num2 + "?";

$(function () {

    $(".confirmation").html(text_confirmation);
    $('#sum').on('keyup', function () {
        input_confirmation = document.getElementById("sum").value;
        if (isNaN(input_confirmation)) {
            let text_nan = '<strong style="color:yellow;">¡Ingrese un número!<strong>';
            $(".confirmation").html(text_confirmation + " " + text_nan);
            $("#submit-button").addClass("disabled");
            return;
        }
        value_confirmation = parseInt(input_confirmation);
        if (value_confirmation === confirmation_sum) {
            let text_correcto = '<strong style="color:green;">¡Correcto!<strong>';
            $(".confirmation").html(text_confirmation + " " + text_correcto);
            $("#submit-button").removeClass("disabled");
            return;
        }
        let text_incorrecto = '<strong style="color:red;">¡Incorrecto!<strong>';
        $(".confirmation").html(text_confirmation + " " + text_incorrecto);
        $("#submit-button").addClass("disabled");
        console.log("false");
    });
});