#importando biblioteca que faz a automacao de tarefas, é bem completo 
#caso de erro, baixe a ultima versao do python, apaga o ambiente virtual e cria de novo, se persistir, apague a biblioteca e instale novamente, 
#e se persisir, fecha e abre o visual de novo
#NOTE: pip install pyautogui
#bibliotexa para gerar executavel
#NOTE: pip install cx_Freeze

#importar bibliotecas
import pyautogui as auto

#comando para atrasar cada linha de comando, pois esta muito rapido e esta digitando as palavras juntas na hora de pesquisar
auto.PAUSE = 0.5


#apertar qualquer tecla, voce informa qual tecla é para ele apertar
auto.press('win') #abre o menu iniciar
auto.write('chrome') #digita a palavra chrome
auto.press('enter') #aperta enter

#maximizar a tela, a janela do chrome
auto.hotkey('alt','space')    #hotkey = para usar tecla de atalho     
auto.press('x') #aperta enter

#acessa site github
auto.write('github.com') #digita github.com
auto.press('enter') #aperta enter

#entrar na pagina de login no github
for i in range(12):
    auto.press('tab')

auto.press('enter') #aperta enter

#gerar executavel
#apos instalar a biblioteca, 
# dgite no promp de comando:  cxfreeze (nome do arquivo "p") --target-dir ('nome da pasta)
#cria uma pasta que gera os arquivos responsaveis para execucao do programa, um atalho
#dentro da pasta automacao que foi criada, abra ela, e va na 1 opcao apos entrar nela, escita 'app.exe' (executavel)
#clique com o botao direito em cima dela
#clique em Revelar no explorador de arquivo
#no explorador de arquivos, clique com o botao direito em cima de 'app'
#Clique em Mostrar mais
#clirque em Enviar para 
#selecione para "Area de trabalho"
#Agora voce tem um executavel na area de trabalho