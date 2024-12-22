
import tkinter as tk #tkinter is a python library or a module
from tkinter import messagebox
import pygame
import threading

player1=True
draw= True
pressed= False
isFinished=False
window= tk.Tk() #Tk() is a class that has methods/variables that define that it's a window. This is module.class 
current_index= 0
current_index2=0
X_count=0
O_count=0
player= ''  
window.title("TicTacToe")

class all_window():
    
    def __init__(self):
        global isFinished
        global player 
        self.isFinished= False
        self.frame = tk.Frame(window)
        self.frame['borderwidth'] = 6
        self.frame['relief'] = 'sunken'
        self.frame.grid()
        self.color_purple= "#9e60ff"
        self.color_pink="#ffaee5"
        self.color_white="#ffffff"
        self.color_black="#000000"
        self.color_select= "#ffdef9"
        self.color_pressed= "#c9fefb"
        self.board = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.current_index=0
        self.label1 = tk.Label(self.frame, font=("Comic Sans", 20, "bold"), text=player+ "'s turn",
                         background=self.color_black, foreground=self.color_white)
        self.label1.grid(row=0, column=1)
        player="X"
        self.label1.config(text=player+"'s turn")
        
    def delete(self, event):
        global isFinished
        global current_index
        global player1

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col].config(text='')
        isFinished = False
        player1= True

    def erase(self):
        global player1
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col].config(text='')
        player1= True

    def onclick(self, row= None,col= None):
        isFinished = False
        global player1
        global pressed
        if row is None or col is None:  # If no position is provided
            
            return  # Do nothing and exit the method
        

        
        if (player1 == True and self.board[row][col]['text'] == '' ):
                #to show the indivual's turn i need to access a variable and then replace it with the newer one
                
            self.board[row][col].config(text='X')
            
            player="O"
            self.label1.config(text=player+"'s turn")
            player1= False
            
                    
        elif self.board[row][col]['text'] == '':
            self.board[row][col].config(text='O')
            player="X"
            self.label1.config(text=player+"'s turn")
            player1= True               

        self.win_condition()
        self.draw_condition()
        
    
   

    def game_over(self):
        global X_count, O_count

        if X_count == 3:
            X_count=0
            O_count=0
            self.labelX.config(text="X: " + str(X_count))
            self.labelO.config(text="O: " + str(O_count))

            messagebox.showinfo("Game Over", "Player X wins the game with 3 points!")
            
            
            
        elif O_count == 3:
            X_count=0
            O_count=0
            self.labelX.config(text="X: " + str(X_count))
            self.labelO.config(text="O: " + str(O_count))
            messagebox.showinfo("Game Over", "Player O wins the game with 3 points!")
           

           
            

    def label(self):
        global X_count, O_count
        

        self.labelX = tk.Label(self.frame, font=("Calibri", 15, "bold"), text="X: " + str(X_count),
                               background=self.color_black, foreground=self.color_white)
        self.labelX.grid(row=0, column=0)

        self.labelO = tk.Label(self.frame, font=("Calibri", 15, "bold"), text="O: " + str(O_count),
                               background=self.color_black, foreground=self.color_white)
        self.labelO.grid(row=0, column=2)

    def update_score_labels(self):
        global X_count, O_count
        self.labelX.config(text="X: " + str(X_count))
        self.labelO.config(text="O: " + str(O_count))


    def win_condition(self):
        global draw, isFinished, X_count, O_count
        if draw:
        # Check rows
            for row in range(3):
                if (self.board[row][0]['text'] == self.board[row][1]['text'] == self.board[row][2]['text'] != ''):
                    winner = self.board[row][0]['text']
                    self.handle_win(winner)
                    return

            # Check columns
            for col in range(3):
                if (self.board[0][col]['text'] == self.board[1][col]['text'] == self.board[2][col]['text'] != ''):
                    winner = self.board[0][col]['text']
                    self.handle_win(winner)
                    return

            # Check diagonals
            if (self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != ''):
                winner = self.board[0][0]['text']
                self.handle_win(winner)
                return
            if (self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != ''):
                winner = self.board[0][2]['text']
                self.handle_win(winner)
                return

    def handle_win(self, winner):
        global X_count, O_count, draw, player
        
        if winner == 'X':
            draw = False
            X_count += 1
            player="X"
            self.label1.config(text=player+"'s turn")
            messagebox.showinfo("Round over", "X wins this round!")
            
        elif winner == 'O':
            draw = False
            O_count += 1
            player="X"
            self.label1.config(text=player+"'s turn")
            messagebox.showinfo("Round over", "O wins this round!")
            
        self.update_score_labels()
        self.game_over()
        self.erase()
        draw= True
        

   
    def draw_condition(self):
        global draw, isFinished
        if all(self.board[row][col]['text'] != '' for row in range(3) for col in range(3)) and draw:
            draw = False
            messagebox.showinfo("Game Over", "It's a draw!, No one earns a point.")
            self.erase()
        draw=True

    def move_down(self,event):
        global current_index
        global current_index2 
        self.board[current_index][current_index2].config(background= self.color_pink) #struggled so much because the config(Background) was capitalized and confused me
                                                        #didn't realize how to cycle through, but that would have been taken care of later(would still struggle tho)
                                                        #next time ask for syntax, more clearly, literally a case sensitive issue
        current_index= (current_index+1) % len(self.board)
        

        self.board[current_index][current_index2].config(background=self.color_select)
    def move_up(self, event):
        global current_index
        global current_index2  
        self.board[current_index][current_index2].config(background= self.color_pink) 
        current_index= (current_index-1) % len(self.board)

        self.board[current_index][current_index2].config(background=self.color_select)

    def move_right(self, event):
        global current_index
        global current_index2  
        self.board[current_index][current_index2].config(background= self.color_pink)
        #when at the end of the column, at index2=2, and i press right key, index will increase by 1, becoming 3
        #but then it's 3 modulus 3, which means 0, so it goes back to the first index, first button on that row. 
        current_index2= (current_index2+1) % len(self.board[current_index])
        #if current index2 is 1, and i press right, current index2 increases by 1, it becomes 2, so 2 modulus 3, which is remainder=2.
    #because it's 2 divided by 3. And what is the remainder of that? It is 2 because 3 goes into 2, 0 times, with a remainder of 2

    #and then if it's at index2=0, i press right, index2 becomes 1 % 3, which means remainder 1, because 1/3, gives you remainder of 1
     

        self.board[current_index][current_index2].config(background= self.color_select)

    def move_left(self, event):
        global current_index
        global current_index2  
        self.board[current_index][current_index2].config(background= self.color_pink) 
        current_index2= (current_index2-1) % len(self.board[current_index])
        

        self.board[current_index][current_index2].config(background= self.color_select)

    def mouse_enter(self, event):
        
        event.widget.config(background= self.color_select)
        
        # self.board[current_index][current_index2].config(background= self.color_select)
    def mouse_leave(self, event):
        event.widget.config(background=self.color_pink)  # Reset to default color

    def enter_key(self, event):
         global current_index
         global current_index2
         self.board[current_index][current_index2].invoke()
         self.board[current_index][current_index2].config(background= self.color_pressed)

    def controller_input(self):
        pygame.init()
        pygame.joystick.init()
        self.clock = pygame.time.Clock()

        # Check for joysticks
        if pygame.joystick.get_count() == 0:
            print("No joystick detected.")
            return

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Connected: {joystick.get_name()}")

        while True: # while not isFinished:
            for event in pygame.event.get():
                if event.type == pygame.JOYHATMOTION:  # D-Pad movement
                    if event.value == (0, 1):  # Up
                        self.move_up(event)
                    
                    elif event.value == (0, -1):  # Down
                        self.move_down(event)
                    elif event.value == (1, 0):  # Right
                        self.move_right(event)
                    elif event.value == (-1, 0):  # Left
                        self.move_left(event)
                elif event.type == pygame.JOYBUTTONDOWN:  # Button presses
                    if event.button == 0:  # A button
                        self.enter_key(event)
                    elif event.button == 1:  # B button
                        self.delete(event)
            self.clock.tick(10)
    
