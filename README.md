# Simple-TCP-Port-Scanner-with-Banner-Grabbing
This Python script is a lightweight TCP port scanner that identifies open ports on a specified IP address and attempts to retrieve service banners. Utilizing Python's built-in socket library, it connects to each port within a user-defined range, providing insights into active services and potential vulnerabilities.

Key Features:

Scans ports from 1 up to a specified limit on a target IP address.

Identifies open TCP ports.

Attempts to retrieve and display service banners for open ports.

Implements a timeout mechanism to prevent hanging on unresponsive ports.
