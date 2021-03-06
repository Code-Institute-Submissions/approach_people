$(document).ready(function() {
    $(".sidenav").sidenav();
    $("select").formSelect();
    // Disable selecting any date other then todays one for a input field posted date
    var dateToday = new Date();
    $("#posted_date").datepicker({
        minDate: dateToday,
        maxDate: dateToday,
        showClearBtn: true
    });
});
// Initialize datepicker
 $(".datepicker").datepicker({
     selectMonths: true, // Creates a dropdown to control month
     selectYears: 15, // Creates a dropdown of 15 years to control year,
     today: "Today",
     clear: "Clear",
     close: "Ok",
     closeOnSelect: false, // Close upon selecting a date,
     showClearBtn: true
});
// Showing and hiding extra information in job-details.html depending on which button is clicked
$(".details-btn").click(function() {
    $(".company-details").removeClass("d-none");
    $(".description").addClass("d-none");
});
$(".description-btn").click(function() {
    $(".description").removeClass("d-none");
    $(".company-details").addClass("d-none");
});
// Reload page once close button is clicked in modal
$(".close-modal").click(function() {
    location.reload();
});
