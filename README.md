# THAI_QRCODE Generator

# system
- ubuntu 22.23
- python 3.9.18

This repository contains Python scripts for generating THAI_QRCODE using the `pypromptpay` library.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirement)
- [Usage](#usage)
- [License](#license)

## Introduction

THAI_QRCODE Generator is a set of Python scripts designed to generate QR codes for Thai PromptPay transactions. The scripts leverage the `pypromptpay` library and handle time zone conversions based on a predefined dictionary.


## Requirement
- CRC-ITU==0.3.3
- crc16==0.1.1
- pypng==0.20220715.0
- pypromptpay==0.5.3
- qrcode==7.4.2
- typing_extensions==4.8.0

## setting
```bash
python3.9 -m pip install -r requirement.txt
```

## Usage

### 1. Config file main.py and run for generate QRCODE.

```bash
python3.9 main.py
```