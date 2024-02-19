---
layout: post
title: "Another report parser"
date: 2024-02-19 00:40:21 +0400
categories: [job, tools, mysql, parser]
---

![Grafana](/docs/assets/grafana.png "Example")

Upon my daily toil at work, I initially found myself wearied by the manual processing of server performance reports. In a fit of ingenuity, I crafted a handful of modest tools to render the routine both more palatable and effective. These contrivances, though abandoned as my manual proficiency reached a pinnacle of perfection, did not quench my thirst for improvement. Thus, on a brief holiday, spanned merely over two days, I embarked upon a new stride in the refinement of client server data analysis. My notebook, through the enchantment of Python, now automatically ensnares the daily dispatches of reports. These documents are then meticulously dissected into lines, from which the paramount figures are extracted—the remaining storage space on the servers. For the depletion thereof spells disaster for the system's operation, as vividly illustrated by the unfortunate episode with [Toyota ](https://futurism.com/the-byte/toyota-factories-shut-down-disk-space).

Further, with scrupulous precision, I dissected the lines into their elemental components, for which I extend my gratitude to Python, and ensconced them within a MySQL database. From this repository, through a series of queries, I retrieve the necessary data to craft tables and charts in Grafana, operating within a Docker container on my local host.

I harbor no ill will towards my company, yet I am possessed by the sensation that my skills languish unappreciated within the confines of my current employ. Nonetheless, I cease not in the creation of tools, though they lack a proper audience to commend their worth.