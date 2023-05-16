import plotly.graph_objs as go
import numpy as np
import glob
import plotly.io as pio
from scipy.optimize import fsolve
pio.templates["draft"] = go.layout.Template(
    layout_font = {'color': '#7F7F7F','family':"Arial Bold",'size':35},
    layout_colorway=[ '#FA7F6F', '#82B0D2','#8ECFC9', '#FFBE7A', '#BEB8DC', '#E7DAD2', '#999999']
    )
pio.templates.default = "simple_white+draft"

def v(rho, v_0, g=9, rho_max=10):
    
    value = v_0 * (1 - np.exp(-g * ((1 / rho) - (1 / rho_max))))
    return value

def find_intersection(g, v0_1, rho_max_1, v0_2, rho_max_2):
    def equation_to_solve(rho):
        return v(rho, v0_1, g, rho_max_1) - v(rho, v0_2, g, rho_max_2)
    
    initial_guess = 1
    rho_intersection = fsolve(equation_to_solve, initial_guess)
    v_intersection = v(rho_intersection, v0_1, g, rho_max_1)
    
    return rho_intersection, v_intersection

# 定义参数
# v_0_values = [0.5,1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# rho_max_values = [13,13, 13, 13, 13, 13, 2.5, 2.5, 0.5, 0.5]

# v_0_values = [1, 2, 3, 4] #SE
# rho_max_values = [13, 13, 13, 13] #SE
v_0_values = [1, 2, 3, 4, 5]
rho_max_values = [13, 13, 13, 2.5, 0.5]

# 计算曲线数据
# rho_values = [np.linspace(0.01, 13, 500),
#               np.linspace(0.01, 13, 500),
#               np.linspace(0.01, 13, 500),
#               np.linspace(0.01, 13, 500)]
rho_values = [np.linspace(0.01, 13, 500),
              np.linspace(0.01, 13, 500),
              np.linspace(0.01, 13, 500),
              np.linspace(0.01, 2, 500),
              np.linspace(0.01, 0.8, 800)]
data = []

d_v = np.loadtext('Fig1_a_NonAttacker.csv')

data.append(go.Scatter(x=d_v[:,0], y=d_v[:,1],opacity = 0.5,mode='markers',marker_color='#82B0D2',marker_symbol='diamond',showlegend=False))
# 显示图表
for i,v_0 in enumerate(v_0_values):
    v_values = v(rho_values[i], v_0,rho_max=rho_max_values[i])
    if v_0 >3:
        max_last = find_intersection(9,v_0,rho_max_values[i],v_0_values[i-1],rho_max_values[i-1])[1]
        v_values[v_values<max_last]=None
    trace = go.Scatter(x=rho_values[i], y=v_values, mode='lines',line_color='#4C7C9B',line_width=8,showlegend=False,opacity = 0.9)
    data.append(trace)

layout = go.Layout(width=1000,height=1000,xaxis_title='Density(m⁻²)',yaxis_title='Speed(ms⁻¹)',xaxis_range=[0, 10.1],yaxis_range=[0, 5.1])

fig = go.Figure(data=data, layout=layout)
