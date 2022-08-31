# test_hubs使用手册

[TOC]

## 1. test_hubs介绍

- common：工作中需要的测试脚本
- config：脚本的配置文件
- data：数据驱动
- docs：相关文档
- logs：每次执行的log
- report：生成的测试报告
- run：unittest运行的主函数
- screenshots：测试截图
- shell：linux相关脚本
- test：debug测试脚本
- test_automation：
  - web_automation(web自动化测试框架)
  - api_automation(接口自动化测试框架)



## 2. 环境搭建

### 2.1 项目环境

- git clone https://gitee.com/cao-z/test_hubs.git

- 项目路径添加到系统路径

  ```
  win
  环境变量->系统变量->新建
  变量名：PYTHONPATH
  变量值：$<test_scripts绝对路径>
  
  linux
  # vi /etc/profile
  最后添加：export PYTHONPATH=$<test_scripts绝对路径>
  保存
  # source /etc/profile
  ```

### 2.2 Python环境

- 安装python3.9版本

  

### 2.3 Anaconda环境

- 默认使用conda配置环境

- 将环境包放在安装好的Anaconda/envs目录下
- 激活环境 conda activate test_envs

### 2.4 Selenium环境

- ChromeDriver下载：https://registry.npmmirror.com/binary.html?path=chromedriver/
- chromedriver.exe解压到anaconda/envs/test_envs目录下
