# Unigram can run from Telegram.exe, so NVDA may request the "telegram" app
# module. The imported AppModule checks product metadata before enabling
# UnigramPlus so Telegram Desktop add-ons can coexist.
from .unigram import *
