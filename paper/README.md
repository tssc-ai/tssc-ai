# Paper sources

- `paper_IT.md`  — Italian source (Pandoc markdown, with `\label`/`\cref` cross-references)
- `paper_IT.pdf` — compiled Italian PDF
- `template-tssc.latex` — Pandoc/LaTeX template (cleveref configured for Italian)

## Build

```
pandoc paper_IT.md -o paper_IT.pdf \
  --pdf-engine=xelatex -N --toc \
  --template=template-tssc.latex \
  -V documentclass=article \
  --top-level-division=chapter
```

The English translation (`paper_EN.md` / `paper_EN.pdf`) is in progress and will
be added here when ready.
