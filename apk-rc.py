import streamlit as st
import pickle
import numpy as np

# Load model files
with open('scaler_model.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('pca_model.pkl', 'rb') as pca_file:
    pca = pickle.load(pca_file)

with open('rc_model.pkl', 'rb') as rc_file:
    ridge_classifier = pickle.load(rc_file)

# Streamlit app
st.title('Klasifikasi Tingkat Tumor Otak')

# Input form for new data
st.write('Klasifikasi Tingkat Tumor Otak ini akan menghasilkan dua kelas, yaitu Tumor Otak Ganas dan Tumor Otak Jinak. Proses klasifikasi ini melibatkan kriteria umum dan mutasi genetik. Tujuan utamanya adalah menghimpun kriteria umum dan kriteria mutasi genetik untuk meningkatkan kinerja prediksi dan mengurangi biaya yang diperlukan.')
st.write('Form pengisian dibawah ini memiliki 23 kriteria yang harus diisi yaitu : 3 kriteria umum (gender, usia, dan ras) dan 20 kriteria mutasi genetik (20 kriteria mutasi genetik didapat saat pasien telah melalui tes genetik molekuler).')
st.write('Sebelum mengisi form dibawah, diharapkan anda telah membaca deskripsi data yang harus diisikan pada setiap form, agar aplikasi dapat melakukan prediksi dengan optimal.')
# Create a button to trigger the modal
button_clicked = st.button('Baca Deskripsi Data Disini')

# Check if the button is clicked
if button_clicked:
    # Display modal content using markdown
    st.write('1. Jenis Kelamin : terdapat 2 pilihan untuk mengisi form ini, yaitu Pria/Wanita.')
    st.write('2. Usia saat di diagnosa : isikan dengan tipe angka sesuai umur pasien saat ini.')
    st.write('3. Ras : isikan sesuai jenis kulit pasien. Terdapat 4 pilihan untuk mengisi form ini, yaitu Kulit Putih, Kulit Hitam, Asia, & Alaska.')
    st.write('4. Mutasi Isocitrate Dehydrogenase : Isocitrate Dehydrogenase (IDH) merupakan enzim dalam siklus asam sitrat yang terlibat dalam konversi isositrat menjadi alfa-ketoglutarat, menghasilkan NADH. Mutasi pada gen IDH, terutama IDH1 dan IDH2, telah terkait dengan beberapa jenis kanker, seperti glioma otak. Mutasi ini menghasilkan oncometabolit 2-hydroxyglutarate, yang dapat memodulasi proses epigenetik dan menyebabkan perubahan kanker. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('5. Mutasi Tumor Protein : Dalam konteks onkologi, mutasi p53 sering dihubungkan dengan perjalanan kanker yang agresif dan resistensi terhadap berbagai bentuk terapi. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('6. Mutasi ATRX Chromatin Remodeler : Mutasi dalam gen ATRX bisa membuat tumor tumbuh dengan cara mengubah cara kerja gen tertentu dan sifat sel, memainkan peran dalam perkembangan kanker dan pertumbuhan sel ganas. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('7. Mutasi Phosphatase and Tensin Homolog : Mutasi pada Phosphatase and Tensin Homolog (PTEN) adalah perubahan dalam gen yang dapat memengaruhi pertumbuhan sel dan menghubungkan dengan risiko pengembangan kanker. Mutasi dalam gen ini dapat menyebabkan kehilangan fungsi normalnya, memungkinkan sel untuk berkembang dengan cepat dan tanpa kendali. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('8. Mutasi Epidermal Growth Factor Receptor : EGFR adalah protein yang berperan dalam mengatur pertumbuhan dan pembelahan sel. Mutasi dalam gen ini dapat mengubah normalitas kontrol pertumbuhan sel, menyebabkan sel-sel tumbuh lebih cepat dan menjadi lebih rentan terhadap pembentukan tumor. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('9. Mutasi Capicua Transcriptional Repressor : CIC berperan dalam mengendalikan ekspresi gen dengan cara menekan aktivitas transkripsi atau pembentukan RNA dari gen-gen tertentu. Mutasi dalam gen CIC dapat mengakibatkan kehilangan fungsi normalnya, yang dapat menyebabkan gangguan dalam kontrol genetik seluler. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('10. Mutasi Mucin 16, Cell Surface Associated : Mutasi pada Mucin 16, Cell Surface Associated (MUC16) adalah perubahan genetik yang terkait dengan perubahan pada protein ini yang terdapat di permukaan sel. MUC16 dikenal sebagai protein membran sel yang berpartisipasi dalam berbagai proses biologis, termasuk interaksi sel-sel dan respons imun. Mutasi dalam gen MUC16 dapat menyebabkan perubahan yang tidak normal pada struktur atau fungsi protein. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('11. Mutasi Phosphatidylinositol-4,5-bisphosphate 3-kinase Catalytic Subunit Alpha : Mutasi pada Phosphatidylinositol-4,5-bisphosphate 3-kinase Catalytic Subunit Alpha (PIK3CA) adalah perubahan genetik yang terjadi pada subunit katalitik protein ini. PIK3CA berperan dalam regulasi berbagai jalur sinyal seluler, termasuk yang terlibat dalam pertumbuhan sel dan proliferasi. Mutasi dalam gen PIK3CA dapat mengakibatkan aktivitas berlebihan dari protein ini, memicu pertumbuhan sel yang tidak terkontrol dan berkontribusi pada perkembangan kanker. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('12. Mutasi Neurofibromin 1 : Mutasi pada Neurofibromin 1 (NF1) adalah perubahan genetik yang terjadi pada gen NF1. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('13. Mutasi Phosphoinositide-3-kinase Regulatory Subunit 1 : Mutasi pada Phosphoinositide-3-kinase Regulatory Subunit 1 (PIK3R1) adalah perubahan genetik yang terjadi pada subunit pengatur protein phosphoinositide-3-kinase (PI3K). Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('14. Mutasi Far Upstream Element Binding Protein 1 :Mutasi pada Far Upstream Element Binding Protein 1 (FUBP1) adalah perubahan genetik yang terjadi pada gen FUBP1. FUBP1 berperan dalam mengatur ekspresi gen dan mempengaruhi proses pertumbuhan dan pembelahan sel. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('15. Mutasi RB Transcriptional Corepressor 1 : Mutasi RB Transcriptional Corepressor 1 (atau biasa disebut dengan mutasi dalam gen RB1) adalah perubahan atau kelainan pada materi genetik yang disebut RB Transcriptional Corepressor 1. Gen ini berperan dalam mengatur pertumbuhan sel dan mencegah terjadinya pertumbuhan sel yang tidak terkendali. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('16. Mutasi Notch Receptor 1 : Notch Receptor 1 adalah semacam "penyaring" atau "reseptor" di dalam sel tubuh kita. Mutasi Notch Receptor 1 berarti ada perubahan atau kesalahan dalam informasi genetik atau "kode" yang membentuk Notch Receptor 1 ini. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('17. Mutasi BCL6 Corepressor : Mutasi BCL6 Corepressor merupakan perubahan pada bagian gen yang terlibat dalam mengendalikan pertumbuhan sel B. Perubahan ini dapat mempengaruhi cara gen tersebut berfungsi, dan hal ini dapat memiliki dampak pada sistem kekebalan tubuh dan kesehatan secara keseluruhan. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('18. Mutasi CUB and Sushi Multiple Domains 3 : Merupakan mutasi pada gen tertentu dapat menyebabkan pertumbuhan sel yang tidak terkendali atau resistensi terhadap pengobatan. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('19. Mutasi SWI/SNF Related, Matrix Associated, Actin Dependent Regulator of Chromatin, Subfamily a, Member 4 : Merupakan mutasi atau perubahan dalam regulator ini dapat memengaruhi bagaimana sel glioma tumbuh dan berkembang. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('20. Mutasi Glutamate Ionotropic Receptor NMDA Type Subunit 2A : Mutasi ini dapat mengubah cara sel tumor di otak berkomunikasi satu sama lain melalui zat kimia tertentu, yaitu glutamat. Perubahan ini dapat memiliki konsekuensi dalam pertumbuhan dan perilaku sel glioma. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('21. Mutasi Isocitrate Dehydrogenase (NADP(+)) 2 : Mutasi ini dapat memengaruhi cara kerja enzim yang disebut Isocitrate Dehydrogenase 2. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('22. Mutasi FAT Atypical Cadherin 4 :  Merupakan perubahan pada gen tertentu yang disebut FAT Atypical Cadherin 4 yang terjadi dalam jenis tumor otak yang disebut glioma. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.write('23. Mutasi Platelet-Derived Growth Factor Receptor Alpha : Mutasi PDGFRA dalam glioma bisa dianggap sebagai "kesalahan" genetik yang membuat sel-sel otak berkembang dengan cara yang tidak normal. Terdapat 2 pilihan untuk mengisi form ini, yaitu Bermutasi/Tidak Bermutasi.')
    st.button('Tutup Deskripsi')  # Optionally, add a button to close the modal


gender = st.selectbox('Jenis Kelamin', ['Pria', 'Wanita'])
gender = 0 if gender == 'Pria' else 1

age = st.number_input('Usia saat di diagnosa', min_value=0, max_value=100)

race = st.selectbox('Ras', ['Kulit Putih', 'Kulit Hitam', 'Asia', 'Alaska'])
race = ['Kulit Putih', 'Kulit Hitam', 'Asia', 'Alaska'].index(race)

mutation_values = ['Tidak Bermutasi', 'Bermutasi']

idh1 = st.selectbox('Mutasi Isocitrate Dehydrogenase', mutation_values)
idh1 = 0 if idh1 == 'Tidak Bermutasi' else 1

tp53 = st.selectbox('Mutasi Tumor Protein', mutation_values)
tp53 = 0 if tp53 == 'Tidak Bermutasi' else 1

atrx = st.selectbox('Mutasi ATRX Chromatin Remodeler', mutation_values)
atrx = 0 if atrx == 'Tidak Bermutasi' else 1

pten = st.selectbox('Mutasi Phosphatase and Tensin Homolog', mutation_values)
pten = 0 if pten == 'Tidak Bermutasi' else 1

egfr = st.selectbox('Mutasi Epidermal Growth Factor Receptor', mutation_values)
egfr = 0 if egfr == 'Tidak Bermutasi' else 1

cic = st.selectbox('Mutasi Capicua Transcriptional Repressor', mutation_values)
cic = 0 if cic == 'Tidak Bermutasi' else 1

muc16 = st.selectbox('Mutasi Mucin 16, Cell Surface Associated', mutation_values)
muc16 = 0 if muc16 == 'Tidak Bermutasi' else 1

pik3ca = st.selectbox('Mutasi Phosphatidylinositol-4,5-bisphosphate 3-kinase Catalytic Subunit Alpha', mutation_values)
pik3ca = 0 if pik3ca == 'Tidak Bermutasi' else 1

nf1 = st.selectbox('Mutasi Neurofibromin 1', mutation_values)
nf1 = 0 if nf1 == 'Tidak Bermutasi' else 1

pik3r1 = st.selectbox('Mutasi Phosphoinositide-3-kinase Regulatory Subunit 1', mutation_values)
pik3r1 = 0 if pik3r1 == 'Tidak Bermutasi' else 1

fubp1 = st.selectbox('Mutasi Far Upstream Element Binding Protein 1', mutation_values)
fubp1 = 0 if fubp1 == 'Tidak Bermutasi' else 1

rb1 = st.selectbox('Mutasi RB Transcriptional Corepressor 1', mutation_values)
rb1 = 0 if rb1 == 'Tidak Bermutasi' else 1

notch1 = st.selectbox('Mutasi Notch Receptor 1', mutation_values)
notch1 = 0 if notch1 == 'Tidak Bermutasi' else 1

bcor = st.selectbox('Mutasi BCL6 Corepressor', mutation_values)
bcor = 0 if bcor == 'Tidak Bermutasi' else 1

csmd3 = st.selectbox('Mutasi CUB and Sushi Multiple Domains 3', mutation_values)
csmd3 = 0 if csmd3 == 'Tidak Bermutasi' else 1

smarca4 = st.selectbox('Mutasi SWI/SNF Related, Matrix Associated, Actin Dependent Regulator of Chromatin, Subfamily a, Member 4', mutation_values)
smarca4 = 0 if smarca4 == 'Tidak Bermutasi' else 1

grin2a = st.selectbox('Mutasi Glutamate Ionotropic Receptor NMDA Type Subunit 2A', mutation_values)
grin2a = 0 if grin2a == 'Tidak Bermutasi' else 1

idh2 = st.selectbox('Mutasi Isocitrate Dehydrogenase (NADP(+)) 2', mutation_values)
idh2 = 0 if idh2 == 'Tidak Bermutasi' else 1

fat4 = st.selectbox('Mutasi FAT Atypical Cadherin 4', mutation_values)
fat4 = 0 if fat4 == 'Tidak Bermutasi' else 1

pdgfra = st.selectbox('Mutasi Platelet-Derived Growth Factor Receptor Alpha', mutation_values)
pdgfra = 0 if pdgfra == 'Tidak Bermutasi' else 1

if st.button('Prediksi Tingkat Tumor'):
    # Preprocess the input data
    new_data = np.array([gender, age, race, idh1, tp53, atrx, pten, egfr, cic, muc16, pik3ca, nf1, pik3r1, fubp1, rb1, notch1, bcor, csmd3, smarca4, grin2a, idh2, fat4, pdgfra]).reshape(1, -1)
    new_data = scaler.transform(new_data)
    new_data = pca.transform(new_data)

    # Make a prediction
    prediction = ridge_classifier.predict(new_data)

    if prediction == 0:
        st.write('Hasil Prediksi: Tumor Otak Jinak')
    else:
        st.write('Hasil Prediksi: Tumor Otak Ganas')
