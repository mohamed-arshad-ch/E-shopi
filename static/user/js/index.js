function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
  beforeSend: function (xhr) {
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});



const btns = document.querySelectorAll('.ti-shopping-cart');
btns.forEach((btn) => {
  btn.addEventListener('click', () => {
    const datad = btn.dataset.s;
    console.log(datad);
    // alert('fuck');
    $.ajax({
      url: 'savebook/',
      type: 'post',
      data: {
        product_id: datad,
        csrfmiddlewaretoken: csrftoken
      },

      success: function (respose) {
        sdf()
        alert("Cart Added Successfully");

        console.log("suus")

        // window.location.replace("http://localhost:8000");
      },
    
    });


  });

});




function sdf() {




  let device = getCookie('device')
  console.log("Pro");
  $.ajax({
    url: 'savebook/',
    type: 'GET',
    data: {
      button_text: "asdas",
      coo:device
    },
    success: function (response) {

      console.log(response.count)


      $(".nav-shop__circle").html(response.count)
      let cart = getCookie('cart')
      a = parseInt(cart)
      c= a+1
      document.cookie = 'cart=' + c + ";max-age=31536000;path=/"
    }
  });



}




