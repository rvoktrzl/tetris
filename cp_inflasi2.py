import streamlit as st
import pandas as pd
import plotly.graph_objects as go

url1 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_raw_202210180850.csv'
df = pd.read_csv(url1)
st.set_page_config(layout='wide')

st.image('https://raw.githubusercontent.com/rvoktrzl/tetris/main/inflation.jpg', width=1250)

st.title('Dunia dalam Peningkatan Inflasi, Bagaimana dengan Indonesia?')
st.markdown('Rivo Oktrizal - Capstone Project TETRIS PRoA 2022')
st.markdown('<div style="text-align: justify;">Dalam pengamatan di laman Google Trends, ternyata pencarian masyarakat Indonesia terkait keyword resesi ekonomi dan inflasi Indonesia meningkat secara pesat. Hal ini menunjukkan bahwa masyarakat Indonesia menaruh perhatian besar terhadap keadaan ekonomi kedepannya. Ancaman nyata akan terjadinya resesi ekonomi di tahun 2023 yang banyak diberitakan oleh media, keadaan ekonomi yang belum stabil pasca pandemi Covid-19 dan kenaikan harga komoditi energi dunia pasca pecahnya perang Rusia-Ukraina, mungkin saja menjadi hal yang mendorong masyarakat Indonesia menaruh perhatian besar terhadap keadaan ekonomi kedepannya.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Keadaan ekonomi kedepannya tentu dapat diukur dan digambarkan berdasarkan keadaan ekonomi saat ini. Tingkat inflasi menjadi salah satu hal utama yang bisa menggambarkan keadaan tersebut. Lalu bagaimanakah keadaan tingkat inflasi dunia dan Indonesia saat ini?</div>', unsafe_allow_html=True)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Tingkat Inflasi Dunia'], 
                         name='Tingkat Inflasi Dunia', mode='lines+markers'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Tingkat Inflasi Indonesia'], 
                         name='Tingkat Inflasi Indonesia', mode='lines+markers'))
fig.update_layout(autosize=False, width=1250, height=550, 
                  title='Tingkat Inflasi Dunia dan Indonesia', 
                  xaxis_title='Date', 
                  yaxis_title='Tingkat Inflasi')
st.plotly_chart(fig)

col1, col2, col3 = st.columns(3)
col1.metric('Year-on-year Growth', 'Tingkat Inflasi Dunia', '5,20%')
col2.write('')
col3.metric('Year-on-year Growth', 'Tingkat Inflasi Indonesia', '4,35%')

st.markdown('<div style="text-align: justify;">Grafik menggambarkan peningkatan yang cukup signifikan pada tingkat inflasi dunia dan Indonesia pasca pecahnya perang Rusia-Ukraina. Sejak November 2019 tingkat inflasi Indonesia berada dibawah rata-rata tingkat inflasi dunia dengan laju tingkat inflasi yang berlawanan arah. Pada masa pandemi Covid-19 terhitung per bulan Maret 2020 hingga Agustus 2021 tingkat inflasi dunia dan Indonesia berada dibawah 5% dengan laju peningkatan tingkat inflasi yang lambat. Pecahnya perang Rusia-Ukraina per 24 Februari 2022 menyebabkan laju tingkat inflasi dunia dan Indonesia kembali searah, dengan sama-sama mengalami peningkatan yang cukup signifikan dalam 1 hingga 2 bulan setelahnya. Dapat disimpulkan bahwa keadaan ekonomi dunia sudah mempengaruhi keadaan ekonomi di Indonesia, secara year-on-year sama-sama mengalami peningkatan dengan peningkatan masing-masing 5,20% untuk tingkat inflasi dunia dan 4,35% untuk tingkat inflasi Indonesia. Jika keadaan ekonomi dunia memburuk, maka keadaan ekonomi Indonesia pun akan ikut memburuk.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Tingkat inflasi yang meningkat tentu saja bisa dirasakan langsung dari kenaikan harga. Sejauh apa kenaikan harga yang dialami Indonesia dengan peningkatan tingkat inflasi year-on-year sebesar 4,35%?</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Kenaikan harga akan dilihat dari dua pembagian komoditi, yaitu komoditi pangan dan komoditi energi. Komoditi pangan dilihat berdasarkan sembilan macam harga bahan pokok dasar yang ada dipasar seperti beras, daging ayam, telur ayam, bawang merah, bawang putih, cabai merah, cabai rawit, minyak goreng, dan gula pasir. Sedangkan dari komoditi energi dilihat berdasarkan lima macam Bahan Bakar Minyak (BBM) seperti pertalite, pertamax, pertamax turbo, dexlite, dan pertamina dex. Semua komoditi dipilih berdasarkan pertimbangan komoditi yang bersentuhan langsung dengan masyarakat secara umum dan keterbatasan sumber data yang ada.</div>', unsafe_allow_html=True)

