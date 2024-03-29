---
title: Power attribution and Estimation Engine in Linux
summary: To design and develop high performance, lightweight power measurement and attribution systems inside Linux.
date: "2020-08-03T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ''

links:
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides:
---
Worked on development of the power panel in GNOME-Usage with Felipe Borges and Christian Kellner.

## Project Log
* Problem and Motivation: Why: not all software is created equal. Some are more harmful than others, just like website have different footprints. We want fairness in energy consumption via quantification for each process
* The What, Who, Why, When, Where, & How of the Power Measurement problem
* Windows Energy Estimation Engine breakdown: [Link](https://embeddedintelligence.wordpress.com/windows-energy-estimation-engine)
* Windows System Power Report : [Video 1](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-168-Powercfg-Sleep-Study), [Video 2](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-181-System-Power-Report)
* MAC OS X Activity Monitor Power Impact breakdown: [Link](https://embeddedintelligence.wordpress.com/mac-os-x-energy-impact)
* Android Power Measurement system : Unknown!
* Reverse Engineering PowerTOP : Link
* Understanding Intel RAPL: Link
* Developing the power models, collecting and crunching global user data
* UPower - System Architecture and Integrations
* Linux Process accounting infrastructure and integrating power event recording
* turbostat - Accessing CPU and GPU Package details and power: [Link](https://manpages.debian.org/testing/linux-cpupower/turbostat.8.en.html)
* Comparison and embedding into sysprof --> Right now gives only CPU and GPU usage, whereas power is a multi-faceted problem
* Update SuperUser question for all power models: [Link](https://superuser.com/questions/1304014/power-consumption-in-windows-10-and-linux)
* Next step = GPU in GNOME-Usage. [GSoC Proposal](https://drive.google.com/file/d/1kQZQLHIANHIsRSQXw_C3Uffz_SeDuQzg/view)
* [Intel CPU Energy analysis tool](https://software.intel.com/content/www/us/en/develop/documentation/energy-analysis-user-guide/top.html)

## Known tools (from LFE Summit)
* [PowerAPI](https://powerapi.org/)
* [Code Carbon](https://mlco2.github.io/codecarbon/index.html)
* [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/)
* [Green Algorithms calculator](https://www.green-algorithms.org/app-user-guide/)
* [GreenFrame](https://greenframe.io/)

## Kernel Developer
* [wookey](wookey.org)

## Relevant Research Papers
* Performance is NOT same as energy -- https://www.sciencedirect.com/science/article/pii/S0306261920304694
* Good paper on power impact of managed languages: https://users.cecs.anu.edu.au/~steveb/pubs/papers/powerperf-asplos-2011.pdf
* https://www.microsoft.com/en-us/research/publication/empowering-developers-to-estimate-app-energy-consumption/
* [AppScope: Application Energy Metering Framework for Android Smartphone Using Kernel Activity Monitoring](
https://www.usenix.org/conference/atc12/technical-sessions/presentation/yoon)
* [DRAM Power Measurement with RAPL](http://web.eece.maine.edu/~vweaver/projects/rapl/2016_memsys_rapl.pdf)
* [RAPL for memory](https://dl.acm.org/doi/10.1145/1840845.1840883)
* https://ieeexplore.ieee.org/document/5751489
* http://www.cs.columbia.edu/~lierranli/coms6998-11Fall2012/papers/eprof_eurosys2012.pdf
* https://dl.acm.org/doi/pdf/10.1145/3194078.3194079
* https://dl.acm.org/doi/10.1145/3229631.3229633
* https://dl.acm.org/doi/pdf/10.5555/2872599.2872613
* https://dl.acm.org/doi/10.1145/3575693.3575709
* https://dl.acm.org/doi/10.1145/3575693.3575754

## Data collection sources
* Tracy: Can collect data from HPC systems for workloads to fine-tune the model

## Resources
* Linux packages to poll information: https://manpages.debian.org/testing/linux-cpupower/index.html
* https://apenwarr.ca/log/20061024
* Linux ACPI Intel Documentation: [Link](https://01.org/linux-acpi)
* Linux process management: [Link](https://tldp.org/LDP/tlk/kernel/processes.html)
* Linux Process Model (from 2000) : [Link](https://www.linuxjournal.com/article/3814)
* Smart Battery Systems: [Link](https://batteryuniversity.com/learn/article/inner_workings_of_a_smart_battery)
* Hacking Battery Firmware for fun and profit: [Link](https://media.blackhat.com/bh-us-11/Miller/BH_US_11_Miller_Battery_Firmware_Public_WP.pdf)
* https://www.semanticscholar.org/paper/Adaptive-Power-Management-Based-on-Reinforcement-Liu-Hsu/40b943ed1f4514979b2b997c3a675cb77ec635c7
* Is it possible to compute carbon footprint of the current application: https://css-tricks.com/reduce-your-websites-environmental-impact-with-a-carbon-budget/ ?
* https://www.phoronix.com/scan.php?page=news_item&px=GNOME-Usage-Power-2020
* https://utcc.utoronto.ca/~cks/space/blog/linux/LoadAverageWhereFrom
* https://eclecticlight.co/2022/05/02/dont-trust-activity-monitor-on-m1-macs/
* https://medium.com/codex/what-are-the-greenest-programming-languages-e738774b1957
* https://sites.google.com/view/energy-efficiency-languages/home

## Links from LFE
* https://greensoftware.foundation/projects/
* https://greensoftware.foundation/articles/software-carbon-intensity-sci-specification-project
* https://codecarbon.io/#howitwork
* https://news.microsoft.com/de-ch/2023/01/10/carbon-aware-computing-whitepaper/
* https://blog.google/inside-google/infrastructure/data-centers-work-harder-sun-shines-wind-blows/
* Toward Carbon-Aware Networking, Noa Zilberman, University of Oxford
* https://news.microsoft.com/de-ch/2023/01/10/carbon-aware-computing-whitepaper/
* https://www.microsoft.com/en-gb/industry/blog/technetuk/2021/10/12/how-to-measure-and-reduce-the-carbon-footprint-of-your-application/