# Lydia collect automator

## About the license : 

This project is licensed under the terms of the GNU General Public License version 2 (GPLv2). You can find a copy of the GPLv2 license in the "LICENSE" file in the root directory of this repository.

The GPLv2 grants users the freedom to use, modify, and distribute this software. However, users must also make the source code available to recipients of the software and include a copy of the GPLv2 license with any modified versions of the software.

For more information on the terms of the GPLv2 license, please see the "LICENSE" file.

# Core
The goal of this repo is to define a function : 

-  taking a URL and a list of attributes as input
-  able to detect on the URL the presence of a lydia collect link, to open it, to complete the form with the given attribute and eventually to submit it. 

This would enable someone having the program to ensure his presence to all lydia collect events. 

# How it works 

The main function is `watcher_completer`, it takes as input [...].

- `watcher_completer()` calls `page_watcher()`, which keeps an eye on a facebook event and watch for a lydia collect link post, and then clicks on it. 

    - Note that `page_watcher()` takes as input a link to the page to look into, and a pattern to recognize in the link. + a waiting time and a step time too refresh the page and watch for new posts. 

- Then, `watcher_completer()` calls `lydia_form_filer()`, which will complete the lydia form
- To complete this form, `lydia_form_filer()` : 
  - takes as input a dictionary with key values and its attributes to complete
  - will complete all missing text fields with "Je ne sais pas" and all scrolling menus with their first option.

- At first, there will be a logger function which would log one to facebook ! 

# Online version (07/01/2023)
The goal is now to put a version online, with a cool interface. 

## About fields and options
In this interface, one should be able to input his credentials (there won't be kept in memory or whatever, the user would have to input them for each utilization), the facebook page he wants to look into, and a dictionnary with all fields he wants to complete. 

Then, there should be toggles than a user could activate or not : 

- One to say if he wants the form to be directly completed or if he wants to submit it manually after all fields are completed. 

- One to ask if the user wants to accept the cookies manually and/or to enter his credentials manually (in this case, my bot will just be useful to complete the form and send it)

## About the functioning itself

How a user will be able to use the bot ? Well, I'm thinking of a credentials for it, with a limited number of uses per person. I could imagine a system of paid recharges with let's say 5 or ten shotguns for 1 euro or I don't know. I have to see if it's legal too... The recharge system enable the users to freely exchange their credentials, since they have only limited shotguns. 

The problem I encountered with this project is that even if the bot works correctly locaaly, I can't find a way to use the python library Selenium within a website. For instance, the PyScript lbrary doesn't support Selenium. Until I find a solution, this project will be paused. 
