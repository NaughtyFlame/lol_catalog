from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Region, Champion

engine = create_engine('sqlite:///regionchampion.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

pic_url_font = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"

info_url_font = "http://gameinfo.na.leagueoflegends.com/en/game-info/champions/"


"""
champion1 = Champion(name = "", slug ="", role = "", description = description, region = region1)
session.add()
session.commit()

"""

# Champions for Demacia
description = """
Demacia is a strong, lawful society with a prestigious military history.
It values the ideals of justice, honor and duty highly, and its people are
fiercely proud.
"""
region1 = Region(name = "Demacia", slug = "demacia", description = description)

session.add(region1)
session.commit()

# No.1 champion
description = """
Garen is a warrior of Demacia who has devoted his life to defending his kingdom and its ideals. Armed with his magic-resistant armor and broadsword, Garen puts his life on the line for both his nation, and his fellow soldiers.
"""
pic_url = pic_url_font + "Garen_0.jpg"
info_url = info_url_font + "garen/"
champion1 = Champion(name = "Garen", slug ="garen", role = "Fighter", description = description, pic_url = pic_url, info_url = info_url, region = region1)

session.add(champion1)
session.commit()

# No.2 champion
description = """
Sona has no memories of her true parents. As an infant, she was found abandoned on the doorstep of an Ionian adoption house, nestled atop an ancient instrument in an exquisite case of unknown origins. She was an unusually well-behaved child, always quiet and content.
"""
pic_url = pic_url_font + "Sona_0.jpg"
info_url = info_url_font + "sona/"
champion2 = Champion(name = "Sona", slug ="sona", role = "Support", description = description, pic_url = pic_url, info_url = info_url, region = region1)
session.add(champion2)
session.commit()

# No.3 champion
description = """
Luxanna Crownguard is a powerful young light mage from Demacia, an insular realm where magical abilities are viewed with fear and suspicion. Forced to keep her power secret for much of her young life, she grew up fearing discovery and exile, but learned to embrace her magic and covertly wields it in service of her homeland.
"""
pic_url = pic_url_font + "Lux_0.jpg"
info_url = info_url_font + "lux/"
champion3 = Champion(name = "Lux", slug ="lux", role = "Mage", description = description, pic_url = pic_url, info_url = info_url, region = region1)
session.add(champion3)
session.commit()

# No.4 champion
description = """
Prince Jarvan IV comes from a lineage of kings, and is favored to lead Demacia in the next era.
"""
pic_url = pic_url_font + "JarvanIV_0.jpg"
info_url = info_url_font + "jarvaniv/"
champion4 = Champion(name = "Jarvan IV", slug ="jarvaniv", role = "Tank", description = description, pic_url = pic_url, info_url = info_url, region = region1)
session.add(champion4)
session.commit()

# No.5 champion
description = """
Lucian wields relic weapons imbued with ancient power and stands a stalwart guardian against the undead.
"""
pic_url = pic_url_font + "Lucian_0.jpg"
info_url = info_url_font + "lucian/"
champion5 = Champion(name = "Lucian", slug ="lucian", role = "Markman", description = description, pic_url = pic_url, info_url = info_url, region = region1)
session.add(champion5)
session.commit()

# No.6 champion
description = """
The most feared duelist in all Valoran, Fiora is as renowned for her brusque manner and cunning mind as she is for the speed of her bluesteel rapier.
"""
pic_url = pic_url_font + "Fiora_0.jpg"
info_url = info_url_font + "fiora/"
champion6 = Champion(name = "Fiora", slug ="fiora", role = "Fighter", description = description, pic_url = pic_url, info_url = info_url, region = region1)
session.add(champion6)
session.commit()


# Champions for Zaun
description = """
Zaun is a large, undercity district, lying in the deep canyons and valleys threading Piltover.
"""
region2 = Region(name = "Zaun", slug = "zaun", description = description)

session.add(region2)
session.commit()

# Champions for Piltover
description = """
Piltover is a thriving, progressive city whose power and influence is on the rise.
"""
region3 = Region(name = "Piltover", slug = "piltover", description = description)

session.add(region3)
session.commit()

# Champions for Shadow Isles
description = """
The land now known as the Shadow Isles was once a beautiful realm, but it was shattered by a magical cataclysm.
"""
region4 = Region(name = "Shadow Isles", slug = "shadow-isles", description = description)

session.add(region4)
session.commit()

# Champions for Mount Targon


# Champions for Shurima


# Champions for Bilgewater


# Champions for Ionia


# Champions for Freljord


# Champions for Noxus


# Champions for Void


# Champions for Bandle City

print "added menu items!"
