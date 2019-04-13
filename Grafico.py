import matplotlib.pyplot as plt #https://panda.ime.usp.br/algoritmos/static/algoritmos/10-matplotlib.html

class Grafico:

    def plotLinha(self, vetor, titulo):
        plt.plot( vetor )    #plota um grafico de linha
        plt.title(titulo)
        plt.show()

    def plotPonto(self, vetor, titulo):
        plt.plot( vetor, "go", color = "blue" )
        plt.title(titulo)
        plt.show()
