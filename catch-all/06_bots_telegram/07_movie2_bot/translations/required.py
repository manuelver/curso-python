import gettext

""" localization support """
en = gettext.translation(
    'messages', 'translations/generated', languages=['en']
)

pt_br = gettext.translation(
    'messages', 'translations/generated', languages=['pt_BR']
)

es = gettext.translation(
    'messages', 'translations/generated', languages=['es']
)

ca = gettext.translation(
    'messages', 'translations/generated', languages=['ca']
)

en.install()