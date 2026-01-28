# SRMU Attendance Automation (eYojan Portal)

> **Educational & Personal Use Only**

An automated Python script to log in to the **SRMU eYojan portal**, generate the student attendance report, and download it as a PDF — without manual interaction.

This project was researched, discovered, and developed by **Ankit Kumar Sharma**, a student of **BCA** at **Shri Ramswaroop Memorial University (SRMU)**.

---

## Overview

SRMU’s eYojan (PeopleSoft) portal requires multiple manual steps to access attendance reports.  
This automation streamlines the entire flow:

- Login to the portal
- Navigate to the Attendance section
- Generate the attendance report
- Download the PDF automatically

During research, an **OTP verification bypass** was identified in the workflow, which made full automation possible.  
This repository demonstrates the automation **without exposing sensitive exploit logic**.

---

## Features

- Automated login using Selenium + Undetected ChromeDriver
- Automatic navigation to Attendance page
- Attendance report generation
- PDF download support
- Uses `undetected_chromedriver` to avoid bot detection
- Config-based credentials (no hardcoding)

---

## Tech Stack

- **Python 3.10+**
- **Selenium**
- **undetected-chromedriver**
- **Google Chrome (v143 recommended)**

---

## Important

- **This code is a dummy version of my main code. it is just a reference not the real code. it wont work**