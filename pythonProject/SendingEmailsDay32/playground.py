from smtplib import SMTP
with SMTP("smtp.live.com") as smtp:
    smtp.noop()