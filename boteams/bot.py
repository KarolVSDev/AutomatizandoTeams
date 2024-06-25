from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):

        # lembre de atualizar os códios para o programa que quer abrir no seu computador
        self.execute(r'C:\Users\blackoperation\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams')
       
        if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar")
        self.click()
        
        self.paste("lucas antonioli")
        
        if not self.find( "lucas", matching=0.97, waiting_time=10000):
            self.not_found("lucas")
        self.click()
        
        if not self.find( "busca", matching=0.97, waiting_time=10000):
            self.not_found("busca")
        self.click()
        
        self.paste("Olá, esta é uma tarefa automatizada com botcity")
        self.enter()
        
        

       



    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()