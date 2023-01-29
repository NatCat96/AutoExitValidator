import smtplib
import optparse

beaconchain_link = "https://beaconcha.in/validator/"
explorer_link = "https://etherscan.io/address/"

parser=optparse.OptionParser()

parser.add_option("-d", "--days", help="Number of days until validators exit")
parser.add_option("-s", "--software", help="The software that is out of date (i.e. Consensus or Execution)")

(opts,args) = parser.parse_args()

sender_email = "email_to_send_from@gmail.com"
#list of emails to alert
email_list = ["email_1_to_send_to@gmail.com"]
#the password is an application password that can be configured in gmail accoun>
password = "PASSWORD"

withdrawal_address = "ETHEREUM ADDRESS"

validator_list = ["12345", "23456"]

withdrawal_address_message = "\nThe Ethereum will all be withdrawn to the address {}. To view this address visit {}{}".format(withdrawal_address, explorer_link, withdrawal_address)

def send_email(days, software, receiver_email):
    message = "Subject: Ethereum Validator\n\nThe validator {} software is out of date. There are {} days left to update before the validator(s) are exited.\n\n If the validators are exited the funds will be automatically withdrawn to {}.\n".format(software, days, withdrawal_address)

    beaconchain_links = "\nTo track the current status of the validator(s) you can use the following link(s):\n\n"

    for validator in validator_list:
        beaconchain_links += "{}{}\n".format(beaconchain_link, validator)

    message += beaconchain_links + withdrawal_address_message

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

for email in email_list:
    send_email(opts.days, opts.software, email)
