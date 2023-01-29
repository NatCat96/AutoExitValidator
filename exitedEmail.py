import smtplib

beaconchain_link = "https://beaconcha.in/validator/"
explorer_link = "https://etherscan.io/address/"

sender_email = "email_to_send_from@gmail.com"
#list of emails to alert
email_list = ["email_1_to_send_to@gmail.com"]
#the password is an application password that can be configured in gmail account settings
password = "PASSWORD"

#list of validator index numbers
validator_list = ["12345"]
#the address you plan to set validator withdrawals to
withdrawal_address = "ETHEREUM ADDRESS"

withdrawal_address_message = "\nThe Ethereum will all be withdrawn to the address {}. To view this address visit {}{}".format(withdrawal_address, explorer_link, withdrawal_address)

def send_email(receiver_email):
    message = "Subject: Ethereum Validator\n\nThe validators have been exited.\n\n The funds will be automatically withdrawn to {}.\n\nPlease note that there is a withdrawal queue, so even though the validators are exited it may take additional time for the funds to show up.".format(withdrawal_address)

    beaconchain_links = "\nTo track the current status of the validators you can use the following links:\n\n"

    for validator in validator_list:
        beaconchain_links += "{}{}\n".format(beaconchain_link, validator)

    message += beaconchain_links + withdrawal_address_message

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

for email in email_list:
    send_email(email)
