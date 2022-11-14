import pandas as pd
import plotly.graph_objects as go
import streamlit as st

url1 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_raw_202210180850.csv'
df = pd.read_csv(url1)
st.set_page_config(layout='wide')

st.image('https://raw.githubusercontent.com/rvoktrzl/tetris/main/dqlab.png')

st.markdown("""
<style>
.title-font {
    font-size:48px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title-font">Dunia dalam Peningkatan Inflasi, Bagaimana dengan Indonesia?</p>', unsafe_allow_html=True)

st.write('Pecahnya perang Rusia-Ukraina per 24 Februari 2022, telah mendorong meningkatnya tingkat inflasi dunia. Berdasarkan data yang dirilis OECD, hingga September 2022 tingkat inflasi dunia berada pada angka **10,30%**. Secara *year-on-year growth* jika dibandingkan dengan tingkat inflasi dunia pada September 2021, tingkat inflasi dunia telah meningkat hingga **5,20%**.')

st.markdown("""
<style>
.header-font {
    font-size:28px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.subheader-font {
    font-size:24px !important;
}
</style>
""", unsafe_allow_html=True)

c1 = st.container()
c1.markdown('<p class="header-font"<div style="text-align: center;">Tingkat Inflasi Dunia VS Tingkat Inflasi Indonesia</div></p>', unsafe_allow_html=True)
c1.markdown('<p class="subheader-font"<div style="text-align: left;">Uji Korelasi</div></p>', unsafe_allow_html=True)
col1, col2, col3 = c1.columns(3)
c1.write('')
col1.write('Sebelum perang, Januari 2019 hingga Januari 2022 dengan nilai korelasi')
col1.write('# -0.21')
col2.write('Setelah perang, Februari 2022 hingga September 2022 dengan nilai korelasi')
col2.write('# 0.86')
col3.write('Perang menyebabkan perubahan nilai korelasi dari lemah menjadi sangat kuat.')
st.write('')

st.write('')
c2 = st.container()
c2.markdown('<p class="header-font"<div style="text-align: left;">Tingkat inflasi dunia dan Indonesia</div></p>', unsafe_allow_html=True)
c2.write('**Tingkat inflasi dunia** dan **tingkat inflasi Indonesia** per **Januari 2019** hingga **September 2022**.')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Tingkat Inflasi Dunia'], 
                         name='Tingkat Inflasi Dunia', mode='lines'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Tingkat Inflasi Indonesia'], 
                         name='Tingkat Inflasi Indonesia', mode='lines'))
fig.update_layout(autosize=True)
c2.plotly_chart(fig)

c3 = st.container()
col1, col2, col3 = c3.columns(3)
col1.write('Tingkat inflasi dunia dan Indonesia dibawah')
col1.write('# 5.00%')
col1.write('selama pandemi covid-19 periode Maret 2020 hingga Agustus 2021.')
col2.write('Peningkatan signifikan setelah pecahnya perang Rusia-Ukraina pada 24 Februari 2022.')
col3.write('*Year-on-year growth* tingkat inflasi Indonesia')
col3.write('# 4.35%')
col3.write('September 2021 VS September 2022.')
st.write('')

st.write('')
c4 = st.container()
col1, col2 = c4.columns(2)
col1.write('Hubungan linier positif yang sangat kuat menjadi nilai korelasi antara tingkat inflasi dunia terhadap harga komoditi energi dunia yang dilihat berdasarkan harga minyak dunia periode Januari 2019 hingga September 2022. Jika inflasi dunia meningkat, maka harga komoditi energi dunia akan ikut meningkat. Bagaimana dengan Indonesia?')
col2.write('# Nilai korelasi 0.87')
st.write('')

st.write('')
c5 = st.container()
c5.markdown('<p class="header-font"<div style="text-align: center;">Tingkat Inflasi Indonesia VS Harga Komoditi Energi di Indonesia</div></p>', unsafe_allow_html=True)
c5.markdown('<p class="subheader-font"<div style="text-align: left;">Uji Korelasi</div></p>', unsafe_allow_html=True)
col1, col2 = c5.columns(2)
c5.write('')
col1.write('Hasil uji korelasi berlinier positif kuat dengan nilai korelasi')
col1.write('# 0.71')
col2.write('Menunjukkan bahwa tingkat inflasi Indonesia mempengaruhi harga komoditi energi di Indonesia.')
st.write('')

st.write('')
c6 = st.container()
c6.write('Seberapa besar peningkatan harga komoditi energi di Indonesia dengan peningkatan tingkat inflasi *year-on-year* sebesar **4,35%**?')
st.write('')

st.write('')
c7 = st.container()
c7.markdown('<p class="subheader-font"<div style="text-align: left;">Pertumbuhan Komoditi Energi di Indonesia</div></p>', unsafe_allow_html=True)
c7.write('Pertumbuhan komoditi energi di Indonesia per **September 2021** hingga **September 2022**.')
url3 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_energi_202210180818.csv'
df_energi = pd.read_csv(url3)

fig_energi_bar = go.Figure(go.Bar(
            x=df_energi['YoY Growth (%)'],
            y=df_energi['Komoditi Energi'],
            orientation='h'))
fig_energi_bar.update_layout(autosize=True)
c7.plotly_chart(fig_energi_bar)

st.write('Tingkat inflasi dunia per bulan September 2022 telah mengalami peningkatan *year-on-year* sebesar **5,20%** dan mendorong peningkatan tingkat inflasi Indonesia *year-on-year* sebesar **4,35%**. Dimana masing-masing tingkat inflasi dunia dan tingkat inflasi Indonesia saat ini berada pada angka **10,30%** dan **5,95%**. Salah satu dampak peningkatan tingkat inflasi ini adalah mendorong terjadinya kenaikan harga yang cukup signifikan pada komoditi energi.')
st.write('Jika hal ini terus berlanjut, tentu akan memperburuk keadaan ekonomi kedepannya dan berdampak pada aspek-aspek dalam lingkup ekonomi lainnya yang tidak diukur dalam analisis ini. Untuk itu kita harus bisa menentukan sikap dalam mengatur bagaimana bertahan dalam keadaan ekonomi tersebut. Dimulai dengan mengatur pengeluaran dan simpanan uang, mengatur investasi dan aset yang mungkin terdampak, serta mengatur pembayaran hutang atau cicilan.')

st.caption('Sumber Data:')
st.caption('https://www.oecd.org/newsroom/consumer-prices-oecd-updated-3-november-2022.htm')
st.caption('https://www.statista.com/statistics/1317738/global-inflation-rate-monthly/#:~:text=CPI%20inflation%20rate%20worldwide%202019%2D2022&text=In%20March%202022%2C%20the%20global,7.47%20percent%20in%20February%202022')
st.caption('https://www.bi.go.id/id/statistik/indikator/data-inflasi.aspx')
st.caption('https://bisnis.tempo.co/read/1630292/inilah-rincian-kenaikan-harga-bbm-pertamina-5-tahun-terakhir')
st.caption('https://industri.kontan.co.id/news/berikut-daftar-harga-bbm-terbaru-pertamina-pasca-kenaikan-harga-bbm')
