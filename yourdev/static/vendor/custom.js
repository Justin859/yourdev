// JQuERY

$(document).ready(function(){

    $(".mdc-snackbar__action-button").click(function(){
        $(".mdc-snackbar").hide();
    });

    $("form").submit(function() {
        document.getElementById("overlay").style.display = "block";
        document.getElementById("overlay_text").style.display = "block";
    });

    $(".mrbutton").click(function() {
        document.getElementById("overlay").style.display = "block";
        document.getElementById("overlay_text").style.display = "block";
    });

});

$(window).bind("pageshow", function(event) {
    $("#overlay").hide();
});

$(window).bind("pageshow", function(event) {
    $("#overlay_text").hide();
});

// MDC Components (Javascript)

var page = ((window.location.href).split("//")[1]).split('/')[1]

if (page === 'Services' || page === 'Contact' || page === '') {
    var toolbar = mdc.toolbar.MDCToolbar.attachTo(document.querySelector('.mdc-toolbar'));
    toolbar.fixedAdjustElement = document.querySelector('.mdc-toolbar-fixed-adjust');
    
    let drawer = new mdc.drawer.MDCTemporaryDrawer(document.querySelector('.mdc-temporary-drawer'));
    document.querySelector('.menu').addEventListener('click', () => drawer.open = true);
}

if (page === 'Contact') {
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-client_name'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-client-mail'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-client-query'));
}

if (page === 'Get-Started') {
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-client-first-name'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-client-last-name'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-client-email'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-company-name'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-company-physical-address'));
    mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-company-description'));
    
}
