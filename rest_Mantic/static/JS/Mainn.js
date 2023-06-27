var coords="";
$(document).ready(function () {
    if(!navigator.geolocation){
        swal("Ubicacion no disponible")
    }else{
        navigator.geolocation.getCurrentPosition(obtenerPosicion);
    }

    function obtenerPosicion(position){
        console.log("longitude= "+position.coords.latitude+" latitude= "+position.coords.longitude);
    }

    $("#btncrearcuenta").click(function (e) {
        if (validar() != "") {
            swal("Error", validar(), "warning")
        } else {
            swal("Enviado", "Tu cuenta se ha creado ", "success")
        }
        e.preventDefault();
    });
    function validar() {
        var html = "";
        var nombreUsuario = $("#validationCustom01").val();
        var contraseña = $("#validationCustom02").val();
        var correo = $("#validationCustomUsername").val();
        if (nombreUsuario == "") {
            html += "- Debe ingresar un nombre de usuario\n";
        } else {
            if (nombreUsuario.length<6) {
                html += "- El nombre de usuario debe tener al menos 6 caracteres\n";
            }
        }
        if (contraseña == "") {
            html += "- Debe ingresar una contraseña\n";
        } else {
            if (contraseña < 8) {
                html += "- La contraseña debe tener al menos 8 caracteres\n";
            }
            if (!contraseña.match(/[A-Z]/)){
                html += "- La contraseña debe tener al menos una mayuscula\n";
            }
            if(!contraseña.match(/\d/)){
                html += "- La contraseña debe tener al menos un numero\n";
            }
        }
        if (correo == "") {
            html += "- Debe ingresar un correo electronico\n";
        } else {
            if (/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(correo)) {
            } else {
                html += "- El correo electronico es invalido";
            }
        }

        return html;
    }
});