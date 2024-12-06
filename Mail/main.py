from work_with_mail import MailWork

if __name__ == '__main__':
    worker = MailWork('login@gmail.com', 'qwerty')
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    worker.send_message(message, recipients, subject, 587)
    worker.receive_message(None)
