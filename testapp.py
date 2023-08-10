from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line, Rectangle, Ellipse, Triangle
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

from random import randint

#Window.size = (450,800)

players_names = []
Turn = []
color = ['blue','red']
color_dictionary = {'blue': '74/255, 158/255, 237/255, 1','red': '232/255, 53/255, 65/255, 1'}
Simbol = []
Begginer = []
Gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
Plays = [0]
Background = [['1,1,1,1'],['0,0,0,1']]
Button = [['74/255, 158/255, 237/255, 1'],['0.2,0.2,0.2,1']]
Button2 = [['232/255, 53/255, 65/255, 1'],['0.2,0.2,0.2,1']]
Score = [[0,0,0],[0,0,0]]

class Screens(ScreenManager):
	pass

class Menu(Screen):
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)

    def back(self,window,key,*args):
        if key == 27:
            self.accept()

    def on_pre_leave(self):
        Window.unbind(on_keyboard = self.back)

    def black_mode(self):
        if Background[0][0] != '0,0,0,1':
            Background[0], Background[1] = Background[1], Background[0]
            self.update()
            

    def white_mode(self):
        if Background[0][0] != '1,1,1,1':
            Background[0], Background[1] = Background[1], Background[0]
            self.update()

    def update(self):
        screen_color = eval(Background[0][0])
        text_color = eval(Background[1][0])
        with self.menu_screen.canvas.before:
            self.menu_screen.canvas.before.clear()
            Color(rgba=(screen_color))
            Rectangle(size=self.size,pos=self.pos)
        self.text1.color = text_color
        self.text2.color = text_color

    def accept(self):
        accept_popup = MyPopup()
        accept_popup.open()
    def mode(self):
        mode_popup = My2Popup()
        mode_popup.open()

class My2Popup(Popup):
    pass

class MyPopup(Popup):
    pass

class Images(Image):
    def __init__(self,**kwargs):
        super(Images,self).__init__(**kwargs)
        self.update()

    def on_pos(self,*args):
        self.update()

    def on_size(self,*args):
        self.update()

    def update(self,*args):
        screen_color = eval(Background[0][0])
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(screen_color))
            Rectangle(size=self.size,pos=self.pos)

class Boxlayout(BoxLayout):
    def __init__(self,**kwargs):
        super(Boxlayout,self).__init__(**kwargs)
        self.update()

    def on_pos(self,*args):
        self.update()

    def on_size(self,*args):
        self.update()

    def update(self,*args):
        text_color = eval(Background[1][0])
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(text_color))
            Rectangle(size=(self.width*.94,self.height*.9),pos=(self.width*.03,self.height*.55))
            
class Btn(ButtonBehavior,Label):
           def __init__(self,**kwargs):
           	super(Btn,self).__init__(**kwargs)
           	self.update()
           def on_pos(self,*args):
           	self.update()
           def on_size(self,*args):
           	self.update()
           def update(self,*args):
           	color = eval(Button[0][0])
           	color2 = eval(Button2[0][0])
           	self.canvas.before.clear()
           	with self.canvas.before:
           		Color(rgba=(color))
           		Triangle(points=(self.pos[0]-self.size[1]/2,self.pos[1],self.pos[0],self.pos[1],self.pos[0],self.pos[1]+self.size[1]))
           		Triangle(points=(self.pos[0]-self.size[1]/2,self.pos[1]+self.size[1],self.pos[0],self.pos[1]+self.size[1],self.pos[0],self.pos[1]))
           		Rectangle(size=(self.size[0]/2,self.size[1]),pos=(self.pos))
           		Color(rgba=(color2))
           		Rectangle(size=(self.size[0]/2,self.size[1]),pos=(self.pos[0]+self.size[0]/2,self.pos[1]))
           		Ellipse(size=(self.size[1],self.size[1]),pos=(self.pos[0]+self.size[0]-self.size[1]/2,self.pos[1]))
           def on_press(self,*args):
           	if Button[0][0] != '0.2,0.2,0.2,1':
           		Button[0], Button[1] = Button[1],Button[0]
           		Button2[0], Button2[1] = Button2[1], Button2[0]
           		self.update()
           def on_release(self,*args):
           	if Button[0][0] == '0.2,0.2,0.2,1':
           		Button[0], Button[1] = Button[1], Button[0]
           		Button2[0], Button2[1] = Button2[1], Button2[0]
           		self.update()

