import sys,os
from tkinter import messagebox
import tkinter as tk
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
pick = 1
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')

def quitwarn():
    root = tk.Tk()   #tkinter must have a root window if cant create one, one will be created automatically
    root.withdraw()    
    response=messagebox.askyesno("Pycarft", "You sure you wanna Quit?")
    if response==1:
        exit()
	
	

window.fps_counter.enabled = False
window.exit_button.visible = True
def fallwarn():
    root = tk.Tk()   
    root.withdraw()    
    response=messagebox.showerror("Pycraft", "You fell into the void Babes :(\n Better luck next time!")
    if response==messagebox.OK:
        exit()
	


	
def update():

	global pick
	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()
	
	txt = Text(text="Press 'i' for Instructions", scale =2, x=-.4,y=-.4)
	
	if held_keys['1']: 
		pick = 1

	if held_keys['2']: 
		pick = 2

	if held_keys['3']: 
		pick = 3

	if held_keys['4']: 
		pick = 4

	if held_keys['i']: 
		os.system('Instructions.py')

	if held_keys['v']:
		camera.position=Vec3(0,random.uniform(0,1),random.uniform(-1,1))

	if player.position < Vec3(-1,-1,-1) or player.position > area.position:
		fallwarn()	
	
	if held_keys['f']:
		window.fullscreen = True
			
	if held_keys['q']:
		mouse.locked = False
		quitwarn()
	

	
	 
class Boxy(Button):
	
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)
	
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				
				if pick == 1: 
					box = Boxy(position = self.position + mouse.normal, texture = grass_texture)
				if pick == 2: 
					box = Boxy(position = self.position + mouse.normal, texture = stone_texture)
				if pick == 3: 
					box = Boxy(position = self.position + mouse.normal, texture = brick_texture)
				if pick == 4: 
					box = Boxy(position = self.position + mouse.normal, texture = dirt_texture)

			if key == 'right mouse down':
				
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 100,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)


for z in range(10):
	for x in range(10):
		area = Boxy(position = (x,0,z))


player = FirstPersonController()
sky = Sky()
hand = Hand()



app.run()
