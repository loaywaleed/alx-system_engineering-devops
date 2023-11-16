# Postmortem: Unexpected Downtime on Web Service
## Issue Summary
Duration:
Start Time: November 11, 2023, 14:20 (GMT +2)
End Time: October 15, 2023, 15:15 (GMT +2)
Impact:
The Nginx service was down for longer than expected which caused users failing to access the web server for a longer than ideal duration.
Root cause:
failing to check syntax of nginx conf file
## Timeline
Detection:
The issue was detected at November 11, 2023, 15:00.
Actions Taken:
Checking nginx conf file and fixed the error which was a syntax error.
Misleading Paths:
Thought it was nginx failing to listen to port 80.
Resolution:
Checked and fixed the syntax error.
## Root Cause and Resolution
Root Cause:
A recent code deployment introduced an unforeseen bug, causing the application to crash under certain conditions.
Resolution:
Checked and fixed the syntax error.
# Corrective and Preventative Measures
Improvements/Fixes:
Always checking syntax before rebooting for new update.
Tasks:
syntax check
making sure nginx works properly after reboot.