
from ursina import *
from ursina import texture
from ursina.application import pause
from ursina.prefabs.first_person_controller \
  import FirstPersonController
from random import uniform


app = Ursina()


app.run()
'''mouse.visible=True
	if held_keys['i']:
		heading = "How To Play".center(25)
		insttext = "1. For the player to move, use w->forward s->backward a->left d->right\n2.To place a block->left click\n3.To destroy a box->Right click\n4.To customise box:\n\t 1->\n\t 2->\n\t 3->\n\t4->\n5.To Quit press q"
		
		headingbox= Text(text=heading,background=color.white,color=color.gray, scale =3, x=-.4,y=.4)
		instbox=Text(text=insttext,color=color.black,size=.5,x=-.45,y=.1)
		B=Button(text='exit', scale=.25)

	#if B.on_click:
	#	B.on_click = quit(instructions)

im = Image.open("assets/pink.png")
im.show()
class instructions(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'quad',
			texture = 'assets/pink.png',
			scale = 2,
			)	
	def input(self,key):
			if key == 'i': print_on_screen('hey')
			if key == 'k': destroy(self)

ground = Entity(model= 'plane',
                texture= 'grass',
                collider= 'mesh',
                scale= (10,1, 10))
if held_keys['f']:
		#Fullscreen()
		window.fullscreen=True
	#if player.position	
def Fullscreen():
	if window.fullscreen==False:
		window.fullscreen=True
	if window.fullscreen==True:
		window.fullscreen=False
		#window.windowed_size = window.fullscreen_size / 5








'''