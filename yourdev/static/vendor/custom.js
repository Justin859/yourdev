// JQuERY

$(document).ready(function(){

    $(".mdc-snackbar__action-button").click(function(){
        $(".mdc-snackbar").hide();
    });

});

// MDC Components

var toolbar = mdc.toolbar.MDCToolbar.attachTo(document.querySelector('.mdc-toolbar'));
toolbar.fixedAdjustElement = document.querySelector('.mdc-toolbar-fixed-adjust');

let drawer = new mdc.drawer.MDCTemporaryDrawer(document.querySelector('.mdc-temporary-drawer'));
document.querySelector('.menu').addEventListener('click', () => drawer.open = true);

mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-textfield-name'));
mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-textfield-email'));
mdc.textfield.MDCTextfield.attachTo(document.querySelector('.mdc-textfield-query'));

mdc.snackbar.MDCSnackbar.attachTo(document.querySelector('.mdc-snackbar'));



