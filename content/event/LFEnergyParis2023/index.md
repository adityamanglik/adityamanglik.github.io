---
title: Measuring Carbon Footprint of Personal Computing
event: Linux Foundation Energy Summit-2023
event_url: https://events.linuxfoundation.org/lfenergysummit/
location: Paris, France
summary: Linux process energy measurement
abstract: This talk aims to detail the recent developments in power tracking infrastructure in the Linux kernel for measuring the energy consumption of hardware devices and software applications.

# summary: An example talk using Wowchemy's Markdown slides feature.
# abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellusac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam.'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-06-02T13:55:00+02:00
# date_end: 2018-07-05T00:10:59+05:30
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: '2023-06-06T00:00:00Z'

authors: 
  - admin
tags: []

# Is this a featured talk? (true/false)
featured: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

# links:
#   - icon: twitter
#     icon_pack: fab
#     name: Follow
#     url: https://twitter.com/georgecushen
# url_code: https://summerofcode.withgoogle.com/archive/2018/projects/5742960490577920/
# url_pdf: 
# url_video: https://youtu.be/DTeVkaFqFsA?t=1526

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: lfe2023

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
<!-- 
{{% callout note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /callout %}}

Slides can be added in a few ways:

- **Create** slides using Wowchemy's [_Slides_](https://wowchemy.com/docs/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://wowchemy.com/docs/writing-markdown-latex/).

Further event details, including [page elements](https://wowchemy.com/docs/writing-markdown-latex/) such as image galleries, can be added to the body of this page. -->

 The talk focuses on power measurement and attribution for software (processes) and hardware devices. The objective is to detail the developments in power tracking infrastructure in the Linux kernel for measuring the energy consumption of hardware devices and software applications. These statistics are extremely useful for both end-users and developers. The focus would be on a detailed discussion of multivariate regression models to determine application and hardware device energy consumption. There are also privacy concerns attached to this data, which need feedback from more developers. LF Energy Summit would be a great platform to present the work to the developer community and get feedback to improve the system design. Talk Outline 1) Understanding why power consumption is a first-class design constraint in modern systems, including desktop, server, and mobile-class systems 2) Demonstrating the value of power consumption across different stakeholders, including end-users, application programmers, kernel developers, and system designers 3) Survey results from corresponding systems in competing environments and OS 4) System design proposal and evaluation 