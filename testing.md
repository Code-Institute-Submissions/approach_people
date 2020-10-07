# Approach People/Testing

## Table of Contents
1. [Manual Testing](#manual-testing)
2. [Code Validation](#code-validation)
3. [Browser and mobile testing](#browser-and-mobile-testing)
4. [Additional Testing](#additional-testing)
## Manual Testing
#### Manual tests have been done throughout the development of the project.
#### The following test scenarios confirms that the website is behaving accordingly, and that bugs have been taken care of:
### Bugs Encountered & Fixed
#### Throughout development, there were many tiny fixes found by completing ongoing checks of functionality.
* Constant iterations of styling to fix responsiveness issues across devices.
* Contact form was not being refreshed once the form was submitted
 * Once submit button was clicked, modal appeared but content from form stayed, to fix this issue, on click event was added on close modal button to reloads the website, works now with no issues.
* Labels for datepickers and search bar were causing an issue while clicking on it. Focus was off so click had to be correctly on the line for it to work.
 * Fix for it was to change labels for placeholders.
* Search bar was not showing html text if no results were in DB
 * Had to count all documents in DB to make this work, once variable was declared and proper logic was in jobs-posted.html, this issue was fixed.
### Functional Testing
#### Landing Page
* Successfully tested that all nav links redirect to the appropriate route.
* Successfully tested that buttons are redirecting to the appropriate route.
#### Look for Job
* Look for a Job - displays correctly all jobs posted with images and text showing correctly
* Search Bar - Finds searched word with no issues if it exists in DB, in case there is no such word, red text is showing correctly on middle of the page.
* Apply - Redirects to a default mailing service, no issues there.
* Edit Job - Takes all information from DB regarding clicked job and displays correctly in type of form, any of the field can be changed
* Delete Job - Pop up modal appears on click asking user to confirm selected action, if user confirms the action, job is deleted successfully from DB, otherwise user is back to all Jobs Posted.
* Job Title - Clicking on it, additional informatio is shown about clicked job, no issues here, Apply, Edit Job and Delete Job are working normally with no issues.
* Pagination - It is showing correct number of jobs per page, and also creates another number if there is more jobs.
#### Post a Job
* Showing correct categories from DB
* Takes all user input without any issue, if user does not provide url, default img is loaded
#### Contact Us
* Form is connected with my email address using EmailJS, once user provides all information and it is passing form validation, pop up modal appears giving feedback to the user while I am recieving email with users information.
## Code Validation
### [Autoprefixer](https://autoprefixer.github.io/)
+ Added prefixes to CSS for different browsers.
### [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
+ Couple of warnings and erros were found on all .html files apart from base.html due to jinja templating language.
+ Other than mentioned above, there were no errors or warnings in index.html.
### [HTML Formatter](https://webformatter.com/html)
+ Formatted all .html files for better indentation.
### [W3C CSS Validator](https://validator.w3.org/)
+ No errors or warnings were found on style.css.
### [CSS Formatter](https://www.cleancss.com/css-beautify/)
+ Formatted style.css.
### [JSHint](https://jshint.com/) 
+ Couple of warnings for undefined variable ("$"), it was reffering to JQuery selector and it can be ignored.
### [PEP8 online](http://pep8online.com/)
+ Couple of warnings for "continuation line under-indented for visual indent" apart that code was fully compliant.
## Browser and mobile testing
+ Default img was showing as extended on Safari, this was fixed by adding "display: block" to child of an targeted element.
+ No issues were found on Google Chrome, Mozilla Firefox, Microsoft Edge and Opera.
+ No issues were found on any mobile devices.
#### All testing was performed using:
+ Google Chrome Dev Tools.
+ Android and IOS. 
+ Desktop - tested display on different screen sizes.
+ Mobile Phones and Tablets - All emulated devices offered in Google Dev Tools as well as physical devices such as Samsung Galaxy Note 8, Samsung Galaxy Edge 7, Huawei Mate 20 Lite and iPad.
## Additional Testing
#### I asked my family and friends to check the website and it's functionality out on the laptop and phone devices and they could not find errors within or the responsiveness of the site.