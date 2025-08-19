import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import butter, filtfilt

class FBGSensor:
    def __init__(self, precision=0.1):
        # 传感器参数初始化
        self.precision = precision
        self.calibration_factor = 0.001
        self.bragg_wavelength = 1550.0
        self.filter_b, self.filter_a = butter(3, 0.1)
        self.reset_history()
    
    def reset_history(self):
        self.strain_history = []
        self.wavelength_history = []
        self.timestamps = []
    
    def measure_strain(self, true_strain):
        # 测量应变并滤波
        noise = random.gauss(0, self.precision/3)
        raw_strain = true_strain + noise
        
        if len(self.strain_history) >= 10:
            filtered = filtfilt(self.filter_b, self.filter_a, self.strain_history[-10:] + [raw_strain])
            measured_strain = filtered[-1]
        else:
            measured_strain = raw_strain
        
        wavelength_shift = self.bragg_wavelength * self.calibration_factor * measured_strain
        current_wavelength = self.bragg_wavelength + wavelength_shift
        
        self.strain_history.append(measured_strain)
        self.wavelength_history.append(current_wavelength)
        self.timestamps.append(time.time())
        
        return measured_strain, current_wavelength

class RGBWLEDController:
    def __init__(self, num_leds=24):
        self.num_leds = num_leds
        self.led_colors = np.zeros((num_leds, 4))
    
    def strain_to_color(self, strain, wavelength):
        # 应变值到颜色映射
        if strain < -50: base_hue = 240
        elif strain < 50: base_hue = 120
        else: base_hue = 0
        
        hue_variation = (wavelength - 1545) / 10 * 30
        hue = (base_hue + hue_variation) % 360
        
        h = hue / 360.0
        s = min(1.0, 0.8 + abs(strain)/200)
        v = min(1.0, 0.5 + abs(strain)/300)
        r, g, b = self.hsv_to_rgb(h, s, v)
        
        w = min(r, g, b) * 0.7
        return r, g, b, w
    
    def hsv_to_rgb(self, h, s, v):
        # HSV转RGB
        if s == 0.0: return v, v, v
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0: return v, t, p
        if i == 1: return q, v, p
        if i == 2: return p, v, t
        if i == 3: return p, q, v
        if i == 4: return t, p, v
        if i == 5: return v, p, q
    
    def update_leds(self, strain, wavelength):
        # 更新LED颜色
        base_r, base_g, base_b, base_w = self.strain_to_color(strain, wavelength)
        for i in range(self.num_leds):
            var = 0.05 * (i / self.num_leds)
            self.led_colors[i] = [
                max(0, min(1, base_r + random.uniform(-var, var))),
                max(0, min(1, base_g + random.uniform(-var, var))),
                max(0, min(1, base_b + random.uniform(-var, var))),
                max(0, min(1, base_w + random.uniform(-var, var)))
            ]
        return self.led_colors

class TensionVisualizationSystem:
    def __init__(self):
        self.fbg = FBGSensor()
        self.led_controller = RGBWLEDController()
        
        # 设置中文字体, 避免中文乱码, 并设置负号正常显示
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        
        # 创建可视化界面
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        self.fig.suptitle('智能光弦系统 - 实时监测', fontsize=16)
        self.strain_line, = self.ax1.plot([], [], 'b-', lw=2)
        self.wavelength_line, = self.ax2.plot([], [], 'g-', lw=2)
        self.led_plot = self.ax3.imshow(np.zeros((5, 5, 4)), extent=[0, 10, 0, 10])
        self.ax3.axis('off')
        
        # 初始化数据
        self.time_data = []
        self.strain_data = []
        self.wavelength_data = []
    
    def simulate_string_vibration(self, t):
        # 弦体振动模拟
        return 80 * np.sin(2 * np.pi * 0.5 * t) + 20 * np.sin(2 * np.pi * 2.3 * t)
    
    def update(self, frame):
        # 更新动画帧
        t = time.time()
        true_strain = self.simulate_string_vibration(t)
        strain, wavelength = self.fbg.measure_strain(true_strain)
        led_colors = self.led_controller.update_leds(strain, wavelength)
        
        self.time_data.append(t - self.fbg.timestamps[0])
        self.strain_data.append(strain)
        self.wavelength_data.append(wavelength)
        
        if len(self.time_data) > 100:
            self.time_data.pop(0)
            self.strain_data.pop(0)
            self.wavelength_data.pop(0)
        
        self.strain_line.set_data(self.time_data, self.strain_data)
        self.ax1.set_xlim(max(0, self.time_data[0]), max(10, self.time_data[-1]))
        self.wavelength_line.set_data(self.time_data, self.wavelength_data)
        self.ax2.set_xlim(max(0, self.time_data[0]), max(10, self.time_data[-1]))
        
        led_matrix = np.zeros((5, 5, 4))
        for i in range(5):
            for j in range(5):
                idx = (i * 5 + j) % self.led_controller.num_leds
                led_matrix[i, j] = led_colors[idx]
        self.led_plot.set_array(led_matrix)
        
        return self.strain_line, self.wavelength_line, self.led_plot

    def run(self):
        ani = FuncAnimation(self.fig, self.update, frames=100, interval=50, blit=False)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()

if __name__ == "__main__":
    system = TensionVisualizationSystem()
    system.run()