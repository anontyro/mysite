# [Alexwilkinson.co](https://alexwilkinson.co)

The current code for my own personal site. Written in Django 2.0 the site runs off a SQLite database for simplicity and
due to the low load it is a quick and easy method to publish.

The site was developed in mid 2016 and went live Wednesday August 17 2016.

The site features a fully featured blog that uses mark-up to display the posts style. The site uses Djangos security methods
built in and has the ability for the user to login to use full CRUD operations on the blog posts.

### Updates
The original site was build in Django 1.9 and a lot has changed since then, I have sinced gained a lot more experience meaning a lot of the areas that were rather blurry previously have made much more sense going over the site again. It gave me time to understand more of the base and really get into Python a lot more. Django has proven to be a fantastic platform to work with and I feel it provides a great platform.

### Server Migration Jan 2018
Due to the previous server being slightly outdated and although I built my code for Python3 it was being served on Python2 and as a result I thought it would be easier to just move servers with this new build. It took a few days and a lot of errors but the site is backup and running and everything seems stable, at least for now. This provided more learning figuring out how to setup a Ubuntu 16.04 server and install everything correctly. Luckily Digital Ocean have many great guides that helped greatly in the migration

### Version 2.0
I have gone back over and tweaked or changed most aspects of the site, I moved the code to Django 2.0 which meant some rewrites and updates but overall that went quite smoothly with only a few setback which is to be expected. With the update I added in a portfolio section and the Django Rest-Framework which has allowed me to connect the database with a RESTful API, although only the basic routes are in place I am looking forward to utilising these with Electron as I have an idea for a project involving that.

### Future
The main aspects have been updated now, of course a lot of the backend is messy and does still need more work, I hope to spend more time on the site overall this year than I did last but at the sametime I do like to spend my time elsewhere so I only expect minor updates and changes as the year goes on. I do hope to switch out the portfolio page with an Angular 5 webapp eventually, maybe towards the end of the year.
