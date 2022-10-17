import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('Capstone Project - Inflasi.xlsx')
st.set_page_config(layout='wide')

st.image('istockphoto-1180481421-612x612.jpg', width=1250)

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

st.markdown('<div style="text-align: justify;">Grafik menggambarkan peningkatan yang cukup signifikan pada tingkat inflasi dunia dan Indonesia pasca pecahnya perang Rusia-Ukraina per 24 Februari 2022. Keadaan ekonomi dunia pun telah mempengaruhi keadaan ekonomi Indonesia saat ini. Jika keadaan ekonomi dunia memburuk, maka keadaan ekonomi Indonesia pun akan ikut memburuk.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Tingkat inflasi yang meningkat tentu saja bisa dirasakan langsung dari kenaikan harga. Sejauh apa kenaikan harga yang dialami Indonesia dengan peningkatan tingkat inflasi year-on sebesar 4,35%?</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Kenaikan harga akan dilihat dari dua pembagian komoditi, yaitu komoditi pangan dan komoditi energi. Komoditi pangan dilihat berdasarkan sepuluh macam harga bahan pokok dasar yang ada dipasar seperti beras, daging ayam, daging sapi, telur ayam, bawang merah, bawang putih, cabai merah, cabai rawit, minyak goreng, dan gula pasir. Sedangkan dari komoditi energi dilihat berdasarkan lima macam Bahan Bakar Minyak (BBM) seperti pertalite, pertamax, pertamax turbo, dexlite, dan pertamina dex. Semua komoditi dipilih berdasarkan pertimbangan komoditi yang bersentuhan langsung dengan masyarakat secara umum dan keterbatasan sumber data yang ada.</div>', unsafe_allow_html=True)

df_pangan = pd.read_excel('cp_inflasi_komoditi_pangan.xlsx')
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
fig_pangan_line.add_trace(go.Scatter(x=df['Date'], y=df['Daging Sapi'], 
                         name='Daging Sapi', mode='lines'))
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

st.markdown('<div style="text-align: justify;">Secara year-on-year growth komoditi pangan mengalami kenaikan yang signifikan pada beberapa harga bahan pokok. Sedangkan grafik pergerakan harga komoditi pangan menunjukkan adanya faktor lain yang mempengaruhi keadaan harga bahan pokok selain meningkatnya tingkat inflasi Indonesia. Hal ini dapat dilihat dengan seringnya terjadi lonjakan harga bahan pokok sebelum pecahnya perang Rusia-Ukraina yang menjadi tolak ukur penyebab meningkatnya tingkat inflasi Indonesia saat ini. Tetapi dari tingkat penurunan antara lonjakan harga pasca pecahnya perang, terlihat kenaikan pada harga dasar bahan pokok yang menunjukkan tingkat inflasi Indonesia saat ini telah mempengaruhi kenaikan harga komoditi pangan.</div>', unsafe_allow_html=True)

df_energi = pd.read_excel('cp_inflasi_komoditi_energi.xlsx')
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

df_komoditi = pd.read_excel('cp_inflasi_komoditi.xlsx')
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
st.markdown('<div style="text-align: justify;">Peningkatan tingkat inflasi yang berkelanjutan menjadi salah satu faktor yang mempengaruhi pertumbuhan ekonomi suatu negara. Pertumbuhan ekonomi yang bernilai negatif mengakibatkan penurunan Produk Domestik Bruto (PDB). Penurunan pada PDB menunjukkan bahwa tingkat produksi dalam negeri menurun karena adanya sebagian atau keseluruhan produsen mengalami kesulitan dalam melakukan proses produksi. Penurunan tingkat produksi disebabkan oleh meningkatnya tingkat inflasi yang mendorong kenaikan harga bahan baku, dimana hal ini menjadi penyebab meningkatnya tingkat pengangguran akibat adanya Pemutusan Hubungan Kerja (PHK). Jika keadaan ekonomi ini terjadi selama dua kuartal berturut-turut, hal inilah yang disebut dengan resesi ekonomi.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Melihat bagaimana tingkat inflasi dan kenaikan harga yang terjadi saat ini, dapat disimpulkan adanya kemungkinan keadaan ekonomi akan semakin memburuk kedepannya yang menandakan terjadinya resesi ekonomi. Jika resesi terjadi banyak aspek-aspek dalam lingkup ekonomi yang akan terdampak. Untuk itu kita harus bisa menentukan sikap dalam mengatur bagaimana bertahan dalam keadaan ekonomi disaat resesi yang mungkin saja terjadi dalam kurun waktu yang lama. Dimulai dengan mengatur pengeluaran dan simpanan uang, mengatur investasi dan aset yang mungkin saja terdampak, serta mengatur pembayaran hutang dan cicilan. Hal ini dilakukan karena suku bunga akan mengalami peningkatan sebagai salah satu bentuk kebijakan moneter Pemerintah untuk mengendalikan keadaan ekonomi di saat resesi terjadi.</div>', unsafe_allow_html=True)
st.caption('Sumber Data: https://trends.google.com/trends/explore?geo=ID&q=Resesi%20ekonomi,Inflasi%20dunia,inflasi%20indonesia, https://www.statista.com/statistics/1317738/global-inflation-ratemonthly/#:~:text=CPI%20inflation%20rate%20worldwide%202019%2D2022&text=In%20March%202022%2C%20the%20global,7.47%20percent%20in%20February%202022, https://www.bi.go.id/id/statistik/indikator/data-inflasi.aspx, https://hargapangan.id/tabel-harga/pedagang-besar/daerah, https://bisnis.tempo.co/read/1630292/inilah-rincian-kenaikan-harga-bbm-pertamina-5-tahun-terakhir, https://industri.kontan.co.id/news/berikut-daftar-harga-bbm-terbaru-pertamina-pasca-kenaikan-harga-bbm')