import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import plotly.io as pio

pio.templates["draft"] = go.layout.Template(
    layout_font = {'color': '#7F7F7F','family':"Arial Bold",'size':35},
    layout_colorway=[  '#82B0D2','#FA7F6F', '#FFBE7A','#8ECFC9', '#BEB8DC', '#E7DAD2', '#999999']
    )
pio.templates.default = "simple_white+draft"
C = px.colors.qualitative.Plotly
SYMBOL = ['triangle-up','x','diamond']


d_v = np.loadtxt('Fig1_a_Attacker.csv')
d_v_non = np.loadtxt('Fig1_a_NonAttacker.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(x=d_v[:,0], y=d_v[:,1],showlegend=False,
                         opacity = 0.8,mode='markers',name = 'Attackers',marker_symbol='diamond',marker_color='#82B0D2'))
fig.add_trace(go.Scatter(x=d_v_non[:,0], y=d_v_non[:,1],showlegend=False,
                    mode='markers',opacity = 0.8,marker_color='#FA7F6F',name = 'Non-Attacker'))

fig.update_layout(autosize=False,yaxis_showgrid=False,xaxis_showgrid=False,
         width=1000,height=1000,xaxis_title='Density(m⁻²)',yaxis_title='Speed(ms⁻¹)',font=dict(size=35))

fig.update_layout(
    xaxis_range=[0, 10.1],
    yaxis_range=[0, 5.1]
)
fig.show()