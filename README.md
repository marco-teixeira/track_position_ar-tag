[Leia esta página em português](https://github.com/marco-teixeira/track_position_ARtag/blob/master/README-pt.md)


Description
=================================

This package is developed to operate on the ROS (Robot Operating System) and aims to present the trajectory covered by an ARTag. ARtags are commonly used in work related to robotics to identify objects in the environment or to identify the robot. With this package, it is possible to view the trajectory of the desired ARtag using the Rviz tool. Each ARtag has an id. You can select which ids you want to track, define the trail color, line size, queue size, update frequency, input topic containing the ARtags information and output topic containing the lines.

Configuration of the system used
--------------------------------

* Ubuntu 18.04.4 (http://releases.ubuntu.com/18.04.4/)
* ROS Melodic (http://wiki.ros.org/melodic/Installation/Ubuntu)

Requirements
--------------------------------
1. ** ar_track_alvar **:
   - URL: (http://wiki.ros.org/ar_track_alvar)
   - Installation: ```sudo apt-get install ros-melodic-ar-track-alvar * ```

Arguments:
----------------------------------
1. ** run_rviz **
   - Description: It can be “true” or “false”. If "true", run rviz with a saved configuration.

2. ** run_ar_tracker_alvar **
   - Description: It can be “true” or “false”. If “true”, execute the launch “ar_tracker_alvar.launch” inside the package “track_position_ARtag”. To check the possible configurations for the launch, go to http://docs.ros.org/fuerte/api/ar_track_alvar/html/msg/AlvarMarkers.html.

Parameters:
----------------------------------
1. ** track_ar_ids_param **
   - Value: "id1, id2, ..., idn"
   - Type: String
   - Default value: "4, 13"
   - Description: The id of the tags must be informed to be tracked. They must be informed separated by ",", “0,1,2,3”

2. ** track_ar_colors_param **
   - Value: "[r, g, b, a]; [r, g, b, a]; [r, g, b, a]; ...; [r, g, b, a]"
   - Type: String
   - Default value: "[0.3,0.5,0.3.1]; [1,0,0,1]"
   - Description: The trail color must be informed, in RGBA. Colors must be between "[]" and separated by ",". Colors must be separated by ";". The supported value is 0 to 1. Example: "[1,0,0,1]; [0.3 , 0.2,0.1] "

3. ** ros_rate_param **
   - Value: "rate"
   - Type: double
   - Default value: 10.0
   - Description: Refers to the package operation fee. The value must be an float, Example: 10.

4. ** queue_size_param **
   - Value: "10"
   - Type: double
   - Default value: 100.0
   - Description: The size of the point queue to be stored. The bigger, the bigger the trajectory will be.

5. ** considered_displacement **
   - Value: "0.02"
   - Type: double
   - Default value: 0.02
   - Description: It will only be calculated the displacement, if the point moves more than the "considered displacement". If it is zero, the queue can move even with a stationary object, disappearing its trail.

6. ** line_scale **
   - Value: "0.01"
   - Type: double
   - Default value: 0.01
   - Description: Line thickness shown in meters.

7. ** input_topic **
   - Value: "topic_name"
   - Type: String
   - Default value: "/ ar_pose_marker"
   - Description: Name of the input topic. It must be of the type “ar_track_alvar/AlvarMarkers” (http://docs.ros.org/fuerte/api/ar_track_alvar/html/msg/AlvarMarkers.html).

8. ** output_topic **
   - Value: "topic_name"
   - Type: String
   - Default value: "track_position_line"
   - Description: Name of the output topic, type visualization_msgs/MarkerArray.msg (http://docs.ros.org/melodic/api/visualization_msgs/html/msg/MarkerArray.html)

9. ** output_frame **
   - Value: "frame_name"
   - Type: String
   - Default value: "usb_cam"
   - Description: Name of the frame to which the output topic will be linked.

Install:
--------------------------------

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/marco-teixeira/track_position_ARtag
$ cd ~/catkin_ws
$ catkin_make
```

Run:
-------------------------------

```
roslaunch track_position_ARtag track_position_ARtag.launch
```



