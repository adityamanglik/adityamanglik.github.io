---
title: Carbon Measurement & Energy Attribution for Processes and Hardware Devices in the Linux Kernel
event: Linux Foundation Open Source Summit-2023
event_url: https://events.linuxfoundation.org/open-source-summit-japan/program/schedule/
location: Tokyo, Japan
summary: Linux process energy measurement and carbon footprint reduction
abstract: >
  This talk highlights the recent developments in carbon measurement infrastructure within the Linux kernel’s power subsystem. Our primary goal is to accurately determine the energy consumption of hardware devices and software processes, and to link these measurements to carbon emissions. By revealing which devices and processes are driving a system’s overall energy consumption and emissions, users and developers can make more informed decisions regarding performance, power management, and environmental impact. We will discuss how multivariate regression models are used to estimate consumption at both process and device levels, explore privacy implications, and present the ongoing work needed to refine the models. This session offers a valuable opportunity to gather feedback from the open-source community, ensuring the infrastructure continues to evolve toward more reliable prediction and improved user control.

date: 2024-02-03T13:55:00+02:00
all_day: true
publishDate: '2023-12-06T00:00:00Z'
authors:
  - admin
tags: []
featured: true

image:
  caption: ""
  focal_point: ""
  preview_only: false

slides: lfe2023
projects: []
---

<!-- 
Talk Outline:

1. Why carbon and energy measurement is a first-class design constraint across desktop, server, and mobile-class systems.
2. Demonstrating the value of carbon-aware power consumption data for diverse stakeholders: end-users, application programmers, kernel developers, and system designers.
3. Comparative survey of power measurement techniques in competing operating systems and environments.
4. Detailed discussion of the new Linux kernel infrastructure, including multivariate regression models for attributing energy consumption to hardware devices and processes.
5. Privacy concerns around collecting and exposing per-process and per-device power data.
6. Future directions and feedback solicitation: model refinement, accuracy improvements, and privacy-preserving designs.
-->
