from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df=pd.read_csv("marks.csv")
mew=df["Totals"][1:216].mean()
std=df["Totals"][1:216].std()
df["Totals"]=df["Totals"].astype(float)
k=df["Totals"].to_list()
for i in range(0,len(k)):
    if(k[i]>=(mew+1.5*std)):
        df.loc[i,"Grades"]="A"    
    if((mew+1*std)<k[i]<=(mew+1.5*std)):
        df.loc[i,"Grades"]="A-"
    if((mew+0.5*std)<k[i]<=(mew+1*std)):
        df.loc[i,"Grades"]="B"
    if((mew)<k[i]<=(mew+0.5*std)):
        df.loc[i,"Grades"]="B-"
    if((mew-0.5*std)<k[i]<=(mew)):
        df.loc[i,"Grades"]="C"
    if((mew-1*std)<k[i]<=(mew-0.5*std)):
        df.loc[i,"Grades"]="C-"
    if((mew-1.5*std)<k[i]<=(mew-std)):
        df.loc[i,"Grades"]="D"
    if(k[i]<(mew-1.5*std)):
        df.loc[i,"Grades"]="F" 
g=["A","A-","B","B-","C","C-","D","F"]
k=[15,15,20,25,25]
labels=["Quiz","Mids","End","Presentation","project"]
y=[i for i in range(int(mew),int(mew+1.5*std))]
# plt.title("Marking system")
# sns.histplot(data=df,x=df["Grades"],hue=df["Grades"])
# plt.pie(k,
# plt.show()
fig=px.histogram(df,x=df["Grades"],labels=g,color=df["Grades"])
fig1=px.pie(values=k,names=labels)
fig.show()
df.to_html("markdghss.html")



