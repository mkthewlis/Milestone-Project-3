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

### Validation

#### HTML
My HTML code was passed through the [W3C Markup Validation Service](https://validator.w3.org/).
Doing so brought up the following errors, all related to creating my HTML files with the use of Jinja templates.
- Bad value: HTML file structure
As each HTML file is an extension of base.html, the individual documents do not declare the doctype, set the language or include a head element. This error was therefore present on each file I tested, except for base.html that fulfilled the requirements. This error was to be expected and did not lead to any changes.
![Error: HTML file structure](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/error_html_structure.png)

- Bad value: 'url for'
As with the first error, this was common across all HTML template files. It was also to be expected, as the validator was not anticipating to find `href="...url_for..."`
![Error: url for](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/error_url_for.png) 

#### CSS
I checked my CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). 
This test passed without any errors.

#### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript code.
This highlighted an error that the variable 'Clipboard' was undefined, relating to the following line of code:
![Error: Clipboard](https://github.com/mkthewlis/Milestone-Project-3/blob/master/static/images/readme_images/error_clipboard.png) 
However, as I followed the instructions on how to use the clipboardjs API directly from their own website, I decided not to make any changes regarding this error. 
The process that I followed to integrate clipboard.js into my code can be found on here: [clipboardjs.com](https://clipboardjs.com/)

### Testing compatibility with different browsers

I manually tested the website on the following web browsers, checking that buttons, responsiveness and design worked as planned:
- Google Chrome 
- Mozilla Firefox 
- Apple Safari
