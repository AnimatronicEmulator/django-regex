from re import finditer

def parse_re(re:str, s:str):
    if not (re and s): return []

    try: result = [r.span() for r in finditer(re, s)]
    except: return "Pattern error"
    
    r_iter, spos, response = 0, 0, ""
    done = False if result else True

    while not done:
        r = result[r_iter]
        sa, sb, sc = s[spos:r[0]], s[r[0]:r[1]], s[r[1]:]
        r_iter, spos = r_iter + 1, r[1]

        if sa: response += f"<span class='rmatch'>{sa}</span>"
        response += f"<span class='rmatch ismatch'>{sb}</span>"

        if r_iter == len(result):
            if sc: response += f"<span class'rmatch'>{sc}</span>"
            done = True

    return response or "No matches"