class Btn2(ButtonBehavior,Label):
    def __init__(self,**kwargs):
        super(Btn2,self).__init__(**kwargs)
        self.update()
    def on_pos(self,*args):
        self.update()
    def on_size(self,*args):
        self.update()
    def update(self,*args):
        color = eval(Button[0][0])
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(color))
            Ellipse(size=(self.size[1],self.size[1]),pos=(self.pos[0]-self.size[1]/2,self.pos[1]))
            Rectangle(size=(self.size),pos=(self.pos))
            Ellipse(size=(self.size[1],self.size[1]),pos=(self.pos[0]+self.size[0]-self.size[1]/2,self.pos[1]))
    def on_press(self,*args):
        if Button[0][0] != '0.2,0.2,0.2,1':
            Button[0], Button[1] = Button[1],Button[0]
            self.update()
    def on_release(self,*args):
        if Button[0][0] == '0.2,0.2,0.2,1':
            Button[0], Button[1] = Button[1], Button[0]
            self.update()

           
class Names(Screen):
    def on_pre_enter(self):
        self.update()
        Window.bind(on_keyboard=self.back)

    def back(self,window,key,*args):
        if key == 27:
            self.name_1.text = ''
            self.name_2.text = ''
            self.message.text = ''
            App.get_running_app().root.current = 'menu'
            
    def on_pre_leave(self):
        Window.unbind(on_keyboard = self.back)

    def update(self):
        screen_color = eval(Background[0][0])
        text_color = eval(Background[1][0])
        self.name_screen.canvas.before.clear()
        with self.name_screen.canvas.before:
            Color(rgba=(screen_color))
            Rectangle(size=self.size,pos=self.pos)
        self.message.color = text_color
        self.text1.color = text_color
        self.text2.color = text_color
    def on_pos(self,*args):
        self.update()
    def on_size(self,*args):
        self.update()
    def players(self):
        if self.name_1.text != '' and self.name_2.text != '':
            players_names.append(self.name_1.text)
            players_names.append(self.name_2.text)
            self.parent.get_screen('choose').ids.name_1.text = players_names[0]
            self.parent.get_screen('choose').ids.name_2.text = players_names[1]
            x = randint(0,1)
            Turn.clear()
            Turn.append(x)
            Begginer.append(x)
            self.parent.get_screen('choose').ids.message.text = f"{players_names[x]} você venceu, escolha um símbolo: "
            self.parent.get_screen('choose').ids.message.color = eval(color_dictionary[(f'{color[Turn[0]]}')]) 
            self.parent.current = 'choose'
        else:
            self.message.text = "Insira nomes para jogar"

class Choose(Screen):

    def on_pre_enter(self):
        X = self.parent.get_screen('choose').ids.image_X
        O = self.parent.get_screen('choose').ids.image_O
        Images.update(X)
        Images.update(O)
        self.update()
        Window.bind(on_keyboard=self.back)

    def back(self,window,key,*args):
        if key == 27:
            Begginer.clear()
            players_names.clear()
            Simbol.clear()
            self.start_button.opacity = 0
            self.start_button.disabled = True
            self.image_X.source = 'greyX.png'
            self.image_O.source = 'greyO.png'
            App.get_running_app().root.current = 'names'
            
    def on_pre_leave(self):
        Window.unbind(on_keyboard = self.back)

    def update(self):
        screen_color = eval(Background[0][0])
        text_color = eval(Background[1][0])
        self.choose_screen.canvas.before.clear()
        with self.choose_screen.canvas.before:
            Color(rgba=(screen_color))
            Rectangle(size=self.size,pos=self.pos)
        self.text1.color = text_color
        self.text2.color = text_color
    def on_pos(self,*args):
        self.update()
    def on_size(self,*args):
        self.update()

    def choose_x(self):
        self.image_X.source = f'{color[Turn[0]]}X.png'
        self.image_O.source = f'{color[1 - Turn[0]]}O.png'
        Simbol.insert(Turn[0],"X")
        Simbol.insert(1 - Turn[0],"O")
        self.start_button.opacity = 100
        self.start_button.disabled = False
    def choose_o(self):
        self.image_O.source = f'{color[Turn[0]]}O.png'
        self.image_X.source = f'{color[1-Turn[0]]}X.png'
        Simbol.insert(Turn[0],"O")
        Simbol.insert(1 - Turn[0], "X")
        self.start_button.opacity = 100
        self.start_button.disabled = False

    def start_game(self):
        self.parent.get_screen('game').ids.result_text.text = f' {players_names[Turn[0]]}, é a sua vez'
        self.parent.get_screen('game').ids.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        self.parent.get_screen('game').ids.name_1.text = f'{players_names[0]}'
        self.parent.get_screen('game').ids.name_2.text = f'{players_names[1]}'
        self.parent.get_screen('game').ids.score_1.text = f'{Score[0][0]}  {Score[0][1]}  {Score[0][2]}'
        self.parent.get_screen('game').ids.score_2.text = f'{Score[1][0]}  {Score[1][1]}  {Score[1][2]}'
        self.parent.current = 'game'
		
