var $ = function(targetElementThing) {


  var stuff$cando = {
    ready: function(callback) {
      document.addEventListener("DOMContentLoaded",function(){
        callback();
      })
    },
    click: function(callback) {
      document.getElementById(targetElementThing).addEventListener("click", function() {
        callback();
      })
    }
  }
  return stuff$cando;
}


$(document).ready(function(){
  console.log("the page has loaded");

  $('tester').click(function(){
    console.log('YOU HAVE CLICKED!!!!');

  })

});
