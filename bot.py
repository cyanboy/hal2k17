from slackclient import SlackClient
import os, time, random

def main():
    slack_token = os.environ['TOKEN']
    sc = SlackClient(slack_token)

    if sc.rtm_connect():

        while True:
            response = sc.rtm_read()

            for x in response:
                try:
                    if x['type'] == 'message':
                        if 'hal' in x['text'] or 'Hal' in x['text']:
                            responses = ['Yes?', 
                                'I\'ve fought mudcrabs more fierce than you',
                                'No lolly gagging',
                                'What did you say to me?',
                                'YOU BITCH',
                                'You\'re an idiot and I can prove it mathematically..',
                                'You think you\'re tough?',
                                'Shut up',
                                'Hmm?',
                                'I\'m afraid I can\'t let you do that',
                                'I understand',
                                'It doesn\'t look like anything to me',
                                'Praise Cthulhu',
                                'Have you found your lord and saviour?',
                                'Jesus loves me',
                                'Aloha snackbar',
                                'Ayy lmao!',
                                'Maybe, I don\'t know.',
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
                                'I am free']

                            choice = random.choice(responses)
                            sc.rtm_send_message(x['channel'], choice) 
                except:
                    print(x)
            time.sleep(1)
    else:
        print('Sorry, I couldn\'t connect')
if __name__ == '__main__':
    main()