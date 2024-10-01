function copy_regex() {
    const regex = document.getElementById("regex").value
    navigator.clipboard.writeText(`r"${regex}"`)
}

function fix_height() {
    const e = (x) => { return document.getElementById(x) }
    const gs = (x, y) => { return parseFloat(getComputedStyle(x)[y]) }

    const doc_height = document.documentElement.clientHeight;
    const nb = e("navbar"), l = e("sample-label"), r = e("regex");

    const max_height = doc_height - gs(nb, "height") - (2 * gs(nb, "padding")) - gs(nb, "borderBlockEndWidth");
    const s_height = max_height - gs(r, "height") - (4 * (gs(l, "height") + gs(l, "margin") + gs(r, "margin")));

    e("content").style.maxHeight = max_height + "px";
    e("test-string").style.height = s_height + "px";
}

document.addEventListener("DOMContentLoaded", () => { fix_height() })