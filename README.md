# LETS BAKE

A recipe search engine for users to find, upload, edit and delete baking recipes.

## UX
This website is design for individuals looking for baking recipes and inspiration. Users will be able to search using keywords for recipes. Use a dropdown menu to browse categories of recipes, as well as upload, edit and delete their own recipes. This site will inspire users to get their mixing bowls out through a "Recipe of the Week" and "Recently Added"

![Image of wireframe1](venv/static/images/LetsBakeWireframe1.jpg)
![Image of wireframe2](venv/static/images/LetsBakeWireframe2.jpg)

## Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
Another feature idea

## Technologies Used
Python
Flask
MongoDb
Bootstrap
Html
CSS


## Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
Debugging, during first master push to heroku I kept receiving an error that the app was crashing. Through thorough checking and trying different fixes it was eventually solve through using gunicorn in the profile and update the requirements.txt. This resolved the issue through trying different fixes I also found an article to Config Vars for Deploy-Specific Settings for Heroku [Read that Article here](https://blog.heroku.com/config-vars). This enabled me to secure the secret key without having it displayed anywhere in my code. Pretty cool.
If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
### Content
The text for section Y was copied from the Wikipedia article Z
### Media
The photos used in this site were obtained from ...
### Acknowledgements
I received inspiration for this project 