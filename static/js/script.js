$(document).ready(function () {
  $(".sidenav").sidenav();
  $("select").formSelect();
   $("#posted_date").datepicker({ 
    });
    // Getting todays date for Date Posted input field
    var myDate = new Date();
    var month = myDate.getMonth() + 1;
    var prettyDate = myDate.getDate() + '/' + month + '/' + myDate.getFullYear();
    $("#posted_date").val(prettyDate);
});
$(".datepicker").datepicker({
  selectMonths: true, // Creates a dropdown to control month
  selectYears: 15, // Creates a dropdown of 15 years to control year,
  today: "Today",
  clear: "Clear",
  close: "Ok",
  closeOnSelect: false, // Close upon selecting a date,
});
$(".datepicker").datepicker();

// Reload contact-us.html once modal is closed
$('.close-modal').click(function() {
    location.reload();
});

