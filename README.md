# UserPersonaToUserStory

UserPersonaToUserStory is a project that aims to help user in converting user persona to user story. To use the app, user must input user persona data to textboxes in the main page. User can preview the inputted user persona before converting it to user story. User story data is saved in history page.

# How to Install
1) Open command prompt and go to project path
2) Clone project repository
3) Install required library
4) Run server using python manage.py runserver
5) Access http://127.0.0.1:8000/ on website

# IMPORTANT
RULES:
1) Pay attention to capitalization; the system is CASE SENSITIVE
2) System will detect [NEEDS] with either ADJ+NOUN or NOUN
    Verb 1 sometimes is detected as NOUN, resulting an incorrect user story
3) Please refrain using VERB - system will most likely create an incorrect result
4) You must put VERB in [GOALS] at THE VERY START OF THE SENTENCE
5) In short, the supported format is:
   [NEEDS] SUBJECT+VERB+ADJ+NOUN/NOUN
    Example:
      I need a good design.
      I love a recommendation system.
   [GOALS] VERB
    Example:
      To help me find something.
      Getting new information.
6) To separate a needs/goals to another, use punctuation that can separate sentence, for example (.) (?) (!)
7) System will print the output based on the inputted needs and goals. Each needs-goals will generate 1 user story. If user input 1 needs and 2 goals, the result will be 1 user story.

# INPUT
Nama: user persona's name
As a: user persona's role
Bio: user persona's bio
Locations: user persona's location
Needs: user persona's needs, must contain adjective+noun OR noun. Needs will be used as output ("I want [needs]...")
Goals: objective or goals of user persona. Needs must contain verb, be it gerund or V1. Goals will be used as output (...so that... [goals]).
Frustrations: user persona's frustration
Behaviours: user persona's behaviour

PREVIEW BUTTON -> redirect user to preview page

# PREVIEW PAGE
Preview page shows the preview of the inputted user persona.
CONVERT BUTTON -> redirect user to convert page

# RESULT PAGE
Result page shows the result; user story will be generated based on the input.
HISTORY BUTTON -> redirect user to history page

# HISTORY PAGE
All generated user story will be stored in history page. User can access the history page through the navigation.