url2 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_pangan_202210240904.csv'
df_pangan = pd.read_csv(url2)
col1, col2 = st.columns(2)

fig_pangan_bar = go.Figure(go.Bar(
            x=df_pangan['YoY Growth (%)'],
            y=df_pangan['Komoditi Pangan'],
            orientation='h'))
fig_pangan_bar.update_layout( 
                  title='YoY Growth Komoditi Pangan', 
                  xaxis_title='Year-on-year Growth (%)', 
                  yaxis_title='Komoditi Pangan')
col1.plotly_chart(fig_pangan_bar)

fig_pangan_line = go.Figure()
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Cabai Merah'], 
                         name='Cabai Merah', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Cabai Rawit'], 
                         name='Cabai Rawit', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Telur Ayam'], 
                         name='Telur Ayam', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Bawang Merah'], 
                         name='Bawang Merah', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Minyak Goreng'], 
                         name='Minyak Goreng', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Gula Pasir'], 
                         name='Gula Pasir', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Beras'], 
                         name='Beras', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Daging Ayam'], 
                         name='Daging Ayam', mode='lines'))
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Bawang Putih'], 
                         name='Bawang Putih', mode='lines'))
fig_pangan_line.update_layout(
                  title='Pergerakan Harga Komoditi Pangan', 
                  xaxis_title='Date', 
                  yaxis_title='Komoditi Pangan')
col2.plotly_chart(fig_pangan_line)

st.markdown('<div style="text-align: justify;">Secara year-on-year growth komoditi pangan mengalami kenaikan yang signifikan pada beberapa harga bahan pokok. Sedangkan grafik pergerakan harga komoditi pangan menunjukkan adanya faktor lain yang mempengaruhi keadaan harga bahan pokok selain meningkatnya tingkat inflasi Indonesia. Hal ini dapat dilihat dengan seringnya terjadi lonjakan harga bahan pokok sebelum pecahnya perang Rusia-Ukraina per 24 Februari 2022 yang menjadi tolak ukur penyebab meningkatnya tingkat inflasi Indonesia saat ini. Tetapi dari tingkat penurunan antara lonjakan harga pasca pecahnya perang, terlihat kenaikan pada harga dasar bahan pokok yang menunjukkan tingkat inflasi Indonesia saat ini telah mempengaruhi kenaikan harga komoditi pangan.</div>', unsafe_allow_html=True)

url3 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_energi_202210180818.csv'
df_energi = pd.read_csv(url3)
col1, col2 = st.columns(2)

fig_energi_bar = go.Figure(go.Bar(
            x=df_energi['YoY Growth (%)'],
            y=df_energi['Komoditi Energi'],
            orientation='h'))
fig_energi_bar.update_layout( 
                  title='YoY Growth Komoditi Energi', 
                  xaxis_title='Year-on-year Growth (%)', 
                  yaxis_title='Komoditi Energi')
col1.plotly_chart(fig_energi_bar)

fig_energi_line = go.Figure()
fig_energi_line.add_trace(go.Scatter(x=df['Date'], y=df['Dexlite'], 
                         name='Dexlite', mode='lines'))
fig_energi_line.add_trace(go.Scatter(x=df['Date'], y=df['Pertamax'], 
                         name='Pertamax', mode='lines'))
fig_energi_line.add_trace(go.Scatter(x=df['Date'], y=df['Pertamina Dex'], 
                         name='Pertamina Dex', mode='lines'))
fig_energi_line.add_trace(go.Scatter(x=df['Date'], y=df['Pertalite'], 
                         name='Pertalite', mode='lines'))
fig_energi_line.add_trace(go.Scatter(x=df['Date'], y=df['Pertamax Turbo'], 
                         name='Pertamax Turbo', mode='lines'))
