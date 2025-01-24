import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def generate_moves():
   left_move = -random.randint(4, 7)
   net_move = random.randint(1,3)
   right_move = abs(left_move) + net_move
   return left_move, right_move, net_move

def generate_options(left_move, right_move, net_move):
   correct_answer = f"{left_move} + (+{right_move}) = {net_move}"
   wrong_answers = []
   
   while len(wrong_answers) < 4:
       wrong_left = -random.randint(3, 7)
       wrong_right = random.randint(5, 9) 
       wrong_result = wrong_left + wrong_right
       wrong_answer = f"{wrong_left} + (+{wrong_right}) = {wrong_result}"
       
       if wrong_answer != correct_answer and wrong_answer not in wrong_answers:
           wrong_answers.append(wrong_answer)
   
   options = [correct_answer] + wrong_answers
   random.shuffle(options)
   return options, correct_answer