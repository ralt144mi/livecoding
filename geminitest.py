from gemini import Scene, Entity

scene = Scene(size=(20,10))
entity = Entity(pos=(5,5), size=(2,1), parent=scene)

scene.render()

from gemini import Scene, Entity, sleep

scene = Scene(size=(20,10))
entity = Entity(pos=(5,5), size=(2,1), parent=scene)

while True:
	entity.move((1,0))
	scene.render()
	sleep(.1)


from gemini import Scene, Sprite, sleep

from random import choice

choice(myfishes)

myfishes = ["""
<^{{{><
""","""
><]]]^>
"""]

fish = """
<^{{{><
"""

mermaid = """
\o/
 "=(
"""


scene = Scene((30,10), is_main_scene=True)

car = Sprite((5,5), fish)
car2 = Sprite((5,5), mermaid)

    car = Sprite((5,5), choice(myfishes))
    car2 = Sprite((5,5), mermaid)

@swim
def spritechanger(p=0.5, i=0):
    car = Sprite((5,5), choice(myfishes))
    car2 = Sprite((5,5), mermaid)
    again(spritechanger,p=4,i=i+1)


@swim
def renderer(p=0.5,i=0):
    scene.render()
    car.move(i%30,i%5)
    car2.move(-i%30,i%5)
    again(renderer,p=P("1!4 2 0.25!4",i),i=i+1)

exit()



