## Testing

To return to the previous document, please click [here](https://github.com/mkthewlis/Milestone-Project-3/blob/master/README.md).

### Testing User Stories

The following tests were conducted to test the experience of each user outlined earlier in the 'User Stories' section.

#### Project stakeholders

- As the creator of this project, I wanted to make sure that users would actually find value in using this app as that would provide an incentive for them to return to it. To achieve this goal, I have created a project that is easy to navigate and intuitive to use, allowing the user to immediately learn how to make the most of its features. There are prompts to sign in or sign up throughout the project, and once a user has signed in, they can navigate the internal pages from their personalised Overview page. Tasks are easy to add, edit, delete and mark as complete, allowing the user to focus on enjoying the process of getting ready to move home, which is the goal of this app.
- I also wanted to make it easy for the community of MoveOn users to share their own tips with other users. This is achieved through the 'Top Tips' page, where users can contribute to the list of tips with their own recommendations. These can only be added when a user has signed in and they can only edit and delete their own recommendations.

#### New users

- The new user who relies on technology for all aspects of their lives would find this app useful when moving homes. They would find that it's easy to set up an account and begin to add, edit and delete their own tasks. They could delegate the tasks to different members of the household and would find it satisfying to watch the 'Completed Tasks' list grow as each one is completed. 
- The young user who has never moved home before would find that this helps them to stay organised. As well as managing their own tasks as the other new user above, they would also be able to find advice and inspiration on the community 'Top Tips' board. As they continue to use the app, they may even add their own tips once settled into their new home.

#### Returning users

- This returning user wanted to share the app with a friend who was about to begin the same process. Sharing the app is easily done with the feature in the footer - when the user clicks the copy icon, the website url is automatically copied with the help of clipboardjs.com. The user can then paste the url in a message to their friend.
- The user who had already created an account and wanted to add more tasks to their list could do so with a few simple steps: they would use the menu bar to navigate to the 'sign in' page, enter their details and click on the 'Add tasks' button when signed in. Once the task is added, they could either click on the link in the flash message to take them back to their task list, or stay on the same page to add another task.

#### Tablet user

- The tablet user would find that the app works just as well on a smaller screen. All features are responsive, including the carousel on the home page that transforms to a list on the smallest screens to improve the user experience.

### Validators and lintners

#### HTML
My HTML code was passed through the [W3C Markup Validation Service](https://validator.w3.org/).
Doing so brought up two errors, both related to creating my HTML files with the use of Jinja templates.
1. *Bad value: HTML file structure*
As each HTML file is an extension of base.html, the individual documents do not declare the doctype, set the language or include a head element. This error was therefore present on each file I tested, except for base.html that fulfilled the requirements. This error was to be expected and did not lead to any changes.

![Error: HTML file structure](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/error_html_structure.png)

2. *Bad value: 'url for'*
As with the first error, this was common across all HTML template files. It was also to be expected, as the validator was not anticipating to find `href="...url_for..."`

![Error: url for](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/error_url_for.png) 

#### CSS
I checked my CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). 
This test passed without any errors.

#### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript code.
This highlighted an error that the variable 'Clipboard' was undefined, relating to the following line of code:

```
let clipboard = new Clipboard('.copy-icon');
```

However, as I followed the instructions on how to use the clipboardjs API directly from their own website, I decided not to make any changes regarding this error. 
The process that I followed to integrate clipboard.js into my code can be found on here: [clipboardjs.com](https://clipboardjs.com/)

#### Python
I used [PEP8](http://pep8online.com/checkresult) to check my Python code.
This test passed without any errors.


### Testing compatibility with different browsers

I manually tested the project on the following web browsers, checking that all aspects worked as planned:
- Google Chrome 
- Mozilla Firefox 
- Apple Safari

This did not lead to any errors or problems.

### Testing the project on different devices

The project has been tested on the following devices:
- Apple MacBook Air 13" 
- Apple MacBook Pro 15" 
- Apple iPhone 8
- Apple iPhone Xs Max
- Apple iPad Air
- Samsung Galaxy
- Huawei p30
- HP EliteBook
- Lenovo Thinkpad

This did not lead to any errors or problems.

### Testing the design's responsiveness on several screen sizes

As I used a 'mobile first' approach to developing this project, I continued to test the responsiveness of the design throughout development process. As I added each new feature to the project, I used Google Chrome's Dev Tools to view the result on different screen sizes. 
Doing so helped me make minor adjustments to the margins, padding and font sizes of different aspects of the project. However, this did help me implement a significant change, as outlined below:

While testing the project, I realised that the carousel feature on the home page did not respond well to small screen sizes. I tried adjusting the size of the font and images alike with the use of media queries but this led to a poor user experience as the design felt "squashed". As a result, I decided to replace the carousel with a list of the same html content in a list form. This made for a much better user experience, as shown below:

*Carousel on a large screen:*


![Carousel large screens](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/carousel_lg.png) 

*Carousel on screens narrower than 767px:*


![Carousel smaller screens](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/carousel_sm.png) 

### Manually testing all aspects of the design

#### Menu bar
- *Logo* - clicking on the logo takes a user back to the home page
- *Home* - as above, clicking on this link returns the user to the home page
- *Sign in* - directs a user to the sign in page
- *Sign up* - directs a user to the sign up page

#### Footer
- Clicking on the copy icon successfully copies the website url
- The return to top arrow scrolls smoothly to the top of the page

#### Home 
- *Sign in button* - directs users to sign in page
- Trying to click this button when a user is already signed in leads to the following flash message error: 'You're already signed in! Sign out first if you want to change account.'

#### Top Tips
- Prompts to encourage users to share their moving tips with the community successfully link to the sign up and sign in pages respectively
- *Sign in button* - directs users to sign in page
- *Sign up button* - directs users to sign up page
- If a user is signed in, the form to submit a tip successfully appears. They can then write a tip and submit the form to share the idea with the community.
- Similarly, a user signed in can edit and delete their tip with the respective modals that pop up to confirm this. They can only do so with tips that they have added from their account. 

#### Sign in
- Trying to submit the sign in form with empty form values does not work as they are required fields
- Submitting the form with a username that doesn't exist leads to the following flash message error: 'We don't have that username on file! Please check your spelling and try again.'
- Submitting the form with the incorrect spelling of the password leads to the following flash message error: 'Oops, it looks like you've entered the wrong combination of username and password. Why not try again?'
- With the correct username and password, a user successfully gets redirected to their 'My Tasks' page
- *Sign up button* - directs users to sign up page

#### Sign up
- Trying to submit the sign up form with empty form values does not work as they are required fields
- Submitting a the form with a username that is already taken leads to the following flash message error: 'Oops, that username already exists! Please try again with another username.'

#### My tasks
- *Add new task button* - user is redirected to add new task form
- If a user has pending tasks in their list, the 'edit', 'complete' and 'delete' buttons function as they should, opening respective modals to confirm the actions
- If a user has complete tasks, the 'delete' button functions as it should
- As the user is in session, they are successfully able to click the 'sign out' button in the menu bar to sign out

#### Add a new task
- Trying to submit the add task form with empty form values does not work as they are required fields
- When filled in, the tasks are successfully added with a flash message confirming this. Within the flash message, the link to return to their 'My Tasks' page works well.
- *My tasks button* - returns a user to their 'My Tasks' page

#### Edit task
- The form is automatically filled with the previous values
- If a user does not fill in the form and returns to their task list, the task maintains the previous values
- *My tasks button* - returns a user to their 'My Tasks' page


[Return to previous document here](https://github.com/mkthewlis/Milestone-Project-3/blob/master/README.md).
