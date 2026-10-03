import time, importlib, sys
sys.path.insert(0, '.')
import _extract2 as m

remaining = [(v,t) for v,t in m.ESSX]
folder = f"{m.BASE}/PT-EarthAndSpaceSciencesX"
import os
for vid, title in remaining:
    fn = m.slugify(title) + ".txt"
    if os.path.exists(os.path.join(folder, fn)):
        continue
    m.process(vid, fn, folder, "pt-BR,pt,en")
    time.sleep(15)
