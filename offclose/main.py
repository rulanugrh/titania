import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("./dataset/penanganan-sampah.csv")
frame_2022 = pd.read_csv("./dataset/penanganan-sampah-2022.csv")

explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05) 
colors = ['#B17457', '#FFD09B', 'steelblue', '#CB80AB', '#6C4E31', '#FFB22C'] 

fig, (axis1, axis2) = plt.subplots(2, 2)

frame_2022.groupby(['wilayah']).sum().plot(kind="pie", ax=axis1[0], y="timbulan_sampah_ton",  labels=None, ylabel="presentase", title="Timbulan Sampah 2022" ,autopct="%1.0f%%", explode=explode, colors=colors)
frame_2022.groupby(['wilayah']).sum().plot(kind="pie", ax=axis1[1], y="pengolahan_ton", labels=None, ylabel="presentase", title="Sampah Terolah 2022" ,autopct="%1.0f%%", explode=explode, colors=colors)
frame.groupby(['wilayah']).sum().plot(kind="pie", ax=axis2[0], y="timbulan_sampah", labels=None, ylabel="presentase", title="Timbulan Sampah 2023" ,autopct="%1.0f%%", explode=explode, colors=colors)
frame.groupby(['wilayah']).sum().plot(kind="pie", ax=axis2[1], y="sampah_terolah", labels=None, ylabel="presentase", title="Sampah Terolah 2023" ,autopct="%1.0f%%", explode=explode, colors=colors)

plt.suptitle("Penanganan Sampah 2022 - 2023")
plt.show()