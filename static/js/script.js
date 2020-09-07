$(document).ready(function () {
  $(".sidenav").sidenav();
  $("select").formSelect();
   $("#posted_date").datepicker({ 
    });
    // Getting todays date for Date Posted input field
    // source: https://stackoverflow.com/questions/233553/how-do-i-pre-populate-a-jquery-datepicker-textbox-with-todays-date#:~:text=You%20must%20FIRST%20call%20datepicker,to%20get%20the%20current%20date.&text=var%20myDate%20%3D%20new%20Date()%3B,%2B%20'%2F'%20%2B%20myDate.
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

