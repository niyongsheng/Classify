![(logo)](https://github.com/niyongsheng/Classify/blob/master/logo.png?raw=true)
Classify
===
<p align="left">
  <a href="https://github.com/niyongsheng/Classify/issues">
     <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Issues">
  </a>
</p>

> 基于ResNet算法的垃圾分类 <br>
> Garbage classification based on ResNet

## Screenshot：
![(logo)](https://github.com/niyongsheng/Classify/blob/master/LF100E8E-A3DE-4565-963D-2C315E370F9F.png)

## Summary:
- [x]Classify_localtrain   本地训练代码
- [x]Classify_app_sever    服务部署代码
- [x]garbage_app_sever     树莓派服务代码
- [x]Classify_app_website  前端应用代码

---
效果演示地址：https://www.bilibili.com/video/BV1Wh411h7K7
<br>
训练数据集地址：https://developer.huaweicloud.com/hero/forum.php?mod=viewthread&tid=47550

## Notes:
```shell
// 1、PyCharm下配置conda解释器python3.6导入框架依赖
// https://www.anaconda.com
pip install conda

// 2.安装tensorflow:机器学习框架
pip3 install tensorflow==1.13.1

// 3.keras:Python 编写的高级神经网络 API
pip3 install keras==2.3.1

// 4.图像处理框架(多用于视频流处理的时候)3.4.10.37 4.3.0.38 
// pip3 install opencv-contrib-python
pip3 install opencv-python

// 5.Python 图像处理库
pip3 install Pillow

// 6.安装框架flask:python下的Web应用服务程序框架
pip3 install Flask
pip3 install flask-cors

// 7.网络请求框架
pip3 install requests


// su下解决cv2报错缺失so文件
// libcblas.so.3: cannot open shared object file: No such file or directory
pip3 install opencv-python
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install python3-pyqt5
sudo apt-get install libqt4-test

pip3 uninstall numpy
pip3 install numpy


// 上传app服务代码到树莓派
cd /tmp/pycharm_project_809
// 运行
python3 ./app_sever.py


// 解决服务端PyCharm运行外网ip无法访问，conda手动运行
// 查看环境列表
conda env list
// 切换
source activate Classify_serverdeploy-master
// 运行
python flask_sever.py
// 退出环境
source activate Classify_serverdeploy-master
// 退出base环境
conda deactivate
```

## Remind
- [x] python@3.6.5
- [x] tensorflow@1.13.1
- [x] vue-electron@1.0.6

## Contact Me
* E-mail: niyongsheng@Outlook.com
* Weibo: [@Ni永胜](https://weibo.com/u/7317805089)

## Contribution
Reward[:lollipop:](https://github.com/niyongsheng/niyongsheng.github.io/blob/master/Beg/README.md)  Encourage[:heart:](https://github.com/niyongsheng/NYSTK/stargazers)

## Tinks
[云中有傻狗](https://www.bilibili.com/video/BV1zJ411Y7jB?from=search&seid=12378720610423736804)
