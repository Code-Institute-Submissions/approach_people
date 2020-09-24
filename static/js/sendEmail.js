function sendMail(contactForm){
    emailjs.send("gmail", "approach_people",{
        "from_name":contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response){
            $('.modal').modal('show');
            $(".close-modal").click(function(){
                location.reload();
            });
        },
        function(error){
             alert("Fail, please try again.");
        });
    return false;
}