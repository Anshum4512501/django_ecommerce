
// $('button .update-cart').each(function(){
//         $(this).click(function(index){
//             console.log("jj");
//         });
        
    
// });
// console.log("User",user)


let button  = document.getElementsByClassName('update-cart');
let plus_button = document.getElementsByClassName('plus_button');
let minus_button = document.getElementsByClassName('minus_button');
var url = '/store/update-cart/';
function update_cart_loop(){

}

for(var i=0;i<button.length;i++){
    button[i].addEventListener("click", function(){
        console.log(this.dataset.product);
        console.log(this.dataset.action);
        if(user==='Anonymoususer'){
            console.log("Not authenticated yet");
        }
        else{
            console.log("User",user);
            update_cart(this.dataset.product,this.dataset.action);
        }
      });
}

for(var i=0;i<minus_button.length;i++){
  minus_button[i].addEventListener("click", function(){
      // console.log(this.dataset.product);
      // console.log(this.dataset.action);
     
      // console.log(this);
      if(user==='Anonymoususer'){
          console.log("Not authenticated yet");
      }
      else{
          console.log("User",user);
          console.log("Minus button dataset",this.dataset);
          
          console.log("Minus button dataset",this.dataset.product);
          
          update_cart(this.dataset.product,this.dataset.action);
      }
    });
}
for(var i=0;i<plus_button.length;i++){
  plus_button[i].addEventListener("click", function(){
      // console.log(this.dataset.product);
      // console.log(this.dataset.action);
      
      if(user==='Anonymoususer'){
          console.log("Not authenticated yet");
      }
      else{
          console.log("User",user);
          console.log(this.dataset.product);
          
           update_cart(this.dataset.product,this.dataset.action);
      }
    });
}

function update_cart(product_id,action){
    fetch(url, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken':csrftoken,
        },
       
        body: JSON.stringify({'product_id':product_id,'action':action}) 
      }).then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
      window.location.reload()
}

