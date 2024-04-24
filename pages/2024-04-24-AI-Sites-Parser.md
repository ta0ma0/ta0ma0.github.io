---
title: "AI Sites Parser"
date: 2024-04-24 20:01:00 -0000
categories: 
- ChatGPT
- requests
- html2text
- AI
- Parser
---

<center>
<!-- ![tg-sample]({{ "/assets/install_script.png" | relative_url }}) -->
<picture>
  <source media="(max-width: 375px)" srcset="/static/images/harvester_375w.jpg">
  <source media="(max-width: 640px)" srcset="/static/images/harvester_375w.jpg">
  <img src="/static/images/harvester.jpg" width='640' alt="Screenshot">
</picture>
</center>

<p>
Once on the Internet I came across a perplexed question: why is it still impossible to send AI to a website and parse all the necessary information from it? As it turned out, it is possible, but all available AI interfaces offer one request to one site at a time. The person wanted to get the same type of information from a whole list of sites. I already had an idea of how it works and I offered him to make such a parser for a small fee. After some time, the project was ready, I received the first bitcoins in my life, and the client was satisfied.
</p>
<p>
A few technical details. It's simple, the program downloads pages from specified sites, converts them into text, and then transfers them to LLM to extract phone numbers and addresses from the text. It would seem that the problem can be solved using regular expressions, but in this case, the AI showed itself well, the efficiency of the program was 70% on the presented sample; 30% either did not answer or did not provide their addresses.
</p>