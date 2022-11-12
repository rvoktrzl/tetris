import streamlit as st
import pandas as pd
import plotly.graph_objects as go

url1 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_raw_202210180850.csv'
df = pd.read_csv(url1)
st.set_page_config(layout='centered')

st.image('https://raw.githubusercontent.com/rvoktrzl/tetris/main/inflation.jpg')

st.title('Dunia dalam Peningkatan Inflasi, Bagaimana dengan Indonesia?')

st.write('Pecahnya perang Rusia-Ukraina per 24 Februari 2022, telah mendorong meningkatnya tingkat inflasi dunia. Berdasarkan data yang dirilis OECD, hingga September 2022 tingkat inflasi dunia berada pada angka **10,30%**. Secara *year-on-year growth* jika dibandingkan dengan tingkat inflasi dunia pada September 2021, tingkat inflasi dunia telah meningkat hingga **5,20%**.')
st.write('')

c1 = st.container()
c1.write('<div style="text-align: center;">Tingkat Inflasi Dunia VS Tingkat Inflasi Indonesia</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
c1.write('')
c1.write('**Uji Korelasi**')
col1.write('Sebelum perang, Januari 2019 hingga Januari 2022')
col1.write('# -0.21')
col2.write('Setelah perang, Februari 2022 hingga September 2022')
col2.write('# 0.86')
col3.write('Perang menyebabkan perubahan nilai korelasi dari lemah menjadi sangat kuat.')

c2 = st.container()
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Tingkat Inflasi Dunia'], 
                         name='Tingkat Inflasi Dunia', mode='lines'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Tingkat Inflasi Indonesia'], 
                         name='Tingkat Inflasi Indonesia', mode='lines'))
fig.update_layout(autosize=True,
                  title='Tingkat inflasi dunia dan Indonesia per Januari 2019 hingga September 2022')
c2.plotly_chart(fig)

col1, col2, col3 = st.columns(3)
col1.write('Tingkat inflasi dunia dan Indonesia dibawah')
col1.write('# 5.00%')
col1.write('selama pandemi covid-19 periode Maret 2020 hingga Agustus 2021.')
col2.write('Peningkatan signifikan setelah pecahnya perang Rusia-Ukraina pada 24 Februari 2022.')
col3.write('*Year-on-year growth* tingkat inflasi Indonesia')
col3.write('# 4.35%')
col3.write('September 2021 VS September 2022.')

col1, col2 = st.columns(2)
col1.write('# Nilai Korelasi 0.87')
col2.write('Hubungan linier positif yang sangat kuat menjadi nilai korelasi antara tingkat inflasi dunia terhadap harga komoditi energi dunia yang dilihat berdasarkan harga minyak dunia periode Januari 2019 hingga September 2022. Jika inflasi dunia meningkat, maka harga komoditi energi dunia akan ikut meningkat. Bagaimana dengan Indonesia?')

c3 = st.container()
c3.write('<div style="text-align: center;">Tingkat Inflasi Indonesia VS Harga Komoditi Energi di Indonesia</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
c3.write('')
c3.write('**Uji Korelasi**')
col1.write('Hasil uji korelasi berlinier positif kuat dengan nilai korelasi')
col1.write('# 0.71')
col2.write('Menunjukkan bahwa tingkat inflasi Indonesia mempengaruhi harga komoditi energi di Indonesia.')

st.write('Seberapa besar peningkatan harga komoditi energi di Indonesia dengan peningkatan tingkat inflasi *year-on-year* sebesar **4,35%**?')

url3 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_energi_202210180818.csv'
df_energi = pd.read_csv(url3)

fig_energi_bar = go.Figure(go.Bar(
            x=df_energi['YoY Growth (%)'],
            y=df_energi['Komoditi Energi'],
            orientation='h'))
fig_energi_bar.update_layout( 
                  title='Pertumbuhan Komoditi Energi di Indonesia per September 2021 hingga September 2022')
st.plotly_chart(fig_energi_bar)

st.write('Tingkat inflasi dunia per bulan September 2022 telah mengalami peningkatan *year-on-year* sebesar **5,20%** dan mendorong peningkatan tingkat inflasi Indonesia *year-on-year* sebesar **4,35%**. Dimana masing-masing tingkat inflasi dunia dan tingkat inflasi Indonesia saat ini berada pada angka **10,30%** dan **5,95%**. Salah satu dampak peningkatan tingkat inflasi ini adalah mendorong terjadinya kenaikan harga yang cukup signifikan pada komoditi energi.')
st.write('Jika hal ini terus berlanjut, tentu akan memperburuk keadaan ekonomi kedepannya dan berdampak pada aspek-aspek dalam lingkup ekonomi lainnya yang tidak diukur dalam analisis ini. Untuk itu kita harus bisa menentukan sikap dalam mengatur bagaimana bertahan dalam keadaan ekonomi tersebut. Dimulai dengan mengatur pengeluaran dan simpanan uang, mengatur investasi dan aset yang mungkin terdampak, serta mengatur pembayaran hutang atau cicilan.')

st.caption('Sumber Data:')
st.caption('https://www.oecd.org/newsroom/consumer-prices-oecd-updated-3-november-2022.htm')
st.caption('https://www.statista.com/statistics/1317738/global-inflation-rate-monthly/#:~:text=CPI%20inflation%20rate%20worldwide%202019%2D2022&text=In%20March%202022%2C%20the%20global,7.47%20percent%20in%20February%202022')
st.caption('https://www.bi.go.id/id/statistik/indikator/data-inflasi.aspx')
st.caption('https://bisnis.tempo.co/read/1630292/inilah-rincian-kenaikan-harga-bbm-pertamina-5-tahun-terakhir')
st.caption('https://industri.kontan.co.id/news/berikut-daftar-harga-bbm-terbaru-pertamina-pasca-kenaikan-harga-bbm')
