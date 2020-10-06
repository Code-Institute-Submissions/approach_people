# Approach People

### [Live Heroku App Link](https://approach-people.herokuapp.com/)
### [GitHub repository Link](https://github.com/todorr92/approach_people) 

![alt text](wireframes/Mockup_Generator.png "Mockup Generator")

## Summary
#### Approach People is an application that allows users to post jobs. Each entry can be easily searchable, and also updated or deleted.
## Table of Contents
### 1. [UX](#ux)
### 2. [Features](#features)
### 3. [Technologies Applied](#technologies-applied)
### 4. [Tests](#tests) 
### 5. [Deployment](#deployment)
### 6. [Credits](#credits)

# UX
### Project Goal
#### The user's experience was at the front and center during the development of this project. One of the goals of the project was to create an application that is simple and satisfying to use. For this reason, Approach People was built to be usable across all screen sizes.
### User Stories
* As a user, I want to check out posted jobs.
* As a user, I want to post certain jobs, and get ideal candidates.
* As a user, I want to update a job, if some details were changed.
* As a user, I want to be able to delete a job, if it is not longer relevant
* As a user, I want to search through entries I have created, to find a specific item.
* As a user, I want to be able to upload images of company logos, so that they are easily recognazible.
* As a user, I want to be able to read through my posted jobs on a mobile device, so that I can access the information from anywhere.
### Design Choices
##### The application was built using bootstrap and its responsive grid system. Some of default bootstrap style was overriden by a [style.css](static/css/style.css).
#### Color Scheme
* **Body** - used #e0f2f1 (aqua) for a background color
* **Footer and Nav Bar** - used #17a2b8 (dark blue) as a background color while text color was #F8F8FF (ghost white)
* **Text** - simple #fff (white) color was used for a text to have a nice contrast with background colors
* **Buttons** - For landing buttons darker shade of blue was used (#01a8c1), for submit buttons #17a2b8 (dark blue) and for action buttons such as Apply, Edit Job and Delete #26a69a (dark cyan) were used as primary colors
#### Fonts
* [Do Hyeon](https://fonts.google.com/?query=Do+Hyeon) - used only in project name (Approach People)
* [Noto Sans KR](https://fonts.google.com/?query=Noto+Sans+KR) -  used for rest of the website
## Wireframe Mockups:
#### During the design process I drew up wireframes using [Balsamiq](https://balsamiq.com/)
![alt text](wireframes/Approach-People.pdf "Wireframes")
## Features
### Existing Features
#### Home
* Navigation bar with four links: Home, Look for a Job, Post a Job and Contact Us
* Simple and appealing background image, with two buttons leading to all jobs posted or to post a job
#### Look for Job
* Shows all current jobs posted in a container with a image(company logo) and few job details such as job name, company name, salary, job location, date posted and employment type.
#### Post a Job
* Takes all information in a form, populating DB with information given by user
#### Job Details
* Goes into more information about specific job clicked by showing job description, job requirements, company telephone number, email address, due date and posted by
#### Apply
* By clicking on Apply button default mailing service will promt to open with pre set subject and email to address using mailto function.
#### Edit
* Takes all information from Mongo DB, once change is made DB is updated
#### Delete
* Deletes a job from DB, but before doing so, pop up modal is triggered asking user to confirm the action.
#### Contact Us
* Contact us form connected with my email address using EmailJS
### Features Left to Implement
* User Authentication
* User profile creating where each user could store their cover letter and CV
* A password recovery system, that would send an email to a user's account, needs to be implemented.
## Technologies Applied:
+ HTML, CSS and JavaScript programming languages
+ Python
+ Flask
+ [Google Fonts](https://fonts.google.com/) 
+ [Bootstrap](https://getbootstrap.com/) 
+ [Materialize](https://materializecss.com/)
+ [Jquery](https://jquery.com/)  
+ [Github](https://github.com/) 
+ [Gitpod](https://gitpod.io/workspaces/)
+ [EmailJS](https://www.emailjs.com/)
+ [Mockup Generator](https://techsini.com/multi-mockup/index.php)
# Credits

### Content
+ Job specs  were taken from [jobs.ie](https://www.jobs.ie/)

### Media
+ The photos used in this site were obtained from [Pexels](https://www.pexels.com/)

### Code Credits
+ [CSS ANIMATED BUTTONS](https://demos.themesfinity.com/css-buttons/) - Button style on landing page
+ Other helpful resources were [w3schools.com](https://www.w3schools.com/), [CSS Gradient](https://cssgradient.io/), [Stack Overflow](https://stackoverflow.com/), [Material Design](https://material.io/), [MDN web docs](developer.mozilla.org), [Stack Abuse](stackabuse.com) and [CSS Tricks](https://css-tricks.com/)


### Acknowledgements
#### I would like to thank my mentor, Akshat Garg for his support, insights and advices. 
#### I would also like to thank Slack community for help provided when needed.
## Disclaimer
#### Please note that content on this website is educational purpose only