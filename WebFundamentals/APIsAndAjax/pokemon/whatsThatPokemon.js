$(document).ready(function(){
    //alert ('javascript is working')
    //function to loop through and append images to photos div.
    function catchEmAll(){
        for(var i = 1; i <= 151; i++){
            //DRASTICALLY improves readability from ('<img id=' + i + ' src="http://pokeapi.co/media/img/' + i + '.png">')
            //added id to each individual picture
            var image_id = i;
            var pokemon_num = i;
            var image = '';
            image +=  "<img id=";
            image +=  image_id;
            image +=  " src='http://pokeapi.co/media/img/";
            image +=  pokemon_num;
            image +=  ".png'>";
            console.log(image)
            //appends photos of all 151 pokemon to the #photos div
            $('#photos').append(image)
        }
    }
    catchEmAll();

    //get individual info for pokemon
    //listening to the #photos div for a click to call function
    $('#photos').on('click','img',function(){
        var thisID =  $(this).attr('id');
        console.log(thisID)
        //res stands for results. This can be anything.
        //traversing through JSON in order to find the  attributes we're looking for
        $.get("http://pokeapi.co/api/v1/pokemon/" + thisID, function(res) {
            var pokeName = res.sprites[0].name
            var types = res.types[0].name
            var weight = res.weight
            var height = res.height

            var string = '<h2>' + pokeName + '</h2>'
            string+= '<img id=' + thisID + ' src="http://pokeapi.co/media/img/' + thisID + '.png">'
            string+= '<h4>Types:</h4>'
            string+= types
            string+='<h4>Height:</h4>'
            string+=height
            string+='<h4>Weight:</h4>'
            string+=weight

            $('#pokedex_1').html(string);

            console.log(res)
            console.log(pokeName)
            console.log('Types: ' + types)
            console.log('Weight: ' + weight)
            console.log('Height: ' + height)
        }, "json");
});
});