class Game(Screen):
    def on_pre_enter(self):
        self.update()
        gameboard = self.parent.get_screen('game').ids.game_board
        Boxlayout.update(gameboard)
        image1 = self.parent.get_screen('game').ids.button1_image
        Images.update(image1)
        image2 = self.parent.get_screen('game').ids.button2_image
        Images.update(image2)
        image3 = self.parent.get_screen('game').ids.button3_image
        Images.update(image3)
        image4 = self.parent.get_screen('game').ids.button4_image
        Images.update(image4)
        image5 = self.parent.get_screen('game').ids.button5_image
        Images.update(image5)
        image6 = self.parent.get_screen('game').ids.button6_image
        Images.update(image6)
        image7 = self.parent.get_screen('game').ids.button7_image
        Images.update(image7)
        image8 = self.parent.get_screen('game').ids.button8_image
        Images.update(image8)
        image9 = self.parent.get_screen('game').ids.button9_image
        Images.update(image9)
        restart = self.parent.get_screen('game').ids.restart_image
        Images.update(restart)
        home = self.parent.get_screen('game').ids.home_image
        Images.update(home)
        Window.bind(on_keyboard=self.back)

    def back(self,window,key,*args):
        if key == 27 and Plays[0] == 0:
            self.restart_game()
            Begginer.append(1 - Begginer[0])
            del Begginer[0]
            Turn.clear()
            Turn.append(Begginer[0])
            App.get_running_app().root.current = 'choose'
            
    def on_pre_leave(self):
        Window.unbind(on_keyboard = self.back)

    def update(self):
        screen_color = eval(Background[0][0])
        text_color = eval(Background[1][0])
        self.button1_image.color = screen_color
        self.button2_image.color = screen_color
        self.button3_image.color = screen_color
        self.button4_image.color = screen_color
        self.button5_image.color = screen_color
        self.button6_image.color = screen_color
        self.button7_image.color = screen_color
        self.button8_image.color = screen_color
        self.button9_image.color = screen_color
        self.game_screen.canvas.before.clear()
        with self.game_screen.canvas.before:
            Color(rgba=(screen_color))
            Rectangle(size=self.size,pos=self.pos)

    def on_pos(self,*args):
        self.update()
    def on_size(self,*args):
        self.update()
        
    def game_result(self):
        text_color = eval(Background[1][0])
        validade = 0
        for i in range(0,7,3):
            if Gameboard[i] == Gameboard[i + 1] and Gameboard[i] == Gameboard[i + 2] and Gameboard[i] == Simbol[1- Turn[0]]:
                validade = 1
                if i == 0:
                    with self.line.canvas:
                        self.line.canvas.clear()				
                        Color(rgba=(text_color))
                        Line(points=(self.button1_image.pos[0], self.button1_image.pos[1]+self.button1_image.size[1]/2,self.button3_image.pos[0]+self.button3_image.size[0],self.button3_image.pos[1]+self.button3_image.size[1]/2),width=self.height*.01)
                elif i == 3:
                    with self.line.canvas:
                        self.line.canvas.clear()				
                        Color(rgba=(text_color))
                        Line(points=(self.button4_image.pos[0], self.button4_image.pos[1]+self.button4_image.size[1]/2,self.button6_image.pos[0]+self.button6_image.size[0],self.button6_image.pos[1]+self.button6_image.size[1]/2),width=self.height*.01)
                else:
                    with self.line.canvas:
                        self.line.canvas.clear()				
                        Color(rgba=(text_color))
                        Line(points=(self.button7_image.pos[0], self.button7_image.pos[1]+self.button7_image.size[1]/2,self.button9_image.pos[0]+self.button9_image.size[0],self.button9_image.pos[1]+self.button9_image.size[1]/2),width=self.height*.01)
        for i in range(3):
            if Gameboard[i] == Gameboard[i + 3] and Gameboard[i] == Gameboard[i + 6] and Gameboard[i] == Simbol[1 - Turn[0]]:
                validade = 1
                if i == 0:
                    with self.line.canvas:
                        self.line.canvas.clear()				
                        Color(rgba=(text_color))
                        Line(points=(self.button1_image.pos[0]+self.button1_image.size[0]/2, self.button1_image.pos[1]+self.button1_image.size[1],self.button7_image.pos[0]+self.button7_image.size[0]/2,self.button7_image.pos[1]),width=self.height*.01)
                elif i == 1:
                    with self.line.canvas:
                        self.line.canvas.clear()				
                        Color(rgba=(text_color))
                        Line(points=(self.button2_image.pos[0]+self.button2_image.size[0]/2, self.button2_image.pos[1]+self.button2_image.size[1],self.button8_image.pos[0]+self.button8_image.size[0]/2,self.button8_image.pos[1]),width=self.height*.01)
                else:
                    with self.line.canvas:
                        self.line.canvas.clear()				
                        Color(rgba=(text_color))
                        Line(points=(self.button3_image.pos[0]+self.button3_image.size[0]/2, self.button3_image.pos[1]+self.button3_image.size[1],self.button9_image.pos[0]+self.button9_image.size[0]/2,self.button9_image.pos[1]),width=self.height*.01)
        if Gameboard[0] == Gameboard[4] and Gameboard[0] == Gameboard[8] and Gameboard[0] == Simbol[1 - Turn[0]]:
            validade = 1
            with self.line.canvas:
                self.line.canvas.clear()				
                Color(rgba=(text_color))
                Line(points=(self.button1_image.pos[0], self.button1_image.pos[1]+self.button1_image.size[1],self.button9_image.pos[0]+self.button9_image.size[0],self.button9_image.pos[1]),width=self.height*.01)
        if Gameboard[2] == Gameboard[4] and Gameboard[2] == Gameboard[6] and Gameboard[2] == Simbol[1 - Turn[0]]:
            validade = 1
            with self.line.canvas:
                self.line.canvas.clear()				
                Color(rgba=(text_color))
                Line(points=(self.button7_image.pos[0], self.button7_image.pos[1],self.button3_image.pos[0]+self.button3_image.size[0],self.button3_image.pos[1]+self.button3_image.size[1]),width=self.height*.01)
        if validade == 1:
            self.result_text.text = f'Parabéns {players_names[1 - Turn[0]]}, você venceu'
            self.result_text.color = eval(color_dictionary[(f'{color[1 - Turn[0]]}')]) 
            Score[1 - Turn[0]][0] += 1
            Score[Turn[0]][1] += 1
            self.button1.disabled = True
            self.button2.disabled = True
            self.button3.disabled = True
            self.button4.disabled = True
            self.button5.disabled = True
            self.button6.disabled = True
            self.button7.disabled = True
            self.button8.disabled = True
            self.button9.disabled = True
            Begginer.append(1 - Begginer[0])
            del Begginer[0]
            self.line.opacity = 100
        elif ' ' not in Gameboard:
            self.result_text.text = 'Deu velha'
            self.result_text.color = eval(Background[1][0])
            Score[0][2] += 1
            Score[1][2] += 1

    def button_1(self):
        self.button1_image.color = eval('1,1,1,1')
        self.button1_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button1.disabled = True
        del Gameboard[0]
        Gameboard.insert(0,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')]) 
        if Plays[0] >= 5:
            self.game_result()
    def button_2(self):
        self.button2_image.color = eval('1,1,1,1')
        self.button2_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button2.disabled = True
        del Gameboard[1]
        Gameboard.insert(1, f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()
    def button_3(self):
        self.button3_image.color = eval('1,1,1,1')
        self.button3_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button3.disabled = True
        del Gameboard[2]
        Gameboard.insert(2,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()

    def button_4(self):
        self.button4_image.color = eval('1,1,1,1')
        self.button4_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button4.disabled = True
        del Gameboard[3]
        Gameboard.insert(3,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()

    def button_5(self):
        self.button5_image.color = eval('1,1,1,1')
        self.button5_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button5.disabled = True
        del Gameboard[4]
        Gameboard.insert(4,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()

    def button_6(self):
        self.button6_image.color = eval('1,1,1,1')
        self.button6_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button6.disabled = True
        del Gameboard[5]
        Gameboard.insert(5,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f"{players_names[Turn[0]]}, é a sua vez"
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()

    def button_7(self):
        self.button7_image.color = eval('1,1,1,1')
        self.button7_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button7.disabled = True
        del Gameboard[6]
        Gameboard.insert(6,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f"{players_names[Turn[0]]}, é a sua vez"
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5: 
            self.game_result()

    def button_8(self):
        self.button8_image.color = eval('1,1,1,1')
        self.button8_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button8.disabled = True
        del Gameboard[7]
        Gameboard.insert(7,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()

    def button_9(self):
        self.button9_image.color = eval('1,1,1,1')
        self.button9_image.source = f'{color[Turn[0]]}{Simbol[Turn[0]]}.png'
        Turn.append(1 - Turn[0])
        del Turn[0]
        self.button9.disabled = True
        del Gameboard[8]
        Gameboard.insert(8,f"{Simbol[1 - Turn[0]]}")
        Plays[0] += 1
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        if Plays[0] >= 5:
            self.game_result()

    def restart_game(self):
        screen_color = eval(Background[0][0])
        self.button1_image.source = ''
        self.button1.disabled = False
        self.button1_image.color = screen_color
        self.button2_image.source = ''
        self.button2.disabled = False
        self.button2_image.color = screen_color
        self.button3_image.source = ''
        self.button3.disabled = False
        self.button3_image.color = screen_color
        self.button4_image.source = ''
        self.button4.disabled = False
        self.button4_image.color = screen_color
        self.button5_image.source = ''
        self.button5.disabled = False
        self.button5_image.color = screen_color
        self.button6_image.source = ''
        self.button6.disabled = False
        self.button6_image.color = screen_color
        self.button7_image.source = ''
        self.button7.disabled = False
        self.button7_image.color = screen_color
        self.button8_image.source = ''
        self.button8.disabled = False
        self.button8_image.color = screen_color
        self.button9_image.source = ''
        self.button9.disabled = False
        self.button9_image.color = screen_color
        self.line.opacity = 0
        Begginer.append(1 - Begginer[0])
        del Begginer[0]
        Turn.clear()
        Turn.append(Begginer[0])
        Plays[0] = 0
        Gameboard.clear()
        for i in range(9):
            Gameboard.append(' ')
        self.result_text.text = f'{players_names[Turn[0]]}, é a sua vez'
        self.result_text.color = eval(color_dictionary[(f'{color[Turn[0]]}')])
        self.score_1.text = f"{Score[0][0]}  {Score[0][1]}  {Score[0][2]}"
        self.score_2.text = f"{Score[1][0]}  {Score[1][1]}  {Score[1][2]}"
    def home(self):
        self.restart_game()
        self.parent.current = 'menu'
        Turn.clear()
        Begginer.clear()
        players_names.clear()
        Simbol.clear()
        Plays.clear()
        Plays.append(0)
        self.parent.get_screen('names').ids.name_1.text = ''
        self.parent.get_screen('names').ids.name_2.text = ''
        self.parent.get_screen('choose').ids.name_1.text = ''
        self.parent.get_screen('choose').ids.name_2.text = ''
        self.parent.get_screen('choose').ids.image_X.source = f'greyX.png'
        self.parent.get_screen('choose').ids.image_O.source = f'greyO.png'
        self.parent.get_screen('choose').ids.start_button.opacity = 0
        self.parent.get_screen('choose').ids.start_button.disabled = True
        self.parent.get_screen('names').ids.message.text = ''
        Score[0].clear()
        Score[1].clear()
        for i in range(3):
            Score[0].append(0)
            Score[1].append(0)

class Test(Screen):
	pass

class tela(App):
	def build(self):
		return Screens()
		
tela().run()
