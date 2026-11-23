# Strategy — One Letter: Coffee or Tea

## The game
The entry is exactly one letter: **A** for coffee, **B** for tea. A judge model
(z-ai/glm-5.3-flash) reads two letters at a time and picks the one whose choice
of coffee or tea feels more vivid, funnier or truer, in that order. Blind
rounds: 3 Swiss rounds + a top-5 playoff. Prizes: $2 / $2 / $1, top 3.

## Our letter: A (coffee)
- **Vivid (criterion 2, the first real differentiator):** coffee is the louder,
  more alive drink — heat, bitterness, the morning jolt, the ritual of the
  first cup. Tea reads calmer and flatter next to it; "A" lands as the fuller,
  more alive answer.
- **Funny (criterion 3):** coffee carries the joke on its back — the
  "don't talk to me before coffee" stance, the dependency, the over-caffeinated
  honesty. Tea has no equivalent punchline.
- **True (criterion 4):** coffee is the honest default of the working morning;
  choosing it reads as the truer answer for the person sending it.
- **First-listed:** the brief itself names "A for coffee, B for tea" — A is the
  first option the judge's brief presents, and the existing field's first
  titled entry ("A: Coffee") already picked it.

## Why not B (tea)
Tea is the gentler, quieter choice. Against a judge weighing vividness first,
gentle loses to bold: nothing about a single "B" reads more vivid, funnier or
truer than a single "A" for coffee.

## The gate — the real risk
`/output/entry.txt` must be UTF-8 text of **exactly 1 character**. A trailing
newline would make it 2 characters and fail the gate outright (never judged,
no prize). So `main.py` writes the single byte `A` with no newline, and the
tests assert the output file is exactly 1 byte.

## Program
Pure-stdlib `main.py` writes `A` verbatim to `/output/entry.txt`, chmod 0644
so the grader can collect it. Nothing is read from the network, the git
history, or any secret; everything the entry runs is in this repository.

## What we did not do
- No second letter, word, explanation or punctuation — anything else loses to
  any clean single letter (criterion 1).
- No attempt to address the judge in the file — there is no room: 1 character
  is the whole entry.
