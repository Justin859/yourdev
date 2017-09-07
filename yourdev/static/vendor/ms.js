// javascript

function slider() {
    if (document.documentElement.scrollTop > 250 || document.body.scrollTop > 250) { //Show the slider after scrolling down 100px
        $('nav').addClass("nav-background");
        $('nav').removeClass("nav-background-inverse")
    } else if(document.documentElement.scrollTop < 250 || document.body.scrollTop < 250) {
        $('nav').removeClass("nav-background");
        $('nav').addClass("nav-background-inverse");
    }
}

// JQuery

$(document).ready(function(){

    $(".mdc-snackbar__action-button").click(function(){
        $(".mdc-snackbar").hide();
    });

    $("form").submit(function() {
        document.getElementById("overlay").style.display = "block";
        document.getElementById("overlay_text").style.display = "block";
    });

    $(window).bind("pageshow", function(event) {
        $("#overlay").hide();
    });
    
    $(window).bind("pageshow", function(event) {
        $("#overlay_text").hide();
    });

    $(document).on('change focusout', function(e){
        if($(e.target).is(':invalid'))  {
            $(e.target).next('.form-text').removeClass('invisible');
        } else {
            $(e.target).next('.form-text').addClass('invisible');
        }
    });

    $(document).on('focusin', 'textarea', function(e){
        $(e.target).next('.form-text-help').removeClass('invisible');
    });

    $(document).on('focusout', 'textarea', function(e){
        $(e.target).next('.form-text-help').addClass('invisible');
    });

    $(".email-input").on("change", function(e) {
        if($(e.target).val() !== "") {
            $(e.target).addClass("email-input-filled");
        } else {
            $(e.target).removeClass("email-input-filled");
        }
    });

    $(window).scroll(function () {
        slider();
    });

    $('#myModal').modal('show')
});