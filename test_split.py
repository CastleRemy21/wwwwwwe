from split import split_text
from embed_and_store import add_documents

test_text = """
The twilight sky shimmered with hues of violet and amber as the distant echoes of laughter drifted through the quiet streets. A lone cat stretched lazily on a warm brick wall, eyes half-closed in contentment. Somewhere in the distance, the faint hum of a radio played an old song, its melody lost to time. The air was thick with the scent of blooming jasmine and freshly turned earth, a reminder that the seasons were shifting, though the world seemed unaware.

Beneath the glow of a flickering streetlamp, a notebook lay forgotten on a wooden bench. Its pages fluttered in the breeze, revealing sketches of fantastical creatures and scribbled notes about dreams yet to be chased. A few pages were dog-eared, and a faded ink stain stretched across the cover, evidence of countless moments spent lost in thought. The wind carried the scent of rain, whispering secrets only the night could understand.

Further down the cobblestone path, an old man sat outside his shop, whittling a small wooden bird. His hands, weathered and strong, moved with careful precision, shaping the delicate figure as if coaxing life from the grain. A lantern hung beside him, casting a golden glow on the shop’s worn wooden sign, its letters barely legible from years of sun and storm. Inside, the scent of sawdust mingled with the rich aroma of freshly brewed tea, waiting for customers who seldom came at this hour.

Across the street, a woman in a flowing blue dress walked slowly, the hem of her skirt brushing against the pavement. She carried a stack of old books bound with twine, their spines faded and frayed. Her steps were measured, as if walking through a memory rather than a city, her gaze lost in the distance. She paused by the window of a quiet café, peering inside at the lone barista wiping down the counter, their movements rhythmic and unhurried. The glow of the café’s hanging lights reflected in the window, merging with the stars above in a quiet, unspoken symmetry.

Somewhere, a clock chimed the hour, its sound swallowed by the hush of the evening. A few streetlights flickered, their bulbs struggling against the inevitable encroachment of time. A bicycle leaned against a wrought iron fence, its tires caked with dust, as if waiting for its owner to return from an adventure long since forgotten.

The city breathed in the night, wrapped in the hush of anticipation. Somewhere, dreams were being formed, stories were being written, and the quiet promise of another day lingered just beyond the horizon.
"""

user_id = '321'
document_id = '12345'
splits = split_text(test_text, user_id, document_id)
for split in splits:
    print(split.page_content[:50], split.metadata)

vector_ids = add_documents(splits)
print('---------------')
print(vector_ids)