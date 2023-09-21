# Bridge Property Estate Agents

Bridge Property Estate Agents is a fictional property business that's located in Celbridge, Kildare. The website is made to allow potential customers to browse houses that are for sale nationwide. If customers are interested in viewing a property, they can get in contact with an estate agent via a form. Staff can then easily manage inquries and listings.

## Table of Contents
- [User-Experience-Design](#user-experience-design)
- [Styling](#styling)
- [Technologies](#technologies)
- [Testing](#testing)

## User-Experience-Design
### Site Goals
The site is aimed for estate agents to be able to display a list of houses for sale and have the capacity for updating and removing listings as is necessary.
The site also allows users to view houses on an intuitive and easy to use website. Users can contact estate agents about any house on the site and logged in users are able to see which listings they've inquired about on their dashboard.

### Database-Design
The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected to the listings, realtors, account and contact apps, linked by key relationships.

### Security
Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository. In production, these variables were added to the heroku config vars within the project.

## Styling
### Colour
The main colours used were #1e00a6 and #0c0042 in a linear gradient to the bottom right to produce a dark blue colour.

### Typography
The Nunito font was used throughout the website. This font is from google fonts and was imported into the style sheet.

### Imagery
The Website logo was made using icons8 in white and blue

The listing images were taken from Pexels which is a royalty free image site.

## Technologies
- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- Javascript
  - Particle JS was used for the animation
- Python
  - Python was  used for the application using the Django Framework.
- Github
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- CodeAnywhere
  - The website was developed using CodeAnywhere IDE
- Font Awesome
  - This was used for various icons throughout the site
- Icons8
  - This was used for various icons throughout the site
 
**Python Modules Used**
* messages - Used to pass messages to the toasts to display feedback to the user upon actions

**External Python Modules**
* cloudinary==1.29.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django== - Framework used to build the application
* gunicorn== - Installed as dependency with another package

## Testing
Ensure a user can sign up

Steps:

1. Head over to site, click the hamburger icon to reveal options and click Register
2. Enter details as required
3. Click Register

Expected:

The newly registered user is logged in and brought to the dashboard page

Actual:

The newly registered user is logged in and brought to the dashboard page

<hr>
Ensure a user can log out
Steps:
1. Login to the website
2. Click hamburger icon to reveal logout option and click it
3. User should be redirected to home page
Expected:
User is logged out
Actual:
User is logged out
<hr>
Ensure a user can query a listing
Steps:
1. Either on the home page or on the listings page, click the more info button
2. Click the 'Make An Inquiry' button and a modal will pop up
3. Property line will be populated with listing address
4. Fill out the form, logged in users will have some details prepopulated
5. When all details are filled out click send
Expected:
Form submits, the modal disappears and user is still on the listing page
Actual:
Form submits, the modal disappears and user is still on the listing page
<hr>
Ensure a user booking can be deleted
Steps:
1. Navigate to user dashboard
2. Logged in users can see what listings they've queried
3. Click the delete button
4. Listing will be deleted and user will remain on the dashboard page
Expected:
Listing is deleted and user remains on their dashboard
Actual:
Listing is deleted and user remains on their dashboard
<hr>
Ensure staff can access the staff dashboard
Steps:
1. Click the hamburger icon and click log in
2. Staff are redirected to staff dashboard which shows all listings that have been queried
Expected:
Staff are redirected to the staff dashboard
Actual:
Staff are redirected to the staff dashboard
<hr>
Ensure staff can create a listing when logged into the website
Steps:
1. Click the hamburger icon and click log in
2. Staff are redirected to staff dashboard
3. At the bottom of the page, click 'Create Listing'
4. Staff is redirected to another page with a form allowing them to create a listing
5. If is published is checked and submit button is clicked, the new listing will be available to view
6. When the submit button is clicked, staff will be redirected to the staff dashboard
Expected:
Staff can create a new listing and publish it on the website when logged in
Actual:
Staff can create a new listing and publish it on the website when logged in
<hr>


## Deployment

### Version Control
The site was created using the CodeAnywhere editor and pushed to github to the remote repository
The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.
The live link can be found here:

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.
