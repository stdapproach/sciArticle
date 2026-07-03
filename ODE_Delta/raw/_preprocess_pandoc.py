import re

with open('solveLinearOdeDeltaFunction.md', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Pass 1: ensure a blank line precedes every ATX heading line
pass1 = []
for line in lines:
    if line.startswith('#') and pass1 and pass1[-1].strip() != '':
        pass1.append('')
    pass1.append(line)

# Pass 2: fix inline-math (single $) delimiter adjacency across lines.
# Tracks whether we are currently inside an open single-$ math span.
# An opener is always a standalone '$' line (glue right, to the next
# line). A closer may be a standalone '$' line (glue left, to the
# previous line) OR embedded at the end of a content line (already
# fine as-is, since it's not preceded by whitespace).
lines = pass1
new_lines = []
i = 0
n = len(lines)
in_math = False
while i < n:
    line = lines[i]
    if not in_math:
        if line.strip() == '$':
            if i + 1 < n:
                new_lines.append('$' + lines[i + 1])
                i += 2
            else:
                new_lines.append(line)
                i += 1
            in_math = True
        else:
            new_lines.append(line)
            i += 1
    else:
        if line.strip() == '$':
            if new_lines:
                new_lines[-1] = new_lines[-1] + '$'
            else:
                new_lines.append('$')
            i += 1
            in_math = False
        elif '$' in line:
            new_lines.append(line)
            i += 1
            in_math = False
        else:
            new_lines.append(line)
            i += 1

out = '\n'.join(new_lines)

# Pass 3: strip spaces immediately inside single-$ (not $$) delimiters
# on the same line, e.g. '$ \int ... $' -> '$\int ... $'
out = re.sub(r'(?<!\$)\$ +', '$', out)
out = re.sub(r' +\$(?!\$)', '$', out)

with open('_pandoc_build.md', 'w', encoding='utf-8') as f:
    f.write(out)
print('wrote _pandoc_build.md')
