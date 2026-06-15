// ========================================================================
//   spec.typ — RESEARCH SPEC (project-independent single source of truth)
// ========================================================================
//   This is YOUR standing reference: the definitions, models, and
//   notation that hold across all of your research, independent of any
//   single project. This is a SCAFFOLD to be changed and edited over time.
//
//   Compile to PDF:   typst compile spec.typ
//   Live preview:     typst watch spec.typ
// ========================================================================

#set page(numbering: "1", margin: 2.2cm)
#set heading(numbering: "1.1")
#set par(justify: true)
#set text(size: 11pt)

#align(center)[
  #text(size: 17pt, weight: "bold")[Research Spec]
  #v(0.3em)
  #text(size: 10pt)[#emph[your name] #h(1em) Last updated: #emph[YYYY-MM-DD]]
]

#align(center)[
  #emph[Project-independent definitions, models, and notation for my research.]
]

#outline(indent: auto)
#v(1em)
#line(length: 100%)

= Scope and conventions
// What this document covers, and the conventions you follow (units,
// indexing, naming, etc.). Set the ground rules once.
_TBD_

= Notation
// Every symbol you use across your work, defined once. A table works well.
#table(
  columns: (auto, 1fr),
  align: (left, left),
  table.header([*Symbol*], [*Meaning*]),
  [$x$], [_TBD_],
  [$y$], [_TBD_],
)

= Definitions
// Formal definitions of the core concepts in your field of work.
// Number them so projects can refer back to them.
*Definition 1.* _TBD_
