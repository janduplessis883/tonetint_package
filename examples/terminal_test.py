from src.tonetint.sentiment_visualizer import ToneTint
tt = ToneTint()

text = """
On a bright Sunday morning in London, the city hums with a soft, lazy energy. The streets, usually packed with hurried commuters, are now filled with leisurely strollers and families enjoying a slow brunch in trendy cafes. The air is crisp, and the scent of freshly baked croissants mingles with the rich aroma of brewing coffee. Down by the Thames, joggers pass by tourists taking in the iconic skyline, their contrasting paces a reflection of the different ways people unwind. Yet, even amidst the calm, there's a pulse of vibrancy — street performers at Covent Garden strumming upbeat tunes, and the chatter of markets, like Brick Lane, buzzing with life. As the sun starts to set, the quiet anticipation of a new week begins to settle in, tinged with a hint of nostalgia for the fleeting relaxation that Sundays bring.
On a bright Sunday morning in London, the city hums with a soft, lazy energy. The streets, usually packed with hurried commuters, are now filled with leisurely strollers and families enjoying a slow brunch in trendy cafes. The air is crisp, and the scent of freshly baked croissants mingles with the rich aroma of brewing coffee. Down by the Thames, joggers pass by tourists taking in the iconic skyline, their contrasting paces a reflection of the different ways people unwind. Yet, even amidst the calm, there's a pulse of vibrancy — street performers at Covent Garden strumming upbeat tunes, and the chatter of markets, like Brick Lane, buzzing with life. As the sun starts to set, the quiet anticipation of a new week begins to settle in, tinged with a hint of nostalgia for the fleeting relaxation that Sundays bring.
"""

tt.display_terminal(text)
