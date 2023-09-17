# Bridge Property Estate Agents

Bridge Property Estate Agents is a fictional property business that's located in Celbridge, Kildare. The website is made to allow potential customers to browse houses that are for sale nationwide. If customers are interested in viewing a property, they can get in contact with an estate agent via a form. Staff can then easily manage inquries and listings.

## Table of Contents
- [Styling](#styling)
- [Technologies](#technologies)
- [Testing](#testing)

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
