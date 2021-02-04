//  Send a POST form to django without page reload
//  AJAX is use throw /wcs/add url
//  The entry point is #member-form HTML form.

$("#member-form").submit(function (event) {
    // preventing from page reload and default actions
    event.preventDefault();
    const log = false;
    if (log===true) { console.log('js-form.js: member-form START')}
    // serialize the data for sending the Django form.
    let serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: "/wcs/add",
        data: serializedData,
        success: function () {
            if (log===true) { console.log('js-form.js: member-form SUCCESS')}
            // on successfull creating object
            // 1. clear the form.
            $("#member-form").trigger('reset');
            // 2. focus to nickname input
            $("#id_name").focus();
        },
        error: function () {
            if (log===true) { console.log('js-form.js: member-form ERROR')}
            // alert the error if any error occured
            alert("Contrôler le formulaire, merci.");
            // alert(JsonResponse({"error": form.errors}));
        }
    })
})


