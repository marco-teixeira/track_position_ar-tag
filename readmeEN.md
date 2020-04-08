#Descrição 

 

Este pacote é desenvolvido para operar no ROS (Robot Operating System) e tem por finalidade apresentar a trajetória percorrida por uma ARTag. As ARtags são comumente utilizadas em trabalhos relacionados a robótica com o objetivo de identificar objetos no ambiente, ou identificar o robô. Com este pacote, é possível visualizar por meio da ferramenta Rviz a trajetória da ARtag desejada. Cada ARtag possui um id. É possível selecionar quais ids deseja rastrear, definir a cor do rastro, tamanho da linha, tamanho do rastro, frequência de atualização, tópico de entrada contendo as informações das ARtags e tópico de saída contendo as linhas. 

 

#Configuração do sistema utilizado 

Ubuntu 18.04.4 (http://releases.ubuntu.com/18.04.4/) 

ROS Melodic (http://wiki.ros.org/melodic/Installation/Ubuntu) 

 

#Requisitos 

* ar_track_alvar: 
URL: (http://wiki.ros.org/ar_track_alvar) 
Instalação: sudo apt-get install ros-melodic-ar-track-alvar* 

 
#Argumentos: 
 

 

#Parâmetros:

 

 

#Vídeo: 

Apresenta um modelo baseado no abnTeX2 desenvolvido para auxiliar os discentes na formatação da dissertação de mestrado. Embora tenho sido desenvolvido especificamente para ser utilizado pelos alunos do Programa de Pós-Graduação em Computação Aplicada - PPGCA, este modelo pode ser configurado e facilmente adaptado para uso em outros programas de pós-graduação e tipos de trabalhos acadêmicos (como TCCs e teses). Espera-se que este modelo implemente todas as exigências do manual de trabalhos acadêmicos da UDESC sem a necessidade de se preocupar com o estilo ou formatação do documento.

# Arquivos do Template

* Principal.tex = arquivo principal que deve ser compilado;
* Estilo/udesc.sty = pacote de estilos da customização;
* Partes/cap1.tex = exemplo de primeiro capítulo;
* Partes/cap2.tex = exemplo de segundo capítulo;
* Partes/pretextual.tex = elementos pré-textuais;
* Partes/aneA.tex = exemplo de anexo;
* Partes/apeA.tex = exemplo de apêndice;
* references.bib = arquivo de referências para exemplificar o uso da abntex2cite.

# Instruções para o uso do modelo:

1. Tenha instalado um compilador com o pdfLaTeX;
2. Edite as informações referentes a capa e folha de rosto no arquivo Principal.tex;
3. Compile o arquivo Principal.tex.

Qualquer dúvida ou sugestão: luis.bilecki at gmail dot com

Fórum Google Groups:

https://groups.google.com/forum/#!forum/templateppgcaudesc



