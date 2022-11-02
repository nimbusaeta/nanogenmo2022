import random
import re

random.seed()

original_text = '''
En un lugar de la Mancha,
de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
adarga antigua,
rocín flaco y galgo corredor.
Una olla de algo más vaca que carnero,
salpicón las más noches,
duelos y quebrantos los sábados,
lantejas los viernes,
algún palomino de añadidura los domingos,
consumían las tres partes de su hacienda.
'''


def extract_fragments_layout(text):

    regex = r"[a-záéíóúüñ][a-záéíóúüñ ]+"

    layout = re.sub(regex, '<f>', text, 0, re.MULTILINE | re.IGNORECASE)

    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    fragments=[]
    for _, match in enumerate(matches):
        fragments.append(match.group())

    return fragments, layout


def restore_text(fragments, layout):

    matches = re.finditer(pattern='<f>', string=layout)
    pos = []
    for m in matches:
        pos.insert(0, (m.start(), m.end()))
    assert len(pos) == len(fragments)

    for (start, end) in pos:
        layout = layout[:start] + fragments.pop() + layout[end:]

    return layout


# Separa el texto en "fragmentos" y "maqueta"
fragments, layout = extract_fragments_layout(original_text)
print(fragments)
print(layout)

# Desordena los fragmentos
random.shuffle(fragments)

# Recompone el texto a partir de la maqueta y los fragmentos desordenados
restored_text = restore_text(fragments, layout)
print(restored_text)