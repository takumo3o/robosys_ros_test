# robosys_ros_test

robosys2018: homework2

## 概要
脳波で動かすロボットを

## 動画
* URL - https://www.youtube.com/watch?v=E9WvXxnSEjY

## 使うもの
* Raspberry Pi Mouse
  * Raspberry Pi 3 Model B
* Mindwave Mobile
* ROSパッケージ
  * [ryuichiueda/pimouse_ros](https://github.com/ryuichiueda/pimouse_ros)

## 使い方
1. ROSパッケージとこのリポジトリをダウンロード
```
cd ~/catkin_ws/src
$ git clone https://github.com/ryuichiueda/pimouse_ros.git
$ git clone https://github.com/takumo3o/robosys_ros_test.git
$ cd ~/catkin_ws && catkin_make && source ~/catkin_ws/devel/setup.bash
```

2. Mindwave Mobileを装着し、PCで以下を実行
```
$ roscore
```
  * 別の端末で
```
$ rosrun mindwave_ros test.py
```

3. Raspberry Pi で以下を実行
* .bashrcに以下を追加
```
$ export ROS_MASTER_URI=http://"Raspberry Piのipaddress":11311
```

```
$ roslaunch pimouse_ros pimouse.launch
```
  * 別の端末で
```
$ rosrun mindwave_rasp velocity.py
```
    * velocity.py or turning.py
    


## LICENSE
このリポジトリは GPLv3 ライセンスに基づきます。[LICENSE](https://github.com/takumo3o/robosys_device_driver/blob/master/LICENSE)をご覧ください。
