# Copyright (c) 2021 Itz-fork
# Part of: Nexa-Userbot

import os

class Config(object):
    APP_ID = os.environ.get("APP_ID", "3938951")
    API_HASH = os.environ.get("API_HASH", "6561686ba611b2d46efedef7debd6fa5")
    # Pyrogram Session
    PYRO_STR_SESSION = os.environ.get("PYRO_STR_SESSION", "BQCLnJUjMUsm4uSMya2sINzMkTJsDHoZnN5S8wNwJtQmtbHb93jhYENusm20Pw2ij2DgORogXjk1w7t43C87zWQXPTejZU1WXWaHroHJOx2SWcltD0u8UA44lgvx3H3dnJboMjYPLJib7wxmJ5JM3vh1lBfWKaqAf06HZojuC6ICoqNFCE5j-AsKui2dqQDh8FG_ubaVcp4zlgqBIbIkbPh2TXXNcCnclmosvNw3BbQHerXpaqJLkdYln1VY-ONg5Mu0ifRmEO6anV5tqSvf3Nd1uvniLcQXQTlGmxRwVle2CK7yFkRxvFL1j7X9t0XKr7nnQg60l35NuEkBk88zJvuBSM-CxQA")
    CMD_PREFIX = os.environ.get("CMD_PREFIX", ".")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
