$(document).ready(function() {
    $('.dogs').click(function(){
        console.log('Got it!')
        $('.theDogs').html(`
            <img src='./images/RoxyAndBear.jpg' alt='Roxy and Bear' />
            <img src='./images/RoxyAndLucy.jpg' alt='Roxy and Lucy' />
        `)
    })

    $('.newDog').click(function(){
        $.get("https://dog.ceo/api/breeds/image/random", function(res) {
            console.log(res.message)
            // var html_str = "";
            // html_str += `<img src='${res.message}' alt='Random Dog' />`;
            $('.img').html(`<img src='${res.message}' alt='Random Dog' />`)
        }, "json");
        return false;
    })
})



