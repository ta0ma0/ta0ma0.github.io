---
layout: post
title: "Parser strace logs"
date: 2023-04-05 14:44:00 +0400
categories: [Parser, SQL, Strings]
---

<!-- ![Screenshot.png](/static/images/strace_parser.png) -->
<picture>
  <source media="(max-width: 375px)" srcset="/static/images/strace_parser-375w.png">
  <source media="(max-width: 640px)" srcset="/static/images/strace_parser.png">
  <img src="/static/images/strace_parser.png" alt="Screenshot">
</picture>

It happened on a certain day in my professional career that I encountered a vexing problem: how to extract from the strace logs only the sql queries that interested me. I pondered this conundrum for a while, until I remembered that python had a marvelous aptitude for manipulating strings. Thus, I crafted a parser that did the job splendidly, and not only for me, but for my colleagues as well.


[Github](https://github.com/ta0ma0/strace_sql_parse2)
