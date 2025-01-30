from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import buildozer

class Szamologep(App):
    def build(self):
        self.operator=["/","+","-","*"]
        self.utolso_operator= None
        self.solution=TextInput(readonly=False,font_size=55,halign="right",multiline=False)
        self.utolso_gomb=None
        main_layout=BoxLayout(orientation="vertical")

        main_layout.add_widget(self.solution)
        buttons=[
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],

        ]
        for row in buttons:
            h_layout=BoxLayout()
            for label in row:
                button=Button(text=label,pos_hint={"center_x":0.5,"center_y":0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        egyenloseg_jel=Button(text="=",pos_hint={"center_x":0.5,"center_y":0.5})
        egyenloseg_jel.bind(on_press=self.on_solution)
        main_layout.add_widget(egyenloseg_jel)
        return main_layout

    def on_button_press(self,instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
             self.solution.text = ""
        else:
            if current and (self.utolso_operator and button_text in self.operator):
                return
            elif current=="" and (button_text in self.operator):
                return
            else:
                uj_szoveg = current + button_text
                self.solution.text = uj_szoveg
        self.utolso_gomb = button_text
        self.utolso_operator = button_text in self.operator

    def on_solution(self,instance):
        text=self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

Szamologep().run()







Szamologep().run()