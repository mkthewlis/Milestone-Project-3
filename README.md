# MoveOn

## Code Institute: Milestone Project 3

![MoveOn Responsive Design](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/am_i_responsive.png)

*MoveOn* is an app that aims to help users prepare for relocating to their new home. My aim with this project was to create an app that would be intuitive, useful and enjoyable for households to use. 

Having moved home several times in my life, I know the importance of being well organised before each move. And as I have always relied on lists to help me plan ahead, I also know how useful a checklist can be! 
My idea therefore came from creating a project that would meet the needs of other users who would soon be moving home themselves.

I also wanted to create a community board where users would be able to share their best moving tips with others, thereby providing a useful source of information for those getting ready to move home.

This was the third of four Milestone Projects that made up the Full Stack Web Development Program at *The Code Institute*. The main requirements were to build a full-stack site with the use of HTML, CSS, JavaScript, Python + Flask and MongoDB.

[Click here to view the project live.](https://ms3-move-on.herokuapp.com/)

## Table of contents

- [**UX**](#UX)
    - [Main aims](#Main-aims)
    - [User Stories](#User-Stories)
        - [Project Stakeholders](#Project-Stakeholders)
        - [New Users](#New-Users)
        - [Returning Users](#Returning-Users)
        - [Tablet User](#Tablet-User)
    - [Design Process](#Design-Process)
        - [UX Research](#Design-Process:-UX-Research)
        - [UX Design](#Design-Process:-UX-Design)
    - [Documenting the design process](#Documenting-the-design-process)
- [**Features**](#Features)
    - [Existing features](#Existing-features)
    - [Features left to implement](#Futures-left-to-implement)
- [**Technologies used**](#Technologies-used)
- [**Testing**](https://github.com/mkthewlis/Milestone-Project-3/blob/master/testing.md)
- [**Deployment**](#Deployment)
    - [Local deployment](#Local-Deployment)
    - [Deploying this project to Heroku](#Deploying-this-project-to-Heroku)
- [**Credits**](#Credits)
    - [Content](#Content)
    - [Images](#Images)
    - [Acknowledgements](#Acknowledgements)

## UX

### Main aims

- To create an app that has real-world value for users who are moving homes. 

- To achieve the first aim, it was essential that this app would satisfy all CRUD functions, allowing users to Create, Read, Update and Delete their own moving tasks within their user account.

- To make the website interactive, by adding JavaScript to create a positive user experience.

- To make navigation intuitive, with prompts to guide the user in the right direction if lost and flash messages to confirm their actions.

- To create a design that would be fully responsive on all devices and screen sizes. 

### User Stories

The following User Stories helped me to create a design that would satisfy the needs of several different types of users.

#### Project stakeholders

- I am the creator of this app and want to make sure that it adds value to users to encourage them to return, by ensuring the app is intuitive to use, fully responsive and sleek in design.
- I would like to create a place for the app's user community to upload and share their moving recommendations and tips.

#### New users

- I am a user who relies on apps for all aspects of my life, from finding recipes, measuring the number of steps that I walk and monitoring the temperature of my home. Naturally as me and my family prepare to move, I want to find an app that can help me organise my plan of action.
- I am a young user who has never moved home before but is now getting ready to leave the family home. I want an app to help me stay organised and plan for the upcoming move.

#### Returning users

- I am user who has recently moved home and used this app to help me do so. My friend has now asked for my help in planning their move, so I want to share the app with them. 
- I created an account a few days ago and need to add more items to my moving to-do list.

#### Tablet user

- I am a user who primarily uses an iPad Pro to browse websites. I want to have a good experience on this website and view all the features in an equally aesthetic way. 

### Design Process

#### Design Process: UX Research 
Before beginning the formal design process, I began by researching other similar apps already in circulation. I wanted to see how they decided to structure their design, what I thought they did well and what I would like to do differently for my project. 
My research led me to the following conclusions:
- I wanted to create an app that users could customize with their own tasks and that these would only be accessible to them.
- The design would have to be sleek, simplistic and positive to capture the user's attention and encourage them to use MoveOn as their preferred task app.
- The app would have to provide feedback to the user each time they make changes to their list, keeping them up to date on the changes they've made. 

##### The following websites were used in the research process:
- [monday.com](https://monday.com/)
- [asana](https://asana.com/)
- [Any.do](https://www.any.do/)
- [Microsoft To Do](https://todo.microsoft.com/tasks/)


#### Design process: UX Design

1. Strategy plane: While researching other to-do apps available to users, I realised that there wasn't one specifically aimed at users moving home. This confirmed to me that there were users who's needs had not yet been met; specifically, the need to have an app targeting users who are moving homes. In order to meet their needs, I realised that I would have to keep this particular type of user in mind throughout the design and planning process in order to create a successful app.

2. Scope plane: With the app idea and type of user in place, I began to consider what features would be required to create a successful and useable app. I knew that a user had to be able to create their own account, manage their tasks with the help of the four CRUD functions and find the design easy to navigate as they worked their way through their list of tasks. I also wanted the app to be personalised, with a user's chosen Username to feature in the design (for example, '"Welcome back 'Username!'"). Furthermore, I also wanted to include a feature to allow users to share their ideas with others, and delete and update the tips that they've added on the community board.

3. Strcuture plane: Once I had narrowed down what features I wanted to include, I began to consider the structure of my design. I realised that the website would have to be presentable to external users browsing through the pages with open access, whilst creating certain pages that are only accessible to users logged in with their account. To create this distinction, I decided that the menu bar would change, with standard items being 'Home', 'Top Tips', 'Sign In' and 'Sign Up', whilst users who are logged in would see see same basic items, but would notice 'My Tasks' (instead of 'Sign In') and 'Sign Out' (instead of 'Sign Up'). This decision was made for a better user experience, as I realised that a registered user who was already logged in would not want to see the 'Sign In'/ 'Sign Up' items in their menu bar. I also made the decision that a user would be able to navigate to the 'Edit task' and 'Add new task' pages through button prompts on their 'My Tasks' page, as these functions are only possible when a user is logged in.

4. Skeleton plane: With the concept and structure in place, I began to plan the navigation route through the design. After opening the website, a new user would immediately be able to access the 'Sign Up' page by noticing a button with the same name in the menu bar (and this standard button design would reappear throughout the design to continue to prompt a new user to sign up). Conversely, existing users could either choose to sign in from the menu, or scroll down to the bottom of this page to find a 'sign in' button prompt. If, however, the user does neither of those steps and chooses to click on the next item in the menu - 'Top Tips' - they would see a list of recommended tasks to consider before moving home. This page then contains a prompt for users to add their own tips to the community board - if they are signed in, the form to do so is visible. Otherwise, they are directed to the sign in/ sign up page respectively and the 'submit' form is hidden. From this page, regardless of whether the user chooses to navigate to the 'Sign Up' or the 'Sign In' page, they will see the same basic page structure: a form to either sign up or sign in (depending on the page they clicked on), a prompt to direct them to the other (if they choose the wrong link) and a feature image.
Regardless of which form they complete and submit, they are navigated to a personalized 'My Tasks' page for their account, which either shows their existing tasks if they are a returning user, or a prompt to add tasks if their list is empty. Clicking on the 'Add new task' button takes them to a page to create a new task which is then visible in their list. By clicking on this task, they can either mark it as complete, delete it or edit it (by being redirected to a 'Edit task' page). Once satisfied with their use of the app, they can click on the 'Sign Out' button and return to the external design and the 'Sign In' page.

5. Surface plane: 
    * The main stylistic decision I made early on was to keep the design as sleek, modern and simplistic as possible, to prevent the design from distracting the user from their use of the app. However, I did not want this decision to compromise the user experience, so I chose to rely on illustrations and graphics instead of photos to bring color and life to the app. My search for graphics led me to find [unDraw](https://undraw.co/), which is a great resource of open source illustrations that can be personalised after your chosen HEX color value.
    * With the idea of the type and style of design that I was after, I started a workspace on [Figma](https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=170%3A2) and began experimenting with my wireframes for desktop, tablet and mobile devices. As with my earlier two Milestone Projects, I found it useful to have my hero image in place, as doing so prompts me to choose the tone and theme for the rest of the design. I selected one of the images I had chosen from unDraw and personalised it with a color palette I had created with [coolors](https://coolors.co/), as shown below. I chose this palette as the colors were modern yet toned down to offer a calm and welcoming feeling to users looking for help when planning their move.
    * I turned to Google Fonts to select the fonts for my project. I wanted to find two compatible fonts that were modern and would look good in a light font weight to complement the simplistic design. I found that Roboto and Quicksand met these criteria. 
    * I began to take note of certain features that I would add later on with JavaScript. These included an arrow button in the footer to scroll smoothly back to top, a menu bar that would fill the background color on scroll down and 'copy url' icon to encourage useres to share the app with others.

> Note: Throughout the design process, I kept referring back to my original 'Main Aims', 'User Stories' and preliminary research to make sure that my project was developing as intended.

### Documenting the design process

Selected color palette:
![Color palette created with coolors.co](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/color_palette.png)

Design for desktop devices:
![My workspace on Figma](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/figma_desktop.png)

Design for mobile devices:
![My responsive design for mobile devices](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/figma_mobile.png)

Design for tablet devices:
![My responsive design for tablet devices](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/figma_tablet.png)

[The entire workspace can be viewed on Figma with this link.](https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=170%3A2)

## Features

### Existing Features

This project consists of seven pages, three of which can only be accessed after a user has created an account and signed in.

#### Consistent features across all pages

- The menu at the top of the page and footer are consistent in design and responsive throughout the website. However, the contents of the menu changes depending on if a user is logged in or not.
- The menu bar for users logged in features a 'Sign Out' button where the 'Sign Up' button usually is. When a user in session chooses to sign out, a flash message confirms this action and they are redirected back to the 'Sign In' page.
- Each page features a 'scroll to top' arrow that becomes visible when the user has scrolled down on the page.
- The footer features an icon to copy the URL for ease of sharing the app with others, created with clipboard.js (referenced below). When a user successfully copies the url, they are notified with 'Copied!' being appended to the text. If it fails (for example, without browser support), an alert tells the user the issue and explains how to manually copy the url to share it on.
- Although each page features different illustrations/ graphics, they are all designed with the same color palette and are from the same illustrator for consistency.
- All sign in/ sign up buttons are designed consistently in their respective colors across the app.
- The active page is underlined with a green line to show the user which page their are on.
- All flash messages appear under the menu bar with the same font and background color throughout the app, and fade out with the same JaveScript function after a few seconds.
- If a user has not logged in, they are unable to access the pages closed to users in session as the pages are redirected back to the open pages, with most of these redirections leading to the 'Sign Up' page to prompt them to create an account.

#### Home

- The user sees two short sentences to welcome them in and to help them immediately understand what the purpose of this app is.
- The user then scrolls down to see a carousel feature with three sections, explaining the three steps required to use this app. 
- On smaller devices, the carousel is hidden and the user sees a box with the same information to make the design appropriate on all screen sizes.
- The end of this page provides a prompt for existing users to login with a button that links them to the sign in page.

#### Top Tips

- This page features five standard recommendations for users to consider when moving home, as a way to inspire them to start adding tasks to their own lists.
- It then includes a prompt to encourage active users to add their own recommendations to this community board; if they are signed in, the form to do so appears. If they have not yet signed in or created an account, they are prompted to do so with a prompt that then disappears when they are signed in later.
- When scrolling down, the user then sees a large sign up prompt along with an image - if the prompt is clicked when a user is already signed in, they are flashed a message informing them to sign out before signing up again.
- The bottom of this page features the same prompt to sign in as the Home page for consistency - if this is clicked when a user is already signed in, they are also flashed a message informing them to sign out before signing in again.

#### Sign In

- The existing user is welcomed with a 'Good to see you again' title, followed by a form to complete with their log in details.
- If they enter the wrong password, a flash error message appears to prompt them to check their spelling.
- If they enter a username that doesn't exist in the database, they are prompted to sign up and create an account.
- Users who don't yet have an account are prompted to sign up with a button next to the sign in form.

#### Sign Up

- New users are welcomed with a 'Good to have you onboard!' title, followed by a form to complete with their log in details.
- If they enter a username that already exists, a flash error message tells the user the issue and encourages them to try with another username. 
- Users who already have an account are prompted to sign in with a button next to the sign up form.

#### My Tasks

- Once a user has either signed up or signed in, they are directed to their 'My Tasks' page with an overview of their tasks.
- If they don't have any tasks yet, they are encouraged to begin by adding their first task. The image is also much larger if a user does not have any tasks.
- The 'Add a task' button directs a user to the 'Add a task' page (described below).
- If the user has already created some tasks, these are separated into two lists: Pending and Completed Tasks respectively. Pending tasks can be clicked on to reveal an accordion displaying more information about the task and the following buttons: Complete, Edit, Delete. The 'Complete' button moves the task to the completed list with a flash message to confirm this, the 'Edit' button redirects the user to the 'Edit Task' page (described below) and the 'Delete' button prompts a modal to expand, with a confirmation that the task should be removed completely.

#### Add a new task

- This page contains a form for the user to complete with details about their task, including who it is delegated to and when they should have it completed by.
- Each time a user adds a task, a success message flashes at the top to confirm it has been added.
- When the user is finished adding new tasks, they can return to their 'My Tasks' page with a 'View my Checklist' button or by using the link in the menu bar.

#### Edit task

- Similar to the 'Add a new task' page, this page contains a form for the user to complete and submit. The form is automatically filled with the previous data so the user is reminded of what their task currently is.
- A success messages flashes to confirm the changes they have made to their task.
- The user can choose to navigate back to their tasks with the 'View my Checklist' button or by following the menu bar.

### Features Left to Implement

- I think that there is a lot of potential to further develop this app, which is unfortunately beyond the scope and time frame of this Milestone Project with *The Code Institute*. Most notably, I would consider adding a feature to connect the family account with each individual household member's account. In so doing, each task could be delegated to a family member, which would make it easier for user's to track who should complete a task.

- It could be useful to create a 'profile' page where users could update their information, including changing their password and adding a profile image for each family member.

- I would also consider adding a feature to report bugs found back to me, to be able to improve the app for future users as and when issues are found.

## Technologies Used

### Languages, libraries, databases, frameworks, editors and version control

- HTML5
    * The language used to create add structure and content to the website.
- CSS3 
    * The language used to style the HTML5 elements according to the design colour scheme.
- JavaScript
    * The languge used to make the app interactive, including the use of the clipboard.js functionality. 
- [jQuery](https://jquery.com/)
    * I used the jQuery library to help write the JavaScript code used in this project.
- Python
    * The programming languaged used to create the back-end function of the app.
- PyMongo
    * PyMongo was used as the Python API for MongoDB. This API enabled me to link the data from the back-end database to the front-end app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * The Python microframework used to help write the Python code for this project.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Jinja templating language was used with Flask in the HTML code. This allowed for template inheritance from the base.html file and to link the back-end to the front-end. 
- [MongoDB](https://www.mongodb.com/)
    * This was the selected database chosen to store data in the cloud.  
- [Bootstrap framework](https://getbootstrap.com/) 
    * I used Bootstrap's grid container system as I wanted to design my project with a 'mobile first' approach. I also used Bootstrap's modal, carousel and accordion features to add structure to my content. 
- [Gitpod](https://www.gitpod.io/)
    * I relied on Gitpod's dev environment to write the code for my project.
- [Git Version Control](https://git-scm.com/)
    * I used Git for Version Control to track and record changes to my code and refer back when needed.
- [GitHub](https://github.com/)
    * I used GitHub as my remote repository, to push to and store the commited changes to my app from Git.
- [Heroku](https://www.heroku.com/)
    * I used Heroku as a hosting platform to deploy the live version of my app. 

### Additional tools used
- [Figma](https://www.figma.com/) 
    * Figma helped me design my project, by creating wireframes for desktop, tablet and mobile devices. 
- [FontAwesome](https://fontawesome.com/) 
    * I relied on free FontAwesome icons, including a copy icon, different types of arrows and a 'tick' to show items as complete.
- [unDraw](https://undraw.co/search) 
    * This was the source of all graphics and illustrations used on the app. 
- [TinyPNG](https://tinypng.com/) 
    * I used TinyPNG to compress my image files to try to reduce the loading time for each page. 
- [Google Fonts](https://fonts.google.com/)
    * I used two complementary fonts from Google for my project: Roboto and Quicksand. 
- [Gauger Fonticon Generator](https://gauger.io/fonticon/) 
    * This free interactive Fonticon Generator allowed me to create a fonticon with a Font Awesome icon and style it with the colours from my colour scheme.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    * This was a great tool throughout the project to check whether there were any errors in my HTML and CSS code (as discussed in more detail in the Testing section).
 - [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
- [PEP 8 online](http://pep8online.com/)
    * I used PEP 8 to check that my Python code complied with formatting standards. 

## Testing

Please view the complete testing process in this separate document [here](https://github.com/mkthewlis/Milestone-Project-3/blob/master/testing.md).

## Deployment

This project was developed using Gitpod as the chosen IDE and GitHub as a remote repository. 

The deployed project can be viewed on the following link: [MoveOn: Live Website](https://ms3-move-on.herokuapp.com/)

The project's GitHub repository can be viewed with the following link: [MoveOn: GitHub Repository](https://github.com/mkthewlis/Milestone-Project-3)

### Local deployment

If you would like to work on this project further you can clone it to your local machine using the following steps:

1. Scroll to the top of this repository and click on the "clone or download button"
2. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    * HTTPS: click on the checklist icon to the right of the URL to copy it
    * SSH key: first click on 'Use SSH' then click on the same icon as above
3. Open a new Terminal window in your IDE of choice
4. Change the current working directory to the location where you want the cloned directory.
5. Enter the following command and press 'Enter' to create your local clone:
```
git clone https://github.com/mkthewlis/Milestone-Project-3.git
```

6. Now create a Database that you intend to use for this cloned project with MongoDB.
7. Return to the Terminal and enter the following to install all required dependencies:
```
pip3 install -r requirements.txt
```
8. Create an env.py file with the following content, replacing the 'username','password', 'cluster_name' and 'database_name' with your MongoDB database values:
```
import os

os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" 
```
9. Add your env.py file to .gitignore to make sure your database information is not viewable to others
10. Your cloned version is now ready to run locally with the following command:
```
python3 app.py
```

You can find both the source of this information and learn more about the process with the following link: [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Deploying this project to Heroku 

To deploy the project to Heroku, I used the following steps:

1. I created a Heroku account, signed in and created a new app with a unique name that had not already been taken (this project uses 'ms3-move-on'). I then set the region to the closest to me: 'Europe'.
2. With the app created, I went to the 'Settings' tab and clicked the 'Reveal Config Variables' button. From here, I input the following values:
```
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
IP: 0.0.0.0
PORT: 5000
```
(Note: within the MONGO_URI value, I replaced the 'username','password', 'cluster_name' and 'database_name' with my specific database values. They are kept private for security reasons.)


3. In Gitpod, I created a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
4. I then created a Procfile with the following content within (making sure that 'Procfile' was written with a capitalized 'P'):
```
echo web: python app.py > Procfile
```
5. I then committed these new files with the following:
```
git add .
```
```
git commit -m ""
```
6. With these files committed, I logged in to Heroku using this command and entered my details at the prompt:
```
heroku login
```
7. Once logged in, I linked my Heroku app created above as the remote repository with this command:
```
heroku git:remote -a ms3-move-on
```
8. I then completed the deployment by pushing the projekt to Heroku:
```
git push heroku master
``` 
9. This completed the process of deploying the project to Heroku. Once deployed, I continued to push all changes made to the project to Heroku throughout the remaining development process.

## Credits

### Content

The content of this website is entirely fictional and written by myself.

### Images

The images are all from unDraw, which is an open source of illustrations. More information about their design project can be found on their website: [unDraw](https://undraw.co/).

### Acknowledgements

Thank you to the following people who helped with support and inspiration:

- My mentor Seun Owonikoko for her attention to detail throughout the development process
- The talented *Code Institute* tutor Tim Nelson for his advice, guidance and support
- My classmate Samantha Gore for reviewing my project and code
- And as always, my family and friends for making me countless cups of tea and giving honest feedback throughout
