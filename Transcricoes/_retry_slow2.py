import time, sys, os
sys.path.insert(0, '.')
import _extract2 as m

folder = f"{m.BASE}/PT-EarthAndSpaceSciencesX"
for vid, title in m.ESSX:
    fn = m.slugify(title) + ".txt"
    if os.path.exists(os.path.join(folder, fn)):
        continue
    m.process(vid, fn, folder, "pt-BR,pt,en")
    time.sleep(60)
