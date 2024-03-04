# Hurtig guide til at få sat robotten op, samt lidt ekstra info
Udgangspunktet er at alt er installeret jf. README
## Opstart af robot og noder
### 1 Tilslut PC til UR'en
Tilslut PC med static ip adresse til UR. UR'en forventer at PC'en har ip adresse 192.168.1.25

Åbn terminal og skriv:

```sh
roslaunch ur_robot_driver ur5_bringup.launch robot_ip:=192.168.1.15 \
  kinematics_config:="/home/robotlab/Desktop/my_robot_calibration.yaml"
```

På UR'en startes 'rockpicker' programmet, og nu skulle terminalen gerne melde tilbage

### 2 Start MoveIt planner og ur5 config i Rviz

Åbn terminal

Start MoveIt planner

```sh
roslaunch ur5_moveit_config moveit_planning_execution.launch
```

Åbn terminal

Start Rviz

```sh
roslaunch ur5_moveit_config moveit_rviz.launch
```

### 3 Start af RealSense kamera, og konfigurering heraf

Åbn terminal

Start IntelRealsense kameraet med følgende parametre

```sh
roslaunch realsense2_camera rs_camera.launch color_width:="1920" color_height:="1080" color_fps:="30"
```

Når noden er startet, start kamera feed i Rviz, kontrollér at det blå/grønne i midten af billedet er væk, det kan være at robotten skal bevæges op og ned, med sandkassen i billedet.

Når det grønne er væk, start rqt dynamic reconfigure

Åbn terminal

```sh
rqt
```
Plugins -> Dynamic Reconfigure -> camera -> rgb_camera

Fjern auto whitebalance, og kør slideren helt i bund.
Sæt brightness til 22

### 4 Start gripper server

Åbn terminal 

Start gripper command server

```sh
rosrun wsg_gripper gripper_command_server2.py
```

### 5 Start kamera server

Åbn terminal

Start camera server

```sh
rosrun realsense_ting_controller camera_server.py
```

### 6 Start billedbandling server

Åbn terminal

Start billedbehandling server

```sh
rosrun realsense_ting_controller image_processing_server.py
```

### 7 Indstilling af threshold

Åbn terminal

For at ændre threshold værdien gå til linje 34 i image_processing_server.py

Test threshold værdier inden robotten sættes igang, dette gøres ved at kalde process servicen:

```sh
rosservice call /process_image "Process"
```
Det nemmeste er at åbne billedet Image_thresh.jpg i visual studio når billedet ligner at stenene er nogenlunde defineret uden alt for meget støj omkring har du fundet en god værdi.
![Thresholded image](Image_thresh.jpg "Thresholded image")

### 8 Start autonom kørsel af robotten

Åbn terminal

Når alt er startet op korrekt og det opfører sig ordenligt, så kan hoved scriptet startes. Der skal være sten tilstede i billedet ellers crasher billedbehandling serveren (Ik så smart, det ved vi godt).

```sh
rosrun ur5_module get_poses.py
```

Man kan heldigvis lade alt det andet køre i baggrunden, og så starte det her script når det skal køre, og så stoppe det igen, når man er færdig.

## Gode ting at vide

Robotten kan ikke føres med hånden, så længe at rockpicker programmet kører, ønsker man at styre den med hånden stoppes programmet, og når ROS skal overtage igen startes det igen.

Hvis den går i nødstop, så afslut get_poses scriptet, og start det igen, og tryk enter, sådan at den sender kommando til at bevæge robotten tilbage til start. Det kan ske ellers at når man starter robotten op igen, at den forsætter med at køre den vej, som fik den til at gå i nødstop, og så gør den det bare igen.

Hvis efter et nødstop at griberen er lukket, så skal den åbnes igen inden den bliver sat igang igen, det gøres ved et service kald:

```sh
rosservice call /gripper_commands "home"
```

Man kan holde øje med, om thresholden holder, ved at kigge på det thresholded billede om der kommer store hvide plamager. Den kan ændres i image_processing_server.py På linje 34 i scriptet er der en variable der hedder main_thresh, juster den med 5 værdier adgangen, for at se om det gør en forskel.
