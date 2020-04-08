Descrição 
=================================

 

Este pacote é desenvolvido para operar no ROS (Robot Operating System) e tem por finalidade apresentar a trajetória percorrida por uma ARTag. As ARtags são comumente utilizadas em trabalhos relacionados a robótica com o objetivo de identificar objetos no ambiente, ou identificar o robô. Com este pacote, é possível visualizar por meio da ferramenta Rviz a trajetória da ARtag desejada. Cada ARtag possui um id. É possível selecionar quais ids deseja rastrear, definir a cor do rastro, tamanho da linha, tamanho do rastro, frequência de atualização, tópico de entrada contendo as informações das ARtags e tópico de saída contendo as linhas. 

 

Configuração do sistema utilizado 
--------------------------------

Ubuntu 18.04.4 (http://releases.ubuntu.com/18.04.4/) 

ROS Melodic (http://wiki.ros.org/melodic/Installation/Ubuntu) 

 

Requisitos
-------------------------------- 

1. **ar_track_alvar**: 
   - URL: (http://wiki.ros.org/ar_track_alvar) 
   - Instalação: ```sudo apt-get install ros-melodic-ar-track-alvar*``` 

 
Argumentos: 
----------------------------------
1. **run_rviz**
   - Descrição: Pode ser “true” ou “false”. Se “true”, executa o rviz com uma configuração salva. 

2. **run_ar_tracker_alvar**
   - Descrição: Pode ser “true” ou “false”. Se “true”, executa o launch “ar_tracker_alvar.launch” dentro do pacote “track_position_ARtag”. Para verificar as configurações possíveis para o launch, acesse http://docs.ros.org/fuerte/api/ar_track_alvar/html/msg/AlvarMarkers.html.
 
Parâmetros:
----------------------------------
1. **track_ar_ids_param**
   - Valor: "id1,id2, ... ,idn"
   - Tipo: String
   - Valor padrão: "4, 13"
   - Descrição: Deve ser informado o id das tags para serem rastreadas. Devem ser informados separados por vírgula, “0,1,2,3” 

2. **track_ar_colors_param**
   - Valor: "[r,g,b,a];[r,g,b,a];[r,g,b,a]; ... ;[r,g,b,a]"
   - Tipo: String
   - Valor padrão: "[0.3,0.5,0.3,1];[1,0,0,1]"
   - Descrição:Deve ser informado a cor do rastro, em RGBA. As cores devem estar entre “[]“ e separadas por ",”. As cores devem estar separadas por “;”. O valor suportado é de 0 até 1. Exemplo: "[1,0,0,1];[0.3,0.2,0,1]" 

3. **ros_rate_param**
   - Valor: "rate"
   - Tipo: double
   - Valor padrão: 10.0
   - Descrição: Remerece a taxa de operação do pacote. O valor deve ser inteiro, Exemplo: 10. 

4. **queue_size_param**
   - Valor: "10"
   - Tipo: double
   - Valor padrão: 100.0
   - Descrição: O tamanho da fila de pontos a ser armazenada. Quanto maior, maior será o rastro salvo. 

5. **considered_displacement**
   - Valor: "0.02"
   - Tipo: double
   - Valor padrão: 0.02
   - Descrição:Só será calculado no deslocamento, caso o ponto se mova mais do que o “considered_displacement”. Caso seja zero, a fila pode se mover mesmo com objeto parado, sumindo o seu rastro. 

6. **line_scale**
   - Valor: "0.01"
   - Tipo: double
   - Valor padrão: 0.01
   - Descrição: Espessura da linha apresentada em metros. 

7. **input_topic**
   - Valor: "nome_do_topico"
   - Tipo: String
   - Valor padrão: "/ar_pose_marker"
   - Descrição: Nome do tópico de entrada. Deve ser do tipo “ar_track_alvar/AlvarMarkers” (http://docs.ros.org/fuerte/api/ar_track_alvar/html/msg/AlvarMarkers.html).

8. **output_topic**
   - Valor: "nome_do_topico"
   - Tipo: String
   - Valor padrão: "track_position_line"
   - Descrição: Nome do tópico de saída, do tipo visualization_msgs/MarkerArray.msg (http://docs.ros.org/melodic/api/visualization_msgs/html/msg/MarkerArray.html) 

9. **output_frame**
   - Valor: "nome_do_frame"
   - Tipo: String
   - Valor padrão: "usb_cam"
   - Descrição: Nome do frame ao qual o tópico de saída será vinculado. 


Instalando:
--------------------------------
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/marco-teixeira/track_position_ARtag
$ cd ~/catkin_ws
$ catkin_make
```


Executando: 
-------------------------------

```
roslaunch track_position_ARtag track_position_ARtag.launch
```

Vídeo:
------------------------------- 




