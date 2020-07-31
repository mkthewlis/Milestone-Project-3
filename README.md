# MoveOn

## Code Institute: Milestone Project 2

![MoveOn Responsive Design](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/am_i_responsive.png)

*MoveOn* is an app that aims to help users prepare for relocating to their new home. My aim with this project was to create an app that would be intuitive, useful and enjoyable to use. 

Having moved home several times in my life, I know the importance of being well organised before each move. And as I have always relied on lists to help me plan ahead, I also know how useful a checklist can be! 
My idea therefore came from creating a project that would meet the needs of other users who would soon be moving home themselves.

This was the third of four Milestone Projects that made up the Full Stack Web Development Program at *The Code Institute*. The main requirements were to build a full-stack site with the use of HTML, CSS, JavaScript, Python + Flask and MongoDB.

[Click here to view the project live.](https://ms3-move-on.herokuapp.com/)

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

#### New users

- I am a user who relies on apps for all aspects of my life, from finding recipes, measuring the number of steps that I walk and monitoring the temperature of my home. Naturally as I prepare to move, I want to find an app that can help me organise my plan of action.
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

2. Scope plane: With the app idea and type of user in place, I began to consider what features would be required to create a successful and useable app. I knew that a user had to be able to create their own account, manage their tasks with the help of the four CRUD functions and find the design easy to navigate as they worked their way through their list of tasks. I also wanted the app to be personalised, with a user's chosen Username to feature in the design (for example, '"Welcome back 'Username!'").

3. Strcuture plane: Once I had narrowed down what features I wanted to include, I began to consider the structure of my design. I realised that the website would have to be presentable to external users browsing through the pages with open access, whilst creating certain pages that are only accessible to users logged in with their account. To create this distinction, I decided that the menu bar would change, with standard items being 'Home', 'Top Tips', 'Sign In' and 'Sign Up', whilst users who are logged in would see see same basic items, but would notice 'My Tasks' (instead of 'Sign In') and 'Sign Out' (instead of 'Sign Up'). This decision was made for a better user experience, as I realised that a registered user who was already logged in would not want to see the 'Sign In'/ 'Sign Up' items in their menu bar. I also made the decision that a user would be able to navigate to the 'Edit task' and 'Add new task' pages through button prompts on their 'My Tasks' page, as these functions are only possible when a user is logged in.

4. Skeleton plane: With the structure roughly in place, I began to plan the navigation route through the design. After opening the website, a new user would immediately be able to access the 'Sign Up' page by noticing a button with the same name in the menu bar. Conversely, existing users could either choose to sign in from the menu, or scroll down to the bottom of this page to find a 'sign in' button prompt. If however the user clicks on the next item in the menu - 'Top Tips' - they would see a list of recommended tasks to consider before moving home. This page then contains a prompt for new users to sign in 

5. Surface plane: 
    * For my design to work, I knew that it would be important to create a theme that would keep the user interested in the topic. Thinking of plastic waste can feel overwhelming, as it is such an intimidating topic with solutions that are not yet fully clear to us. My first design decision was therefore to make the website seem welcoming, rather than daunting, with light colours and images of plastic waste that would not be shocking enough to prevent the user from continuing on (as this would of course prevent them from learning, which is one of the main aims of this project).
    * With this in mind, I started a workspace on [Figma](https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=170%3A1) and began experimenting with my wireframe. As with my first Milestone Project, I found it useful to have my hero image in place to extract complementary colors for the theme from it. I also began designing my logo ideas on [Canva](https://www.canva.com/design/DAD-9OmoVNg/wbnoii0XoGRt1jnc77ivOQ/view?utm_content=DAD-9OmoVNg&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton) as I felt this would be important to the theme of the design. In the end I settled with a blue and yellow theme: the blue (#528FCB) was extracted from the hero image and represents the ocean, whilst the yellow (#F5F862) complements the blue color well and sybolises the hope of solving this problem. As hope is important to keep the user engaged in such a difficult subject, I thought it would be good to balance the blue and yellow together in this way.
    * I turned to Google Fonts to select the fonts for my project. I wanted to find two compatible fonts that would help to both make the design look credible (so users would take it seriously as a source of information), but that would not be intimidating as I want the users to feel motivated to read on. As a result, I settled for Montserrat for my titles and Raleway for the content. 
    * With the wireframes complete, I began experimenting with the quiz in a seperate workspace to create the JavaScript needed to make this aspect of my project work. I created the basic structure and code with HTML and JavaScript and the repository can be found on GitHub [here](https://github.com/mkthewlis/quiz-practice).  


### Sources:
- Coolors - colour picker https://coolors.co/a7e8bd-dce3ed-f6fdf8-f9f6ec-efb7b9-3a2e39
- UnDraw - source of all cartoon images https://undraw.co/search
- Design inspiration - https://www.checkli.com/ and https://monday.com/ 
- Change form colors when active - https://stackoverflow.com/questions/14820952/change-bootstrap-input-focus-blue-glow
- Add list items for each task - https://www.geeksforgeeks.org/todo-list-app-using-flask-python/
- Scroll top JavaScrip - https://www.journaldev.com/5446/how-to-create-scroll-to-top-animation-in-jquery
- Clipboard.js - https://clipboardjs.com/
- Background color jquery code - https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling
