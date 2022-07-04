function clearAlert(){

}

function changeImg(element){
    console.log("changeimage", element);
    element.src = "./assets/succulents-2.jpg";

}


function closeCookie(){
    console.log("ate the cookie");
    var element =  document.querySelector("#cookie-box");
    element.remove();
}

function removeAlert(){
    console.log("you're cart is empty", element)
    var element = document.querySelector("Soothing Aloe")
    element.remove()
}