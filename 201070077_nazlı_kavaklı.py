import matplotlib.pyplot as plt

# Pasta grafiğinde gösterilecek veriler
labels = ['Elma', 'Muz', 'Kiraz', 'Çilek']
sizes = [15, 30, 45, 10]  # Her bir dilimin büyüklüğü
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Renkler
explode = (0.1, 0, 0, 0)  # İlk dilimi biraz dışarı çıkartmak için

# Pasta grafiğini oluşturma
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Eşit oranlı daire
plt.title('Meyve Dağılımı')
plt.show()
