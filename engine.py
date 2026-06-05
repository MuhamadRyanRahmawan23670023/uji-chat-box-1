import random
from FSM import (FSM,
    STATE_GREET, STATE_GEMPA, STATE_BANJIR, STATE_TSUNAMI,
    STATE_KEBAKARAN, STATE_GUNUNG_API, STATE_EVAKUASI,
    STATE_PERTOLONGAN, STATE_LOGISTIK, STATE_PSIKOSOSIAL,
    STATE_PASCA_BENCANA, STATE_FAREWELL, STATE_UNKNOWN)

RESPONSES = {
    STATE_GREET: [
        "Halo! Saya SIGAB — Sistem Informasi Cepat Tanggap Bencana. 🚨\nSilakan tanyakan informasi seputar bencana alam, evakuasi, atau pertolongan pertama.",
        "Hai! Saya siap membantu kamu menghadapi situasi darurat bencana. Apa yang ingin kamu ketahui?",
    ],
    STATE_GEMPA: [
        "🌍 **Gempa Bumi — Tindakan Darurat:**\n"
        "- **Saat gempa:** Berlindung di bawah meja kokoh, lindungi kepala, jauhi jendela.\n"
        "- **Setelah gempa:** Segera keluar gedung, waspada gempa susulan.\n"
        "- **Jangan gunakan lift.** Gunakan tangga darurat.\n"
        "- Pantau informasi resmi dari **BMKG (bmkg.go.id)**.",

        "🌍 **Mitigasi Gempa Bumi:**\n"
        "- Kenali titik kumpul di lingkunganmu.\n"
        "- Pastikan lemari dan furnitur berat terpasang ke dinding.\n"
        "- Siapkan tas siaga berisi: air minum, P3K, senter, dokumen penting.",
    ],
    STATE_BANJIR: [
        "🌊 **Banjir — Tindakan Darurat:**\n"
        "- Segera pindah ke lantai yang lebih tinggi.\n"
        "- Matikan listrik dari panel utama jika air mulai masuk rumah.\n"
        "- Jangan berjalan di air banjir — bisa ada arus deras atau lubang tersembunyi.\n"
        "- Hubungi BPBD setempat untuk bantuan evakuasi.",

        "🌊 **Kesiapsiagaan Banjir:**\n"
        "- Pantau curah hujan dan status sungai terdekat.\n"
        "- Siapkan sandbag/karung pasir untuk menahan air masuk.\n"
        "- Simpan dokumen penting dalam wadah kedap air.",
    ],
    STATE_TSUNAMI: [
        "🌊 **TSUNAMI — TINDAKAN SEGERA:**\n"
        "- ⚠️ Jika merasakan gempa kuat di dekat pantai — **LANGSUNG LARI KE DATARAN TINGGI!**\n"
        "- Jangan tunggu peringatan resmi, setiap detik sangat berharga.\n"
        "- Jauhi pantai minimal **radius 500 meter** atau naik ke ketinggian **>20 meter dpl**.\n"
        "- Jangan kembali ke pantai sebelum ada pernyataan aman dari BMKG.",

        "🌊 **Tanda-tanda Tsunami:**\n"
        "- Air laut surut drastis dan tiba-tiba.\n"
        "- Terdengar suara gemuruh dari arah laut.\n"
        "- Gempa bumi kuat di dekat pantai.\n"
        "- **Jika melihat tanda ini → EVAKUASI SEGERA!**",
    ],
    STATE_KEBAKARAN: [
        "🔥 **Kebakaran — Tindakan Darurat:**\n"
        "- Berteriak 'KEBAKARAN!' untuk memperingatkan orang lain, aktifkan alarm.\n"
        "- Hubungi **Damkar: 113** atau **119**.\n"
        "- Tutup mulut & hidung dengan kain basah, merangkak di bawah asap.\n"
        "- Jangan buka pintu yang terasa panas — api ada di baliknya.\n"
        "- Gunakan tangga darurat, **JANGAN gunakan lift.**",

        "🔥 **Kebakaran Hutan:**\n"
        "- Pantau arah angin — angin membawa api.\n"
        "- Buat sekat bakar/firebreak jika memungkinkan.\n"
        "- Evakuasi warga dalam radius 2 km dari titik api.\n"
        "- Gunakan masker N95 untuk perlindungan dari asap.",
    ],
    STATE_GUNUNG_API: [
        "🌋 **Erupsi Gunung Api — Tindakan Darurat:**\n"
        "- Pantau status gunung dari **PVMBG (vsi.esdm.go.id)**.\n"
        "- Status **AWAS (Level 4)** → evakuasi segera dari radius bahaya.\n"
        "- Gunakan masker dan kacamata untuk lindungi diri dari abu vulkanik.\n"
        "- Tutup sumber air dan makanan agar tidak terkontaminasi abu.",

        "🌋 **Radius Bahaya Erupsi:**\n"
        "- Level WASPADA: radius 2-3 km dikosongkan.\n"
        "- Level SIAGA: radius 5-6 km dikosongkan.\n"
        "- Level AWAS: radius 8-10 km atau lebih dikosongkan.\n"
        "- Ikuti arahan resmi BNPB dan Pemda setempat.",
    ],
    STATE_EVAKUASI: [
        "🚶 **Prosedur Evakuasi:**\n"
        "- Ikuti **jalur evakuasi** yang telah ditandai (rambu hijau).\n"
        "- Menuju **titik kumpul** terdekat — biasanya lapangan atau area terbuka.\n"
        "- Bantu lansia, anak-anak, dan penyandang disabilitas.\n"
        "- Bawa tas siaga: dokumen, obat, air minum, makanan untuk 3 hari.\n"
        "- **Jangan kembali** ke rumah sebelum dinyatakan aman.",

        "🚶 **Manajemen Pengungsian:**\n"
        "- Daftarkan diri ke posko pengungsian untuk pendataan.\n"
        "- Prioritaskan kelompok rentan: ibu hamil, bayi, lansia, difabel.\n"
        "- Jaga kebersihan dan sanitasi di tempat pengungsian.\n"
        "- Koordinasikan kebutuhan dengan petugas BPBD.",
    ],
    STATE_PERTOLONGAN: [
        "🩹 **Pertolongan Pertama Darurat Bencana:**\n"
        "- **Pendarahan:** Tekan luka dengan kain bersih selama 10-15 menit.\n"
        "- **Patah tulang:** Imobilisasi dengan bidai, jangan paksa diluruskan.\n"
        "- **Pingsan:** Baringkan, angkat kaki, jaga jalan napas tetap terbuka.\n"
        "- **Luka bakar:** Siram air mengalir 20 menit, jangan gunakan pasta gigi/odol.",

        "🩹 **Prioritas Korban (Triase):**\n"
        "- 🔴 **Merah (Prioritas 1):** Kondisi kritis, butuh penanganan segera.\n"
        "- 🟡 **Kuning (Prioritas 2):** Luka serius tapi stabil, bisa menunggu.\n"
        "- 🟢 **Hijau (Prioritas 3):** Luka ringan, bisa berjalan sendiri.\n"
        "- ⚫ **Hitam:** Meninggal dunia atau tidak ada harapan.\n"
        "- Segera hubungi **119** untuk ambulans.",
    ],
    STATE_LOGISTIK: [
        "📦 **Manajemen Logistik Bencana:**\n"
        "- Kebutuhan dasar: air bersih (2L/orang/hari), makanan siap saji, selimut.\n"
        "- Distribusi logistik koordinasikan melalui posko utama BNPB/BPBD.\n"
        "- Prioritaskan kelompok rentan dalam distribusi bantuan.\n"
        "- Catat semua bantuan masuk dan keluar untuk akuntabilitas.",

        "📦 **Tas Siaga Bencana — Isi Wajib:**\n"
        "- 💧 Air minum 3 liter\n"
        "- 🍱 Makanan darurat (roti, biskuit) untuk 3 hari\n"
        "- 🩹 Kotak P3K lengkap\n"
        "- 🔦 Senter + baterai cadangan\n"
        "- 📄 Fotokopi dokumen penting (KTP, KK, akta)\n"
        "- 📱 Power bank dan peluit darurat",
    ],
    STATE_PSIKOSOSIAL: [
        "🧠 **Dukungan Psikososial Pasca Bencana:**\n"
        "- Wajar merasa takut, sedih, atau marah setelah bencana — itu respons normal.\n"
        "- **Psychological First Aid (PFA):** Dengarkan tanpa menghakimi, berikan rasa aman.\n"
        "- Jaga rutinitas harian untuk membantu pemulihan mental.\n"
        "- Hubungi **hotline kesehatan jiwa: 119 ext 8** jika butuh bantuan.",

        "🧠 **Tanda Trauma Serius (Butuh Bantuan Profesional):**\n"
        "- Mimpi buruk berulang tentang kejadian bencana.\n"
        "- Menghindari tempat/situasi yang mengingatkan pada bencana.\n"
        "- Sulit tidur, mudah kaget, selalu waspada berlebihan.\n"
        "- Tidak mau makan atau berinteraksi selama >2 minggu.\n"
        "- → Segera konsultasi ke psikolog/psikiater di posko kesehatan.",
    ],
    STATE_PASCA_BENCANA: [
        "🏗️ **Tahap Pemulihan Pasca Bencana:**\n"
        "- **Jangka pendek (0-3 bulan):** Pembersihan puing, perbaikan darurat, santunan.\n"
        "- **Jangka menengah (3-12 bulan):** Rekonstruksi hunian sementara, pemulihan layanan dasar.\n"
        "- **Jangka panjang (>1 tahun):** Rekonstruksi permanen, pemulihan ekonomi, mitigasi ulang.\n"
        "- Pantau program bantuan resmi di **bnpb.go.id**.",

        "🏗️ **Rehabilitasi & Rekonstruksi:**\n"
        "- Bangun kembali dengan standar tahan bencana (rumah tahan gempa, dll).\n"
        "- Libatkan masyarakat dalam perencanaan rekonstruksi.\n"
        "- Dokumentasikan kerugian untuk klaim bantuan pemerintah.\n"
        "- Ikuti pelatihan kesiapsiagaan agar lebih siap di masa depan.",
    ],
    STATE_FAREWELL: [
        "Terima kasih telah menggunakan SIGAB. Tetap waspada dan jaga keselamatan! 🙏\nDalam keadaan darurat hubungi: **BNPB 117** | **Damkar 113** | **Ambulans 119**",
        "Semoga informasi ini bermanfaat. Ingat: **Siaga sebelum bencana!** 🚨\nKontak darurat: **BNPB 117** | **Basarnas 115** | **PLN 123**",
    ],
    STATE_UNKNOWN: [
        "Maaf, saya kurang memahami pertanyaan tersebut. 🤔\nSaya dapat membantu tentang:\n- Gempa bumi, Banjir, Tsunami\n- Kebakaran, Erupsi Gunung Api\n- Evakuasi, Pertolongan Pertama\n- Logistik, Psikososial, Pemulihan",
        "Coba tanyakan dengan kata kunci seperti:\n**gempa, banjir, tsunami, kebakaran, gunung, evakuasi, pertolongan, logistik, trauma, pemulihan**",
    ],
}

class ChatEngine:
    def __init__(self):
        self.fsm = FSM()

    def get_response(self, user_input: str) -> str:
        state = self.fsm.transition(user_input)
        return random.choice(RESPONSES[state])

    def reset(self):
        self.fsm = FSM()
