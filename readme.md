# SRMU Attendance Automation (eYojan Portal)
# Website Load Tester 
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
> **For Educational and Personal Use Only**

This project is a Python-based automation script that demonstrates how the **SRMU eYojan (PeopleSoft) portal** attendance report workflow can be automated.  
It automates the complete process of logging in, navigating to the attendance section, generating the report, and downloading it as a PDF — without manual interaction.

This project was researched, designed, and developed by **Ankit Kumar Sharma**,  
**BCA student**, **Shri Ramswaroop Memorial University (SRMU)**.

---

## Background

The SRMU eYojan portal requires several repetitive manual steps to access student attendance reports.  
This includes login, verification checks, navigation across multiple pages, and report generation.

The goal of this project was to:
- Understand the portal workflow
- Reduce repetitive manual effort
- Demonstrate browser automation using Python and Selenium
- Learn how modern portals handle verification and session validation

During research, a workflow behavior was observed that made full automation technically possible.  
**This repository does NOT expose any sensitive logic, exploits, or bypass mechanisms.**

---

## What This Project Does

The automation flow includes:

1. Opens the SRMU eYojan portal
2. Logs in using student credentials
3. Navigates to the Attendance section
4. Triggers attendance report generation
5. Downloads the attendance report as a PDF

All steps are handled automatically using browser automation.

---

## Key Features

- Fully automated browser-based workflow
- Attendance report generation without manual clicks
- PDF download handling
- Uses `undetected_chromedriver` to reduce bot detection
- Credentials are read from a configuration file (no hardcoded data)
- Designed for learning, research, and automation practice

---

## Technology Used

- **Python 3.10 or higher**
- **Selenium WebDriver**
- **undetected-chromedriver**
- **Google Chrome (version 143 recommended)**

---

## Project Structure (Example)


