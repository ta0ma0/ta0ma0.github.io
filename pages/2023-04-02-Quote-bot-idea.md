---
title: "Cyberpunk quote bot"
date: 2023-04-02 15:40:00 -0000
categories: 
- Ideas 
- Telegram
- Programming
- Python
---
<center>
<!-- ![tg-sample]({{ "/assets/tg-bot-sample.png" | relative_url }}) -->
<picture>
  <source media="(max-width: 375px)" srcset="/static/images/tg-bot-sample-375w.png">
  <source media="(max-width: 640px)" srcset="/static/images/tg-bot-sample.png">
  <img src="/static/images/tg-bot-sample.png" alt="Screenshot">
</picture>
</center>

I needed an idea for a home programming project and I found it. I decided to create a bot that would post a picture from DeviantArt and a quote from a cyberpunk book in a chat. While looking for interesting images on DeviantArt, I came across the [Openverse](https://openverse.org/) website where you can find CC-licensed images. I decided to use this site and find interesting pictures by tag "cyberpunk". For quotes, I searched [Goodreads](https://www.goodreads.com/) and found 370 hand-picked cyberpunk quotes. The bot can now load images from Openverse with the "/load" command and post a quote from Goodreads with the "/quote" command. Both elements are selected from a pre-created database in random order, so after a while repetitions will be inevitable.

[Telegram-bot on github](https://github.com/ta0ma0/quotes_images)

[Telegram-bot](https://t.me/CyberpunkQuotesBot)
