# Trivia

**File:** /python3/trivia.py

Changes:

- Moved import from line 147 to the top
- Used black for code style formatting on entire file
- Replace old string formatting with new f-string format
- _current_category: replaced if statements with dict mapping (place_category_mapping)
- _ask_question: created elifs instead of only ifs, print at the end of the function
- changed how_many_players to players_counter
- __main__: subordinated last if to else since if would never be reached otherwise
- __main__: added players via array  
- substituted all len(self.players) by self.players_counter- function ccreated create_wuquestion function or appending qeustionuestions
- function add removed return True because not neccessary and renamed into add_player
- function wrong_answer removed return True becasue not neccessary 
- _did_player_win: changed not(self.purses[self.current_player] == 6) to self.purses[self.current_player] != 6
- wrong_answer & was_correctly_answered: replace the conditional player increment with modulo 
- roll: changed self.places[self.current_player] = self.places[self.current_player] - 12 to self.places[self.current_player] -= 12
- roll: changed self.places[self.current_player] = (self.places[self.current_player] + roll) to self.places[self.current_player] += roll  
- roll: if and else had same code snippets, added below if statement and deleted unneccessary else
- was was_correctly_answered: if and else had same code snippets, added below if statement and deleted unneccessary else
- replace fixed sized array (places, purses, in_penalty_box) for 6 player with dynamically created arrays (depending on real player counter)
- created main function
- created one question_set which includes categories and their question_set
- created question array
- deleted not_winner in main
- restructured ordering of functions