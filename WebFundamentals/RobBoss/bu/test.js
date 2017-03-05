console.log('yo we made it!');
var $ = function(thingy) {
  var things$cando = {
    ready: function(callback){
      document.addEventListener("DOMContentLoaded", function(){
        callback();
      })
    },

    click: function(callback){
      document.getElementById(thingy).addEventListener("click", function(){
        callback();
      })
    },
    changebg: function(){
      document.getElementById(thingy).style.background = 'gree'
    }


  }
  return things$cando;
}

$(document).ready(function(){
  console.log('THE DOCUMENT IS MOST READY SIRRRR');

  $('tester').click(function(){
    console.log('THOU HAST CLICKED');
  })
})
