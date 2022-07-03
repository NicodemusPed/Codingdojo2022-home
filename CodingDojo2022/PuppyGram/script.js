
function uploadpup(element){
    console.log("New Pup")
    element.innerText = "Uploaded! Thank you.";
}

function removebutton(element){
    console.log("try to remove button")
    element.Remove();
}


function changePicture(element){
    console.log("New Picture",element)
    element.Remove();
}


function pawsvideo(element){
    element.pause()
}

function changeImg(element){
    console.log("Hello2",element)

}

function removeAlert(){
    console.log("cookie monster", element)
    var element = document.querySelector("hello3")
    element.remove()
}

function cookieMonster(){
    console.log("cookie monster", element)
    var element = document.querySelector("hello3")
    element.remove()
}

function incrementLike(id){
    console.log("hello4", id)
    var element = document.querySelector(id)
    console.log("Hello5", element)
    let likeCount = Number(element,innerText)
    console.log()
}