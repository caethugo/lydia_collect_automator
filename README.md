# Lydia collect automator

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

