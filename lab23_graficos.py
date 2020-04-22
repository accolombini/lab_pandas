import numpy as np 
import matplotlib.pyplot as plt 


x = np.linspace(0, 2, 100)
y = 2 * x
y2 = x ** 2

plt.plot(x, y, '. r')
plt.title('Matplotlib')
plt.xlabel('Eixo_x')
plt.ylabel('Eixo_y')
plt.show()

plt.plot(x, y2, 'o g')
plt.title('Matplotlib')
plt.xlabel('Eixo_x')
plt.ylabel('Eixo_y')
plt.show()

# Plotando os dois graficos juntos
plt.plot(x, y, '. r')
plt.plot(x, y2, 'o g')
plt.title('Matplotlib')
plt.xlabel('Eixo_x')
plt.ylabel('Eixo_y')
plt.legend(['Reta', 'Parabola'])
plt.show()

# Vamos agora visualizar varios tipos de graficos um ao lado do outro
k = np.linspace(-1, 1, 100)
w1 = 2 * k
w2 = k ** 2
w3 = k ** 3
w4 = np.sin(k)

# Definindo o gride de plotagem
fig, janela = plt.subplots(2,2)
janela[0, 0].plot(k, w1, '.r')
janela[0, 1].plot(k, w2, '.g')
janela[1, 0].plot(k, w3, '.y')
janela[1, 1].plot(k, w4, '.b')
fig.legend(['Reta', 'Parabola', 'Cubica', 'Senoidal'])
plt.show()
