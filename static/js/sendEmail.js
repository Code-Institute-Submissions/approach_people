// EMAIL JS
(function() {
    emailjs.init("user_NCVoKpfkDgC3bkJIJPFHw");
})();

function sendMail(contactForm) {
    emailjs.send("gmail", "approach_people", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            // Showing modal if form valid
            function(response) {
                $('.modal').modal('show');
                $(".close-modal").click(function() {
                    location.reload();
                });
            },
            // Alerting message below if form not valid
            function(error) {
                alert("Fail, please try again.");
            });
    return false; // To block from loading a new page
}