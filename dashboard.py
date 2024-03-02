import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#Masukkan Data 
day_df=pd.read_csv('day_new.csv')
hour_df=pd.read_csv('hour_new.csv')

st.title('Proyek Data Analisis Bike Sharing')
# Deskripsi singkat
st.write('Pada halaman ini akan dianalisis dataset rental sepeda di Washington D. C. Tahun 2011 dan 2012')
# Tampilkan gambar
st.image('rental.jpg', caption='source: https://chattahoochee.whitewaterexpress.com/activity/bike-rentals/',use_column_width=True)
text="""Sistem rental sepeda adalah penyewaan sepeda tradisional dengan  seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian dilakukan otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan mengembalikannya di posisi lain. Saat ini, ada sekitar lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda salah satunya di Washington D. C."""
st.write('')
st.write(f"<p style='text-align: justify;'>{text}</p>", unsafe_allow_html=True)

with st.sidebar:
    
    st.text('Proyek dikerjakan oleh:')
    st.write('Muhammad Faizal')
    st.write('')
    st.text('Penyelenggara:')
    st.write('Dicoding')

st.header('Dataset')
# Tampilkan describe() output dari day_df
st.write("Deskripsi tabel day_df:")
st.write(day_df.head())
st.write("Data source: [day.csv](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

# Tampilkan describe() output dari hour_df
st.write("Deskripsi tabel hour_df:")
st.write(hour_df.head())
st.write("Data source: [hour.csv](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

st.header('Pertanyaan Bisnis')
# Masukkan pertanyaan 
text = "1. Bagaimana tren penggunaan sepeda berdasarkan kondisi cuaca selama dua tahun terakhir di Washington D. C.?"

# Definisikan gaya bubble CSS
bubble_style = """
<style>
.bubble-text {
    background-color: #f0f0f0;
    color: #333;
    padding: 10px 20px;
    border-radius: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    display: inline-block;
}
</style>
"""

# Tampilkan menggunakan HTML
st.markdown(bubble_style, unsafe_allow_html=True)
st.markdown(f"<div class='bubble-text'>{text}</div>", unsafe_allow_html=True)
# Masukkan pertanyaan
text = "2. Bagaimana perbedaan pola penggunaan sepeda antara hari kerja dan hari libur selama dua tahun terakhir di Washington D. C.?"

# Definisikan gaya bubble CSS
bubble_style = """
<style>
.bubble-text {
    background-color: #f0f0f0;
    color: #333;
    padding: 10px 20px;
    border-radius: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    display: inline-block;
}
</style>
"""

# Tampilkan menggunakan HTML
st.markdown(bubble_style, unsafe_allow_html=True)
st.markdown(f"<div class='bubble-text'>{text}</div>", unsafe_allow_html=True)

st.header('Alur Analisis')

import streamlit as st

# Daftar Alur
items = ["Gathering", "Assesing", "Cleaning","Exploratory Data Analysis (EDA)","Visualization & Explanatory Analysis","Conclusion","Teknik Analisis Lanjutan"]

# Tampilkan
for i, item in enumerate(items, start=1):
    st.write(f"{i}. {item}")
st.header('Hasil')
# Masukkan pertanyaan 
text = "1. Bagaimana tren penggunaan sepeda berdasarkan kondisi cuaca selama dua tahun terakhir di Washington D. C.?"

# Definisikan gaya bubble CSS
bubble_style = """
<style>
.bubble-text {
    background-color: #f0f0f0;
    color: #333;
    padding: 10px 20px;
    border-radius: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    display: inline-block;
}
</style>
"""

# Tampilkan menggunakan HTML
st.markdown(bubble_style, unsafe_allow_html=True)
st.markdown(f"<div class='bubble-text'>{text}</div>", unsafe_allow_html=True)

st.write('')
# Mengelompokkan data per jenis kondisi cuaca (weathersit) dan menghitung jumlah total penggunaan sepeda
weather_total = day_df.groupby(day_df['weathersit'])['cnt'].sum()

# Membuat bar chart horizontal
fig, ax = plt.subplots(figsize=(9, 6))
weather_total.plot(kind='barh', color="#72BCD4", ax=ax)
ax.set_title('Total Penggunaan Sepeda per Jenis Kondisi Cuaca 2 Tahun')
ax.set_xlabel('Total Penggunaan Sepeda')
ax.set_ylabel('Kondisi Cuaca')
ax.set_yticks(range(0, 4))
ax.set_yticklabels(['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow'])
ax.grid(axis='x')
for index, value in enumerate(weather_total):
    ax.text(value, index, str(value))

# Tampilkan di Streamlit
st.pyplot(fig)
text="""Dari visualisasi pertama, terlihat bahwa penggunaan sepeda paling tinggi terjadi pada kondisi cuaca yang cerah (Clear), diikuti oleh kondisi cuaca berkabut (Mist). Penggunaan sepeda cenderung lebih rendah pada kondisi cuaca dengan hujan ringan atau salju ringan, dan sangat rendah bahkan tidak ada data pada kondisi cuaca dengan hujan deras atau salju tebal."""
st.write('')
st.write(f"<p style='text-align: justify;'>{text}</p>", unsafe_allow_html=True)

# Masukkan pertanyaan
text = "2. Bagaimana perbedaan pola penggunaan sepeda antara hari kerja dan hari libur selama dua tahun terakhir di Washington D. C.?"

# Definisikan gaya bubble CSS
bubble_style = """
<style>
.bubble-text {
    background-color: #f0f0f0;
    color: #333;
    padding: 10px 20px;
    border-radius: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    display: inline-block;
}
</style>
"""

# Tampilkan menggunakan HTML
st.markdown(bubble_style, unsafe_allow_html=True)
st.markdown(f"<div class='bubble-text'>{text}</div>", unsafe_allow_html=True)
st.write('')

# Mengelompokkan data per jam, berdasarkan hari kerja (workingday) atau hari libur (holiday)
hourly_avg_workday = hour_df[hour_df['workingday'] == 1].groupby(hour_df['hr'])['cnt'].mean()
hourly_avg_holiday = hour_df[hour_df['workingday'] == 0].groupby(hour_df['hr'])['cnt'].mean()

# Membuat line chart
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(hourly_avg_workday, marker='o', label='Hari Kerja')
ax2.plot(hourly_avg_holiday, marker='o', label='Hari Libur')
ax2.set_title('Rata-Rata Penggunaan Sepeda per Jam pada Hari Kerja dan Hari Libur')
ax2.set_xlabel('Jam (0-23)')
ax2.set_ylabel('Rata-Rata Penggunaan Sepeda')
ax2.grid(True)
ax2.set_xticks(range(24))
ax2.legend()
st.pyplot(fig2)

# Tampilkan di Streamlit
text="""Dari visualisasi kedua, dapat dilihat bahwa rata-rata penggunaan sepeda lebih tinggi pada hari kerja dibandingkan dengan hari libur di sebagian besar jam. Terlihat bahwa lonjakan penggunaan sepeda naik pada pukul 8 Pagi sebagai jam masuk kerja dan pukul 17 Sore sebagai jam pulang kerja. Ini menunjukkan bahwa sebagian besar pengguna sepeda menggunakan sepeda mereka untuk keperluan komuter atau bekerja pada hari kerja."""
st.write('')
st.write(f"<p style='text-align: justify;'>{text}</p>", unsafe_allow_html=True)

st.header('Analisis Lanjutan')

# Mengelompokkan data berdasarkan musim, hari kerja, dan kondisi cuaca, serta menghitung jumlah total penggunaan sepeda
seasonal_total = day_df.groupby('season')['cnt'].sum()
workday_total = day_df.groupby('workingday')['cnt'].sum()
weather_total = day_df.groupby('weathersit')['cnt'].sum()

# Membuat visualisasi dengan diagram batang horizontal
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Visualisasi untuk musim
axes[0].barh(seasonal_total.index, seasonal_total.values, color='#72BCD4')
axes[0].set_title('Total Penggunaan Sepeda per Musim')
axes[0].set_xlabel('Total Penggunaan Sepeda')
axes[0].set_ylabel('Musim')

# Visualisasi untuk hari kerja
axes[1].barh(workday_total.index, workday_total.values, color='#72BCD4')
axes[1].set_title('Total Penggunaan Sepeda pada Hari Kerja dan Hari Libur')
axes[1].set_xlabel('Total Penggunaan Sepeda')
axes[1].set_ylabel('Hari Kerja (0) / Hari Libur (1)')

# Visualisasi untuk kondisi cuaca
axes[2].barh(weather_total.index, weather_total.values, color='#72BCD4')
axes[2].set_title('Total Penggunaan Sepeda per Kondisi Cuaca')
axes[2].set_xlabel('Total Penggunaan Sepeda')
axes[2].set_ylabel('Kondisi Cuaca')

plt.tight_layout()
# Tampilkan visualisasi di Streamlit dengan judul yang sesuai
st.write("Visualisasi Total Penggunaan Sepeda")
st.write("")

# Tampilkan setiap plot secara terpisah
st.pyplot(fig)