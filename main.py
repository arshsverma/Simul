from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
import cmath


class MainScreen(Screen):
    pass


class Home(Screen):
    pass


class Health(Screen):
    pass


class Education(Screen):
    pass


class Feynman_technique(Screen):
    s = StringProperty("")
    data = open("How_to_Use_the_Feynman_Technique_to_Learn_Faster.txt", "r", encoding='utf-8')
    s = "".join(data)


class Environment(Screen):
    pass


class Utilities(Screen):
    pass


class AllManager(ScreenManager):
    pass


class Calculator(Screen):
    pass


class Quadratic_solver(Screen):
    def Solve(self):
        a = float(self.ids.A.text)
        b = float(self.ids.B.text)
        c = float(self.ids.C.text)
        ans = self.ids.answer
        discriminant = (b ** 2) - (4 * a * c)

        ans1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        ans2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

        ans.text = str(ans1) + ", " + str(ans2)


class Diet(Screen):
    def dietList(self):
        f_1 = self.ids['input1']
        f_2 = self.ids['input2']
        f_3 = self.ids['input3']
        app = MDApp.get_running_app()
        app.root.ids.dietlabel.m += str("\nDate: {}, Time: {}, Food: {}".format(f_1.text, f_2.text, f_3.text))


class Diet_label(Screen):
    m = StringProperty("")


class Exercise(Screen):
    def exerciseList(self):
        f_1 = self.ids['input11']
        f_2 = self.ids['input21']
        f_3 = self.ids['input31']
        app = MDApp.get_running_app()
        app.root.ids.exerciselabel.s += str("\nDate: {}, Time: {}, Exercise: {}".format(f_1.text, f_2.text, f_3.text))


class Exercise_label(Screen):
    s = StringProperty("")


class First_aid(Screen):
    s = StringProperty("")
    data = open("first_aid_tips.txt", "r", encoding='utf-8')
    s = "".join(data)


class Tree_cost(Screen):
    def treeAnswer(self):
        num = self.ids.tree_number
        planting = self.ids.cost_plant
        maintaining = self.ids.cost_maintain
        total = self.ids.cost_final
        s = float(num.text)
        planting.text = str(s * 5000) + " - " + str(s * 15000)
        maintaining.text = str(s * 70000) + " - " + str(s * 115000)
        total.text = str(s * 75000) + " - " + str(s * 130000)


class Gardening_hacks(Screen):
    pass


class Gardening_beginners(Screen):
    s = StringProperty("")
    data = open("BEGINNERS.txt", "r", encoding='utf-8')
    s = "".join(data)


class Gardening_intermediate(Screen):
    s = StringProperty("")
    data = open("intermediate.txt", "r", encoding='utf-8')
    s = "".join(data)


class Gardening_experienced(Screen):
    s = StringProperty("")
    data = open("experienced.txt", "r", encoding='utf-8')
    s = "".join(data)


class Easy_plants_to_grow(Screen):
    s = StringProperty("")
    data = open("easy_plants_to_grow.txt", "r", encoding='utf-8')
    s = "".join(data)


class Profitable_trees(Screen):
    s = StringProperty("")
    data = open("profitable_tress.txt", "r", encoding='utf-8')
    s = "".join(data)


class MainApp(App):
    def build(self):
        return AllManager()


if __name__ == '__main__':
    MainApp().run()
