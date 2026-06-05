import re

# ── STATES ──────────────────────────────────────────────────────────────────
STATE_GREET         = "GREET"
STATE_GEMPA         = "GEMPA"
STATE_BANJIR        = "BANJIR"
STATE_TSUNAMI       = "TSUNAMI"
STATE_KEBAKARAN     = "KEBAKARAN"
STATE_GUNUNG_API    = "GUNUNG_API"
STATE_EVAKUASI      = "EVAKUASI"
STATE_PERTOLONGAN   = "PERTOLONGAN_PERTAMA"
STATE_LOGISTIK      = "LOGISTIK"
STATE_PSIKOSOSIAL   = "PSIKOSOSIAL"
STATE_PASCA_BENCANA = "PASCA_BENCANA"
STATE_FAREWELL      = "FAREWELL"
STATE_UNKNOWN       = "UNKNOWN"

# ── POLA REGEX ───────────────────────────────────────────────────────────────
PATTERNS = [
    (STATE_GREET,         r"\b(halo|hai|hi|hello|selamat|mulai|start)\b"),
    (STATE_GEMPA,         r"\b(gempa|earthquake|guncangan|richter|seismik|gempa bumi)\b"),
    (STATE_BANJIR,        r"\b(banjir|banjir bandang|genangan|luapan|flood)\b"),
    (STATE_TSUNAMI,       r"\b(tsunami|gelombang besar|ombak raksasa|tidal wave)\b"),
    (STATE_KEBAKARAN,     r"\b(kebakaran|api|terbakar|asap tebal|fire|kebakaran hutan)\b"),
    (STATE_GUNUNG_API,    r"\b(gunung|erupsi|lava|abu vulkanik|letusan|vulkanik)\b"),
    (STATE_EVAKUASI,      r"\b(evakuasi|mengungsi|jalur evakuasi|titik kumpul|shelter|pengungsian)\b"),
    (STATE_PERTOLONGAN,   r"\b(pertolongan pertama|p3k|luka|pingsan|patah tulang|pendarahan|first aid)\b"),
    (STATE_LOGISTIK,      r"\b(logistik|bantuan|makanan|air bersih|obat|tenda|pasokan|distribusi)\b"),
    (STATE_PSIKOSOSIAL,   r"\b(trauma|stress|psikologi|mental|ketakutan|panik|trauma healing|psikososial)\b"),
    (STATE_PASCA_BENCANA, r"\b(pasca|pemulihan|rekonstruksi|rehabilitasi|recovery|bangkit kembali)\b"),
    (STATE_FAREWELL,      r"\b(bye|dadah|keluar|selesai|terima kasih|makasih|sampai jumpa)\b"),
]

def detect_intent(text: str) -> str:
    text = text.lower()
    for state, pattern in PATTERNS:
        if re.search(pattern, text):
            return state
    return STATE_UNKNOWN

class FSM:
    def __init__(self):
        self.state = STATE_GREET
        self.prev_state = None

    def transition(self, user_input: str) -> str:
        self.prev_state = self.state
        intent = detect_intent(user_input)
        self.state = intent
        return self.state
