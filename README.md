# Illumina Run Metrics Grabber
This tool is a script for Windows computers used to extract the run metric information from an Illumina Sequencing run utilizing the InterOp package made available by Illumina (https://github.com/Illumina/interop). This tool uses the summary application to provide an output of the run summary information, and extracts the following run information:  
-Run name  
-%Q30  
-Yield (in Gbp)  
-PhiX alignment  
-Error rate  
-Scored cycles  
-Lane cluster density and %Pass filter  


https://github.com/dmatica/run-metrics-grabber/assets/4794041/6282f201-baac-48cf-a299-3270be66dbf5

## How it works
Illumina’s Sequencing Analysis Viewer is a tool to view the various performance metrics for sequencing runs from an Illumina instrument. While this is great for visualizing Q30 performance, or assessing cluster density, it does not allow for easy export of metrics, should we wish to database these metrics.

<img width="1682" alt="Screenshot 2024-02-21 at 10 55 53 PM" src="https://github.com/dmatica/run-metrics-grabber/assets/4794041/816bf159-3aa3-45c3-9cda-bd1d2d97662e">

Run Metrics Grabber works by utilizing the InterOp package’s summary application, which provides the output above, which looks similar to the Summary tab in SAV. From this output, the script scrapes the Run Name, number of cycles scored, % reads >=Q30, Yield (in Gbp), PhiX alignment and error rates (if applicable), cluster density, and % clusters passing filter. From there, the script then sends these values into the clipboard, which can then be pasted into a document.

## Installation instructions
First, download the following files:
1. Extraction script: RMG_v1.0.py or RMG_v1.0.exe
2. Batch file: RMG_v1.0.bat

Next, save the Run Metrics Grabber script to C:\Illumina_Resources. We'll then want to open a File Explorer window, and in the address bar, type in 'shell:sendto'. We're going to place the RMG_v1.0.bat file there. Once we do this, we should be able to access this script by right clicking on a Run Folder and then navigating down to the 'Send to' option.
