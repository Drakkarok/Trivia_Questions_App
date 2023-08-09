# Trivia_Questions_App

Short description:
An app that tests your general knowledge about various subjects. All questions are realtime downloaded using opentdb public API. So this means that atleast in theory questions should never repeat and they are always refresed on start!

---

## CONFIGURATION - Difficulty
1. In data.py there are two parameters that are gray out (they are not taken into account):  
"# "category": 18,"  
"# "difficulty": "hard","  
If you want the request to take any of these into account simply remove the #.

Category determines the subjects of the questions:  
1 General Knowledge;  
2 Entertainment: Books;  
3 Entertainment: Film;  
4 Entertainment: Music;  
5 Entertainment: Musicals & Theatres;  
6 Entertainment: Television;  
7 Entertainment: Video Games;  
8 Entertainment: Board Games;  
9 Science & Nature;  
10 Science: Computers;  
11 Science: Mathematics;  
12 Mythology;  
13 Sports;  
14 Geography;  
15 History;  
16 Politics;  
17 Art;  
18 Celebrities;  
19 Animals;  
20 Vehicles;  
21 Entertainment: Comics;  
22 Science: Gadgets;  
23 Entertainment: Japanese Anime & Manga;  
24 Entertainment: Cartoon & Animations.

There are 3 difficulties:  
easy;  
medium;  
hard;  

Feel free to replace any of these two parameters and to modify them!  

---

Build using: 
- tkinter;
- os;
- requests;
- html.

Functions:
- N/A.

Classes:
- (1) UI;
- (2) Data;
- (3) Question_model;
- (4) Quiz_brain.

Methods:
- (1) update_score;
- (1) update_quiz;
- (1) user_input_false;
- (1) user_input_true;
- (1) give_feedback;
- (4) still_has_questions;
- (4) next_question;
- (4) check_answer.
