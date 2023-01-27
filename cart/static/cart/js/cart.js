console.log("working")
downID = document.getElementsByClassName('arrow_icon')
for(i=0;i<downID.length;i++){
    downID[i].addEventListener('click',function(){
        if(user === 'AnonymousUser'){
            console.log("Please login")
        }else{
            updateQuantity(this.dataset.prod_id,this.dataset.action)
            
        }
       
    })
}

function updateQuantity(cartID,action){
var url = '/updateQuantity/'
header = {
    'Content-Type' : 'application/json',
    'X-CSRFToken': csrftoken,
}
fetch(url,{
    method: 'POST',
    headers:header,
    body:JSON.stringify({"cartID":cartID,"action":action})
})
.then((response)=>{
    return  response.json();
})
.then((data)=>{
    location.reload()
})
}
