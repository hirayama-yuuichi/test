
#test
import matplotlib.font_manager as fm
import pandas as pd

fonts=fm.findSystemFonts()


for f in sorted(fonts):
    font=fm.FontProperties(fname=f)
    print(font.get_name())
#"HGSeikaishotaiPRO"
