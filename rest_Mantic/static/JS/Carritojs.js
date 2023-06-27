$(document).ready(function () {
    if (!navigator.geolocation) {
        swal("Ubicacion no disponible")
    } else {
        navigator.geolocation.getCurrentPosition(obtenerPosicion);
    }

    function obtenerPosicion(position) {
        console.log("longitude= " + position.coords.latitude + " latitude= " + position.coords.longitude);
        $.get("https://api.open-meteo.com/v1/forecast?latitude=" + "12" + "&longitude=" + position.coords.longitude + "&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m", function (data) {
            console.log(data);
            console.log(data["current_weather"]["temperature"]);
            $("#cuadrogato").html("<img src='IMG/maxwell-the-cat-maxwell.gif' alt=''></img>");
            if(data["current_weather"]["temperature"]>=20){
                $("#cuadroclima").html("<img src='IMG/Solsito.gif'>");
            }
            if(data["current_weather"]["temperature"]<20){
                $("#cuadroclima").html("<img src='IMG/FantasticAssuredIberianbarbel-size_restricted.gif'>");
            }
        });

    }

});