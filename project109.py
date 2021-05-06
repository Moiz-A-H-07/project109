import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=statistics.mean(data)
sd=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)
print(mean , sd , median , mode )
fsds,fsde=mean-sd,mean+sd
ssds,ssde=mean-(2*sd),mean+(2*sd)
tsds,tsde=mean-(3*sd),mean+(3*sd)
listofdatainfsds=[result for result in data if result>fsds and result<fsde]
listofdatainssds=[result for result in data if result>ssds and result<ssde]
listofdataintsds=[result for result in data if result>tsds and result<tsde]
print("fsds:",format(len(listofdatainfsds)*100.0/len(data)))
print("ssds:",format(len(listofdatainssds)*100.0/len(data)))
print("tsds:",format(len(listofdataintsds)*100.0/len(data)))
fig=ff.create_distplot([data],["result"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode="lines",name="fsds"))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode="lines",name="fsde"))

fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode="lines",name="ssds"))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode="lines",name="ssde"))

fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode="lines",name="tsds"))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode="lines",name="tsde"))

fig.show()