# Start the controller input in a separate thread
    
    #iterator
    def print_board(self):
        
        for row in range(len(self.board)): 
            for col in range(len(self.board[row])): 
                self.board[row][col]=tk.Button(self.frame,font=("Comic Sans", 40, "bold"), background=self.color_pink, 
                                                foreground=self.color_purple, width=5, height=2, 
                                                command=lambda rows=row, column=col: self.onclick(rows, column)) #using lambda allows each button to save its location
                                                                                        #otherwise all the buttons will act like it's the last one
                                                                                        #using the saved row=row,col=col values, the onclick takes those parameters
                                                                                        #and runs the logic with those values.
                                                                                        #the onclick is also a function object in this case, that
                                                                                        #is passed to the lambda, so that only when the button is 
                                                                                        #clicked, will it execute the onclick function
                                                                                        #otherwise, with those parameters, the board will already
                                                                                        #have a X placed on it, as if the button has been pushed
                                                                                       
                self.board[row][col].bind("<Enter>", self.mouse_enter)
                self.board[row][col].bind("<Leave>", self.mouse_leave)                                                                                                
                self.board[row][col].grid(row=row+1, column=col)
    



window_obj = all_window()


window_obj.print_board()  # Initialize the board buttons first
window_obj.label()
window_obj.onclick()
window.bind("<Down>", window_obj.move_down)
window.bind("<Up>", window_obj.move_up)
window.bind("<Right>", window_obj.move_right)
window.bind("<Left>", window_obj.move_left)
window.bind("<Return>", window_obj.enter_key)
window.bind("<Delete>", window_obj.delete)
threading.Thread(target=window_obj.controller_input, daemon=True).start()
window.mainloop()



  



