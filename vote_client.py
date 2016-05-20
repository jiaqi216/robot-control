import requests
import signal
TIMEOUT = 5 #num seconds for timeout

OPTIONS = {
    'w':'U',
    'a':'L',
    's':'D',
    'd':'R'
}

def interrupted(signum, frame):
    print '\nsorry, time\'s up!'
    print 'press enter to continue'
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
        print ' You have 5 seconds to vote...'
        vote = raw_input('enter w (forward), a (left), s (backward), d (right)')
        if vote.lower() not in 'wasd':
            print 'invalid entry'
        else:
            return vote
    except:
        return None


prev_id=0
while True:
  r = requests.get('http://localhost:8000/sessions/0/')
  data=r.json()
  session_id=data['id']
  if session_id == prev_id:
      continue
  prev_id=session_id
  print 'Move Number: '+str(session_id)
  signal.alarm(TIMEOUT)
  v = input()
  signal.alarm(0)
  if v is not '':
      cast_vote = requests.post('http://localhost:8000/votes/', data={"robot":1, "session":session_id,"vote":OPTIONS[v.lower()], "username":1})