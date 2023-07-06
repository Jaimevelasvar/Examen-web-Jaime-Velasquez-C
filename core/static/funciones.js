function validarRut(){
    var rut = document.querySelector("#rut");
    if(rut.value.length == 10 || rut.value.length == 9){
        rut.classList.remove("error");
    }else{
        rut.classList.add("error");
    }
}
function validarNombre(){
    var nombre = document.querySelector("#nombre");
    if(nombre.value.length >= 3 && nombre.value.length <= 12){
        nombre.classList.remove("error")
    }else{
        nombre.classList.add("error")
    }
}
function validarAppat(){
    var appat = document.querySelector("#appat");
    if(appat.value.length >= 4 && appat.value.length <= 12){
        appat.classList.remove("error")
    }else{
        appat.classList.add("error")
    }
}
function validarApmat(){
    var Apmat = document.querySelector("#apmat");
    if(Apmat.value.length >= 4 && Apmat.value.length <= 12){
        Apmat.classList.remove("error")
    }else{
        Apmat.classList.add("error")
    }
}
function validarEmail(){
    var Email = document.querySelector("#email");
    if(Email.value.length > 10 && Email.classList.contains("@")){
        Email.classList.remove("error")
    }else{
        Email.classList.add("error")
    }
}
function validar(){
    var rut = document.querySelector("input, textarea");
    var result = true;
    inputs.forEach(element => {
        if(element.classList.contains("error")){
            document.querySelector("#mensaje").innerHTML = "Revise el campo "+element.name+"."
            result = false;
        }
        
    });
    return result;
}
function validarContraseña(){
    var contraseña = document.querySelector("#contraseña");
    if(contraseña.value.length >= 8 ){
        contraseña.classList.remove("error")
    }else{
        contraseña.classList.add("error")
    }
}
function confirmarContraseña(){
    var dato = document.querySelector("#pass");
    var contra = document.querySelector("#contraseña")
    if(dato.value == contra.value){
        dato.classList.remove("error")

    }else{
        dato.classList.add("error")
    }
}

function mostrarUsuarios(){
    var dato = document.querySelector(".intro");
    var dato2 = document.querySelector(".prods");
    dato.classList.remove("hide");
    dato2.classList.add("hide");
    
    

}
function mostrarProductos(){
    var dato = document.querySelector(".intro");
    var dato2 = document.querySelector(".prods");
    dato2.classList.remove("hide");
    dato.classList.add("hide");

}

function carritoIncrementar(){
    var carrito = document.getElementById("carritoIncrementar");
    var value = carrito.innerHTML;

    ++value;

    console.log(value)
    document.getElementById("carritoIncrementar").innerHTML = value;
}
function editarPerfil(){
    var dato = document.querySelector(".perfil");
    dato.classList.remove("hide")
}
function cancelarEdicion(){
    var dato = document.querySelector(".perfil");
    dato.classList.add("hide")
}
function suscripcion1(){
    var dato = document.querySelector(".cansub");
    var dato2 = document.querySelector(".sub");
    var dato3 = document.querySelector(".subs2");
    var dato4 = document.querySelector(".subs")
    var dato5 = document.querySelector(".donacion")
    dato2.classList.remove("hide");
    dato.classList.add("hide");
    dato3.classList.remove("hide");
    dato4.classList.add("hide")
    dato5.classList.add("hide")
}
function suscripcion2(){
    var dato = document.querySelector(".cansub");
    var dato2 = document.querySelector(".sub");
    var dato3 = document.querySelector(".subs2")
    var dato4 = document.querySelector(".subs")
    var dato5 = document.querySelector(".donacion");
    dato2.classList.add("hide");
    dato.classList.remove("hide");
    dato3.classList.add("hide");
    dato4.classList.remove("hide");
    dato5.classList.remove("hide");
}

function mostrarDetalle(){
    var dato = document.querySelector(".card3");
    dato.classList.remove("hide");
}