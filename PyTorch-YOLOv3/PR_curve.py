import matplotlib.pyplot as plt
# Grafica mostrada en el paper, guardando los datos(precision y cobertura) obtenidos para cada 
# umbral de confianza. X=Recall Y=Precision.
# Precisión y cobertura obtenidos con test.py

x1 = [0.076,0.08,0.082,0.085]
y1 = [0.02,0.019,0.015,0.008]

x2 = [0.076,0.078,0.082,0.081]
y2 = [0.021,0.019,0.012,0.009]

x3 = [0.079,0.08,0.082,0.084]
y3 = [0.022,0.02,0.019,0.016]

axes = plt.gca()
axes.set_xlim([0,0.1])
axes.set_ylim([0,0.03])
plt.plot(x1, y1, marker='', color='olive', linewidth=2, linestyle='dotted', label="5 epoch trained model-No Rotation")
plt.plot(x2, y2, marker='', color='black', linewidth=2, linestyle='solid', label="7 epoch trained model-No Rotation")
plt.plot(x3, y3, marker='', color='magenta', linewidth=2, linestyle='dashed', label="7 epoch trained model-Rotation")
plt.xlabel('Recall', fontsize=14)
plt.ylabel('Precision', fontsize=14)
plt.legend()
plt.title('200-class precision-recall curve')
plt.grid()
f = plt.gcf()
plt.show()
f.savefig('pr_curve.jpg')
