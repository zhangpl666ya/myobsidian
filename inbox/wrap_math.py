import re

path = r"C:\Users\39173\Desktop\笔记\myobsidan\inbox\讲义.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# State machine: track whether we're inside $$..$$ or $...$
# Output accumulator
result = []
i = 0
n = len(content)

while i < n:
    # Check for $$...$$ (display math block)
    if i + 1 < n and content[i] == '$' and i + 1 < n and content[i+1] == '$':
        result.append("$$")
        i += 2
        # Skip content until closing $$
        while i < n:
            if content[i] == '$' and i + 1 < n and content[i+1] == '$':
                result.append("$$")
                i += 2
                break
            result.append(content[i])
            i += 1
    # Check for $...$ (inline math)
    elif content[i] == '$':
        result.append('$')
        i += 1
        while i < n:
            if content[i] == '\\':
                result.append(content[i])
                result.append(content[i+1])
                i += 2
            elif content[i] == '$':
                result.append('$')
                i += 1
                break
            else:
                result.append(content[i])
                i += 1
    # Plain text: scan for math patterns
    else:
        # Find next $ or end
        start = i
        while i < n and content[i] != '$':
            i += 1
        segment = content[start:i]

        # Now apply wrapping to this plain-text segment
        # Strategy: wrap sequences that look like math
        # Math pattern: \ commands, subscripts/superscripts, fractions, operators, Greek letters
        # We use a lookahead: find known LaTeX commands and wrap them

        wrapped = []
        pos = 0
        seg_len = len(segment)

        while pos < seg_len:
            # Try to match a math token at current position
            # Patterns (must start with \ or a digit/number, or be a comparison/number pattern)

            # Pattern 1: \command{...} or \command
            m = re.match(r'\\([a-zA-Z]+)(?:\b|_)', segment[pos:])
            if m:
                # check there's actual math context
                MathCommands = [
                    'frac', 'sqrt', 'sum', 'prod', 'int', 'partial', 'infty',
                    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'theta', 'lambda',
                    'mu', 'sigma', 'omega', 'pi', 'rho', 'Delta', 'Theta', 'Sigma',
                    'Omega', 'Phi', 'Psi', 'mathcal', 'mathbb', 'mathbf', 'textit',
                    'hat', 'bar', 'tilde', 'vec', 'dot', 'ddot', 'overline',
                    'underline', 'underbrace', 'quad', 'qquad', 'ldots', 'cdots',
                    'vdots', 'ddots', 'rightarrow', 'leftarrow', 'Rightarrow', 'Leftarrow',
                    'to', 'infty', 'times', 'div', 'pm', 'mp', 'geq', 'leq',
                    'neq', 'approx', 'equiv', 'subset', 'supset', 'in', 'notin',
                    'cup', 'cap', 'emptyset', 'forall', 'exists', 'lambda',
                    'sin', 'cos', 'tan', 'log', 'exp', 'lim', 'max', 'min',
                    'mathbb', 'begin', 'end', 'label', 'ref', 'dots', 'ldots',
                    'mathcal', 'mathsf', 'mathrm', 'texttt',
                ]
                cmd = m.group(1)
                # Also allow generic \something
                # wrapped.append('$' + m.group(0))
                # Simple approach: if the word after \ is a known math command or a single letter, wrap it
                # Heuristic: if it's a letter sequence, likely a math command
                # Wrap it
                end_pos = pos + m.end()
                # grab everything up to end_pos as math
                math_content = segment[pos:end_pos]
                # But check if this is preceded by text (then wrap only if preceded by space/punct)
                wrapped.append('$' + math_content + '$')
                pos = end_pos
                continue

            # Pattern 2: numbers with operators like x = 3, n >= 1, etc.
            # Match: number or variable, space, operator, space, number
            m = re.match(r'([a-zA-Z_]\w*)\s*([=<>]+|\\leq|\\geq|\\neq)\s*(-?\d+\\.?\d*|\$[^\$]+\$|\{[^{}]*\})', segment[pos:])
            if m:
                math_content = segment[pos:pos+m.end()]
                wrapped.append('$' + math_content + '$')
                pos += m.end()
                continue

            # Pattern 3: fractions like \frac{...}{...}
            if re.match(r'\\frac', segment[pos:]):
                m = re.match(r'\\frac\s*\{', segment[pos:])
                if m:
                    # find matching closing }
                    depth = 0
                    end = pos + len(r'\\frac')
                    while end < seg_len:
                        if segment[end] == '{':
                            depth += 1
                        elif segment[end] == '}':
                            depth -= 1
                            if depth == 0:
                                end += 1
                                break
                        end += 1
                    math_content = segment[pos:end]
                    wrapped.append('$' + math_content + '$')
                    pos = end
                    continue

            # Pattern 4: subscript like X_{...}
            m = re.match(r'([a-zA-Z])\s*_\s*\{([^{}]*)\}', segment[pos:])
            if m:
                math_content = segment[pos:pos+m.end()]
                wrapped.append('$' + math_content + '$')
                pos += m.end()
                continue

            # Pattern 5: superscript like X^{...} or X^n
            m = re.match(r'([a-zA-Z])\s*\^\s*\{([^{}]*)\}', segment[pos:])
            if m:
                math_content = segment[pos:pos+m.end()]
                wrapped.append('$' + math_content + '$')
                pos += m.end()
                continue

            # Pattern 6: Greek letters \alpha \beta etc.
            m = re.match(r'\\(alpha|beta|gamma|delta|epsilon|theta|lambda|mu|sigma|omega|pi|rho|Delta|Theta|Sigma|Omega|Phi|Psi|eta|zeta|iota|kappa|nu|xi|omicron|tau|upsilon|phi|chi|psi|omega)', segment[pos:])
            if m:
                math_content = segment[pos:pos+m.end()]
                wrapped.append('$' + math_content + '$')
                pos += m.end()
                continue

            # Pattern 7: standalone numbers with operators like n \le 5, p_1 = ..., etc.
            # Match variable with subscript or superscript followed by comparison
            m = re.match(r'([a-zA-Z]_?\w*)\s*([=<>]+)\s*(-?\d+\\.?\d*)', segment[pos:])
            if m:
                math_content = segment[pos:pos+m.end()]
                wrapped.append('$' + math_content + '$')
                pos += m.end()
                continue

            # Pattern 8: inline math fragments like \mathcal{S}_0
            m = re.match(r'\\mathcal\s*\{', segment[pos:])
            if m:
                # find matching }
                depth = 0
                end = pos
                while end < seg_len:
                    if segment[end] == '{':
                        depth += 1
                    elif segment[end] == '}':
                        depth -= 1
                        if depth == 0:
                            end += 1
                            break
                    end += 1
                math_content = segment[pos:end]
                wrapped.append('$' + math_content + '$')
                pos = end
                continue

            # No match - copy one character
            wrapped.append(segment[pos])
            pos += 1

        result.append(''.join(wrapped))

output = ''.join(result)

with open(path, 'w', encoding='utf-8') as f:
    f.write(output)

print("Done! Wrapped unwrapped math formulas.")
print(f"Original length: {len(content)}, Output length: {len(output)}")