import numpy as np
import matplotlib.pyplot as plt

#constant define begin
pi=np.pi
#constant define end

class ECG_data():
    def __init__(self,time_span,rate,accuracy):
        self.time_span=time_span
        self.x=np.arange(accuracy,time_span+accuracy,accuracy)
        self.rate=rate
        self.li=30/rate

        self.a_pwav = 0.25
        self.d_pwav = 0.09
        self.t_pwav = 0.2

        self.a_qwav = 0.025
        self.d_qwav = 0.066
        self.t_qwav = 0.166

        self.a_qrswav = 1.6
        self.d_qrswav = 0.11

        self.a_swav = 0.25
        self.d_swav = 0.066
        self.t_swav = 0.09

        self.a_twav = 0.35
        self.d_twav = 0.142
        self.t_twav = 0.2

        self.a_uwav = 0.035
        self.d_uwav = 0.0476
        self.t_uwav = 0.433

        self.final_wave=0

    #Custom the parameters begin
    def set_pwav(self,amplitude,duration,time_shift):
        self.a_pwav = amplitude
        self.d_pwav = duration
        self.t_pwav = time_shift

    def set_qwav(self,amplitude,duration,time_shift):
        self.a_qwav = amplitude
        self.d_qwav = duration
        self.t_qwav = time_shift

    def set_qrswav(self,amplitude,duration):
        self.a_qrswav = amplitude
        self.d_qrswav = duration

    def set_swav(self,amplitude,duration,time_shift):
        self.a_swav = amplitude
        self.d_swav = duration
        self.t_swav = time_shift

    def set_twav(self,amplitude,duration,time_shift):
        self.a_twav = amplitude
        self.d_twav = duration
        self.t_twav = time_shift

    def set_uwav(self,amplitude,duration,time_shift):
        self.a_uwav = amplitude
        self.d_uwav = duration
        self.t_uwav = time_shift
    # Custom the parameters end

    # Calculate each wave begin
    def cal_pwav(self):
        l = self.li
        a = self.a_pwav
        x = self.x + self.t_pwav
        b = (2 * l) / self.d_pwav
        p1 = (1 / l)
        p1=0
        p2 = 0
        for i in range(1,101):
            harm1 = (((np.sin((pi / (2 * b)) * (b - (2 * i)))) / (b - (2 * i)) + (np.sin((pi / (2 * b)) * (b + (2 * i)))) / (
                    b + (2 * i))) * (2 / pi)) * np.cos((i * pi * x) / l)
            p2 = p2 + harm1
        pwav1 = p1 + p2
        pwav = a * pwav1
        return pwav

    def cal_qwav(self):
        l = self.li
        x = self.x + self.t_qwav
        a = self.a_qwav
        b = (2 * l) / self.d_qwav
        q1 = (a / (2 * b)) * (2 - b)
        q1=0
        q2 = 0
        for i in range(1,101):
            harm5 = (((2 * b * a) / (i * i * pi * pi)) * (1 - np.cos((i * pi) / b))) * np.cos((i * pi * x) / l)
            q2 = q2 + harm5

        qwav = -1 * (q1 + q2)
        return qwav

    def cal_qrswav(self):
        l = self.li
        x = self.x
        a = self.a_qrswav
        b = (2 * l) / self.d_qrswav
        qrs1 = (a / (2 * b))
        qrs1=0
        qrs2 = 0
        for i in range(1, 101):
            harm = (((2 * b * a) / (i * i * pi * pi)) * (1 - np.cos((i * pi) / b))) * np.cos((i * pi * x) / l)
            qrs2 = qrs2 + harm
        qrswav = qrs1 + qrs2
        return qrswav

    def cal_swav(self):
        l = self.li
        x = self.x - self.t_swav
        a = self.a_swav
        b = (2 * l) / self.d_swav
        s1 = (a / (2 * b)) * (2 - b)
        s1=0
        s2 = 0
        for i in range(1,101):
            harm3 = (((2 * b * a) / (i * i * pi * pi)) * (1 - np.cos((i * pi) / b))) * np.cos((i * pi * x) / l)
            s2 = s2 + harm3
        swav = -1 * (s1 + s2)
        return swav

    def cal_twav(self):
        l = self.li
        a = self.a_twav
        x = self.x - self.t_twav - 0.045
        b = (2 * l) / self.d_twav
        t1 = 1 / l
        t1=0
        t2 = 0
        for i in range(1,101):
            harm2 = (((np.sin((pi / (2 * b)) * (b - (2 * i)))) / (b - (2 * i)) + (np.sin((pi / (2 * b)) * (b + (2 * i)))) / (
                        b + (2 * i))) * (2 / pi)) * np.cos((i * pi * x) / l)
            t2 = t2 + harm2
        twav1 = t1 + t2
        twav = a * twav1
        return twav

    def cal_uwav(self):
        l = self.li
        a = self.a_uwav
        x = self.x - self.t_uwav
        b = (2 * l) / self.d_uwav
        u1 = 1 / l
        u2 = 0
        for i in range(1,101):
            harm4 = (((np.sin((pi / (2 * b)) * (b - (2 * i)))) / (b - (2 * i)) + (np.sin((pi / (2 * b)) * (b + (2 * i)))) / (
                        b + (2 * i))) * (2 / pi)) * np.cos((i * pi * x) / l)
            u2 = u2 + harm4

        uwav1 = u1 + u2
        uwav = a * uwav1
        return uwav
    # Calculate each wave end

    # Merge the wave begin
    def gen_wave(self):
        p_wave=self.cal_pwav()
        q_wave=self.cal_qwav()
        qrs_wave=self.cal_qrswav()
        s_wave=self.cal_swav()
        t_wave=self.cal_twav()
        u_wave=self.cal_uwav()
        final_wave=p_wave+q_wave+qrs_wave+s_wave+t_wave+u_wave
        self.final_wave=final_wave
        return
    # Merge the wave end

    # Plot wave begin
    def plot_signal(self):
        t_shift=self.time_span*0.05
        v_shift=(np.max(self.final_wave)-np.min(self.final_wave))*0.1
        x_lim=[0-t_shift,self.time_span+t_shift]
        y_lim=[np.min(self.final_wave)-v_shift,np.max(self.final_wave)+v_shift]

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set(xlim=x_lim, ylim=y_lim,title='ECG graph')
        ax.plot(self.x, self.final_wave)
        ax.grid(visible=True, which='major', axis='both')
        plt.show()
    # Plot wave end

if __name__=='__main__':
    a=ECG_data(time_span=3,rate=60,accuracy=0.01)
    a.gen_wave()
    a.plot_signal()