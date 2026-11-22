// MathJax configuration for MkDocs Material + pymdownx.arithmatex (generic mode).
//
// arithmatex converts Markdown math into \( ... \) (inline) and \[ ... \] (display)
// and wraps them in <span class="arithmatex">, so those are the only delimiters
// MathJax has to know about here.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Re-typeset equations after every instant-navigation page change.
document$.subscribe(() => {
  if (window.MathJax && MathJax.typesetPromise) {
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  }
});
