from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

SABORES = {
    'Comun' : ['Cochina','Especial de rucula','Roquefort con panceta','Provolone con panceta','De atun','Champignones'],
    'Raro' : ['Especial de la casa','Muzza','Jamon y morron','Jamon','Morron','Napolitana','Napolitana c/jamon','Napolitana c/huevo','Napolitana c/Jamon y huevo','Calabresa','Palmitos','Especial de palmitos','Cuatro Quesos','Especial de panceta','Criolla','Panceta c/Cheddar','Especial de salchichas','Especial de pollo','Muza al verdeo','Rucula','Berenjenas','Especial de crudo','Caprese','Humita','Choclo','Primavera','Primavera c/Jamon','Correntina','Verduras C/Salsa blanca','Provolone','Provolone c/jamon','Roquefort','Roquefort c/jamon','Lluvia de papas','Salchipapa','Margarita','A la bolognesa','De vegetales','Fugazza con queso y panceta','Fugazza con queso','Fugazza cheddar','Cheddar'],
    'Legendario' : ['Ananá','Hawaiana','Hawaiana c/crudo','Romana','Muzarella c/Anchoas','Anchoas','Mixta']

}



class Pizza:
    def __init__(self, sabor='', rareza='') -> None:
        self.sabor = sabor
        self.rareza = rareza

    def generar_pizza(self):
        x = random.randint(0, 100)
        self.rareza = 'Comun' if x <= 60 else 'Raro' if x < 100 else 'Legendario'
        if self.rareza == 'Comun':
            y = random.randint(0, 5)
            self.sabor = SABORES[self.rareza][y]
        elif self.rareza == 'Raro':
            y = random.randint(0, 41)
            self.sabor = SABORES[self.rareza][y]
        else:
            y = random.randint(0, 6)
            self.sabor = SABORES[self.rareza][y]

    def __str__(self) -> str:
        return self.sabor


class PizzaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Presiona el botón para generar 4 pizzas")
        button = Button(text="Generar Pizzas", on_press=self.generar_pizzas)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def generar_pizzas(self, instance):
        pizzas = []
        for _ in range(4):
            pizza = Pizza()
            pizza.generar_pizza()
            while any(p.sabor == pizza.sabor for p in pizzas):
                pizza.generar_pizza()


            pizzas.append(pizza)

        self.label.text = "Sabores de las pizzas:\n" + "\n".join(str(p) for p in pizzas)


if __name__ == '__main__':
    PizzaApp().run()