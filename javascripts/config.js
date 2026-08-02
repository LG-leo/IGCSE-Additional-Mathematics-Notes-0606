window.MathJax = {
  tex: {
    inlineMath: [
      // 原有的
      ["\\(", "\\)"],
      ["$", "$"],
      // 新增10种（注意：部分可能与Markdown语法冲突，需谨慎使用）
      ["\\[", "\\]"],        // 注意：\\[\\] 通常用于块级，放在行内可能不合理，但技术上可以
      ["\\begin{math}", "\\end{math}"],
      ["`$", "$`"],          // 反引号包裹的 $...$（减少转义需求）
      ["\\$", "\\$"],        // 转义后的美元符（其实等于 $...$，重复了）
      ["{\\$", "\\$}"],      // 花括号包裹的美元符
      ["\\{", "\\}"],        // 花括号作为分隔符（极易冲突，不推荐）
    ],
    displayMath: [
      // 原有的
      ["\\[", "\\]"],
      ["$$", "$$"],
      // 新增10种
      ["\\begin{equation}", "\\end{equation}"],
      ["\\begin{align}", "\\end{align}"],
      ["\\[\\[", "\\]\\]"],   // 双方括号
      ["\\{", "\\}"],          // 花括号作为块级（极不推荐）
      ["\\(", "\\)"],          // 重复
      ["\\begin{displaymath}", "\\end{displaymath}"],
      ["\\begin{gather}", "\\end{gather}"],
      ["\\<\\[", "\\]\\>"],    // 自定义
      ["\\#\\#", "\\#\\#"],    // 双井号（Markdown标题可能冲突）
      ["\\$\\$\\$", "\\$\\$\\$"]  // 三个美元符（少用）
    ],
    processEscapes: true,
    processEnvironments: true,
    tags: 'ams'
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// 动态渲染
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