fig_energi_line.update_layout(
                  title='Pergerakan Harga Komoditi Energi', 
                  xaxis_title='Date', 
                  yaxis_title='Komoditi Energi')
col2.plotly_chart(fig_energi_line)

st.markdown('<div style="text-align: justify;">Secara year-on-year growth komoditi energi secara keseluruhan telah mengalami kenaikan harga. Grafik pergerakan harga komoditi energi menunjukkan enam bulan pasca pecahnya perang, tepatnya per bulan September 2022 terjadi kenaikan harga BBM dimana pada bulan tersebut tingkat inflasi Indonesia berada pada angka 5,95%. Hal ini menunjukkan bahwa tingkat inflasi Indonesia telah mempengaruhi kenaikan harga BBM di indonesia.</div>', unsafe_allow_html=True)

url4 = 'https://raw.githubusercontent.com/rvoktrzl/tetris/main/data/cp_inflasi_komoditi_202210180818.csv'
df_komoditi = pd.read_csv(url4)
col1, col2, col3 = st.columns(3)

col1.write('')
fig_komoditi_bar = go.Figure(go.Bar(
            x=df_komoditi['YoY Growth (%)'],
            y=df_komoditi['Komoditi'],
            orientation='h'))
fig_komoditi_bar.update_layout(
                  title='YoY Growth Komoditi Pangan VS Komoditi Energi', 
                  xaxis_title='Year-on-year Growth (%)', 
                  yaxis_title='Komoditi')
col2.plotly_chart(fig_komoditi_bar)

col3.write('')

st.markdown('<div style="text-align: justify;">Secara keseluruhan dengan kenaikan year-on-year tingkat inflasi sebesar 4,35%, grafik menunjukkan kenaikan harga komoditi energi lebih tinggi daripada komoditi pangan, dimana masing-masing kenaikan harga mencapai 51% untuk komoditi energi dibandingkan tahun lalu dan 25% untuk komoditi pangan dibandingkan tahun lalu. Hal ini menunjukkan bahwa pecahnya perang Rusia-Ukraina benar-benar berpengaruh signifikan terhadap komoditi energi dunia dan mendorong meningkatnya tingkat inflasi dunia. Kenaikan harga komoditi energi akan menjadi rentetan panjang yang mendorong kenaikan harga komoditi-komoditi lainnya, yang mana hal inilah yang akan memperburuk keadaan ekonomi kedepannya.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Tingkat inflasi dunia per bulan September 2022 telah mengalami peningkatan year-on-year sebesar 5,20% dan mendorong peningkatan tingkat inflasi Indonesia year-on-year sebesar 4,35%. Dimana masing-masing tingkat inflasi dunia dan tingkat inflasi Indonesia saat ini berada pada angka 10,30% dan 5,95%. Salah satu dampak peningkatan tingkat inflasi ini adalah mendorong terjadinya kenaikan harga yang cukup signifikan pada komoditi energi. Jika hal ini terus berlanjut, tentu akan memperburuk keadaan ekonomi kedepannya dan berdampak pada aspek-aspek dalam lingkup ekonomi lainnya yang tidak diukur dalam analisis ini. Untuk itu kita harus bisa menentukan sikap dalam mengatur bagaimana bertahan dalam keadaan ekonomi tersebut. Dimulai dengan mengatur pengeluaran dan simpanan uang, mengatur investasi dan aset yang mungkin terdampak, serta mengatur pembayaran hutang atau cicilan.</div>', unsafe_allow_html=True)

st.caption('Sumber Data: https://trends.google.com/trends/explore?geo=ID&q=Resesi%20ekonomi,Inflasi%20dunia,inflasi%20indonesia, https://www.statista.com/statistics/1317738/global-inflation-ratemonthly/#:~:text=CPI%20inflation%20rate%20worldwide%202019%2D2022&text=In%20March%202022%2C%20the%20global,7.47%20percent%20in%20February%202022, https://www.bi.go.id/id/statistik/indikator/data-inflasi.aspx, https://hargapangan.id/tabel-harga/pedagang-besar/daerah, https://bisnis.tempo.co/read/1630292/inilah-rincian-kenaikan-harga-bbm-pertamina-5-tahun-terakhir, https://industri.kontan.co.id/news/berikut-daftar-harga-bbm-terbaru-pertamina-pasca-kenaikan-harga-bbm')
