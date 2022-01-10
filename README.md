# ECG_generator
## ECG_generator based on Fourier series
### English Introduction

The program include a useful class in N_generate, and the document "main.py" is empty, stay for further update.

The program can generate ECG signal by changing the parameters of it.

The class include 15 functions in it, they can be divided into 5 classes.

- **Initialization**
  - def \_\_init__(self,time_span,rate,accuracy)
  
    *Initialize the class, there is some defult parameters in it*
- **Set parameters**
  - def set_pwav(self,amplitude,duration,time_shift):
  - def set_qwav(self,amplitude,duration,time_shift):
  - def set_qrswav(self,amplitude,duration):
  - def set_swav(self,amplitude,duration,time_shift):
  - def set_twav(self,amplitude,duration,time_shift):
  - def set_uwav(self,amplitude,duration,time_shift):

    *To set the parameters, All the functions are same. Mention: the first QRS wave was considered lay on the x=0, so it doesn't have the parameter:"time shift"*
- **Calculate waves**
  - def cal_pwav(self)
  - def cal_qwav(self)
  - def cal_qrswav(self)
  - def cal_swav(self)
  - def cal_twav(self)
  - def cal_uwav(self)

    *You shouldn't use any of them because there is another function will call them. The algorithm is based on Fourier series.*
- **Generate ECG wave**
  - def gen_wave(self):

    *By calling this, the class will calculate the ECG wave.*
- **Other function**
  - def plot_signal(self):
    
    *Plot a graph in a fit way.*

When you do the instantiation of the class, you should enter "time_span=","rate=","accuracy". And the defult parameters are 2, 60, 0.01

---
### 中文介绍

该程序在N_generate中存在一个有用的类，但文档“main.py”为空，保留给未来的更新。

该程序可以通过改变心电信号的参数来产生心电信号。

这个类包含了15个函数，它们可以分为5类。
- **初始化**
  - def \_\_init__(self,time_span,rate,accuracy)
  
    *初始化类，里面有一些默认参数*
- **设置参数**
  - def set_pwav(self,amplitude,duration,time_shift):
  - def set_qwav(self,amplitude,duration,time_shift):
  - def set_qrswav(self,amplitude,duration):
  - def set_swav(self,amplitude,duration,time_shift):
  - def set_twav(self,amplitude,duration,time_shift):
  - def set_uwav(self,amplitude,duration,time_shift):

    *设置参数时，每个函数作用相同。说明:第一个QRS波被认为是落在x=0上的（定位用），所以它没有参数:“时间偏移”*
- **计算波形**
  - def cal_pwav(self)
  - def cal_qwav(self)
  - def cal_qrswav(self)
  - def cal_swav(self)
  - def cal_twav(self)
  - def cal_uwav(self)

    *你不该调用它们中的任何一个，因为会有另一个函数调用它们。算法是基于傅里叶级数*
- **生成心电信号**
  - def gen_wave(self):

    *通过调用这个函数，类的实例将计算ECG波。*
- **其他函数**
  - def plot_signal(self):
    
    *我们贴心地提供了画图函数qwq*

当您执行类的实例化时，您应该输入 "time_span=","rate=","accuracy". 默认值是 2, 60, 0.01
