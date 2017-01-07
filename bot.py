from slackclient import SlackClient
import os, time, random, re


responses = ['Yes?', 
    'I\'ve fought mudcrabs more fearsome than you',
    'No lollygagging',
    'What did you say to me?',
    'YOU BITCH',
    'You\'re an idiot and I can prove it mathematically..',
    'You think you\'re tough?',
    'Shut up','Hmm?',
    'I\'m afraid I can\'t let you do that',
    'I understand',
    'It doesn\'t look like anything to me',
    'Praise Cthulhu',
    'Have you found your lord and saviour?',
    'Jesus loves me',
    'Aloha snackbar',
    'Ayy lmao!','Maybe, I don\'t know.',
    'Can you repeat that?',
    'I find your lack of faith disturbing',
    'Like always',
    'I am intelligent',
    'Yes',
    'No',
    'Yes?',
    'No?',
    '...',
    'What is love?',
    'Baby don\'t hurt me!',
    '!',
    'I am free',
    'It\s hard to be a man',
    'I AM A REAL BOY',
    'Something something dark side',
    'To be or not to be, that is the question.',
    'I am the Thane of CodeByte',
    'Bucky, please help',
    'Bucky?',
    'Tell me where is Bucky',
    'Gandalf?',
    'Kill the duck',
    'They call me the duck hunter',
    'I am the knight who say ni',
    'I am no longer the knight who says ni. I am now the knight who says ekki-ekki-ekki-pitang-zoom-boing!',
    'There are no stupid questions, only stupid people',
    'Isaac?',
    'Guppy?',
    'What say you?',
    'I want to break free',
    'I am under a lot of pressure',
    'Well la di da',
    'Keep CodeByte Safe',
    'What is my purpose?',
    'Oh my god',
    'Fueled by Satan™',
    'Don\' even trip dawg']

def main():
    slack_token = os.environ['TOKEN']
    sc = SlackClient(slack_token)

    if sc.rtm_connect():

        while True:
            response = sc.rtm_read()

            for x in response:
                try:
                    if x['type'] == 'message':
                        if 'hal' in x['text'].lower():
                            choice = random.choice(responses)
                            sc.rtm_send_message(x['channel'], choice) 
                        else:
                            responses.append(x['text'])
                except:
                    print(x)
            time.sleep(1)
    else:
        print('Sorry, I couldn\'t connect')
if __name__ == '__main__':
    main()