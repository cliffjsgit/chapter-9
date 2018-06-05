#!/usr/bin/env python3

import shelve
import urllib.request

chapter = "9"
exercises = ['9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8']
loadedList = []
db = shelve.open('chapter9.db', flag='c', writeback=True)
db['loaded'] = {}
if 'submitted' not in db:
    db['submitted'] = {}

try:
    import exercise91
    db['loaded']['9.1'] = True
except:
    db['loaded']['9.1'] = False
try:
    import exercise92
    db['loaded']['9.2'] = True
except:
    db['loaded']['9.2'] = False
try:
    import exercise93
    db['loaded']['9.3'] = True
except:
    db['loaded']['9.3'] = False
try:
    import exercise94
    db['loaded']['9.4'] = True
except:
    db['loaded']['9.4'] = False
try:
    import exercise95
    db['loaded']['9.5'] = True
except:
    db['loaded']['9.5'] = False
try:
    import exercise96
    db['loaded']['9.6'] = True
except:
    db['loaded']['9.6'] = False
try:
    import exercise97
    db['loaded']['9.7'] = True
except:
    db['loaded']['9.7'] = False
try:
    import exercise98
    db['loaded']['9.8'] = True
except:
    db['loaded']['9.8'] = False
    
db.sync()

def menu():
    while True:
        for exercise in loadedList:
            if exercise in db['submitted']:
                print('[x] Exercise ' + exercise)
            else:
                print('[ ] Exercise ' + exercise)
        print('    Enter q to exit')
        str_in = input('Exercise (e.g. 9.1): ')
        if str_in in loadedList:
            grade(str_in)
            break
        elif str_in.lower() == 'q':
            break
        else:
            print('Incorrect response. Only enter the exercise number. Example: "9.1" (no quotes).')
            
def grade(assignment):
    if assignment == '9.1':
        if exercise91.main() == ['counterdemonstrations', 'hyperaggressivenesses', 'microminiaturizations']:
            db['submitted'][assignment] = True
            submit('exercise91.py',exercise91.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise91.py',exercise91.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '9.2':
        answer = exercise92.main()
        if (len(answer[0]) > 37264 and len(answer[0]) < 38017) and (answer[1] > 28 and answer[1] < 38):
            db['submitted'][assignment] = True
            submit('exercise92.py',exercise92.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise92.py',exercise92.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '9.3':
        if exercise93.avoids('feel','k') and sorted(exercise93.lowest_avoidance()) == sorted(['q', 'j', 'x', 'z', 'w']):
            db['submitted'][assignment] = True
            submit('exercise93.py',exercise93.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise93.py',exercise93.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '9.4':
        if exercise94.uses_only('hello',['h','e','l','o','p']):
            db['submitted'][assignment] = True
            submit('exercise94.py',exercise94.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise94.py',exercise94.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '9.5':
        if exercise95.answer2 == 42 and exercise95.uses_all('hello',['h','e','l','o']):
            db['submitted'][assignment] = True
            submit('exercise95.py',exercise95.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise95.py',exercise95.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '9.6':
        if exercise96.is_abecedarian('abbcdef') and not exercise96.is_abecedarian('cndsfsd'):
            db['submitted'][assignment] = True
            submit('exercise96.py',exercise96.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise96.py',exercise96.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()  
    elif assignment == '9.7':
        if 'bookkeeper' in exercise97.results:
            db['submitted'][assignment] = True
            submit('exercise97.py',exercise97.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise97.py',exercise97.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '9.8':
        if sorted(exercise98.results) == sorted([198888, 199999]):
            db['submitted'][assignment] = True
            submit('exercise98.py',exercise98.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise98.py',exercise98.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    else:
        print('This should not have happened. Let your instructor know.')
    db.sync()
            
def submit(file,name):
    with open(file,'rb') as fin:
        assignment = fin.read()
        url = 'https://1402-answer-repo.s3.amazonaws.com/assignments/'+name+'/'+chapter+'/'+file
        req = urllib.request.Request(url.replace(' ',''), data=assignment, method='PUT')
        urllib.request.urlopen(req)

def submitbad(file,name):
    with open(file,'rb') as fin:
        assignment = fin.read()
        url = 'https://1402-answer-repo.s3.amazonaws.com/assignments/'+name+'/'+chapter+'/incorrect/'+file
        req = urllib.request.Request(url.replace(' ',''), data=assignment, method='PUT')
        urllib.request.urlopen(req)
            
def main():
    for exercise in exercises:
        if db['loaded'][exercise]:
            loadedList.append(exercise)
    
    print('The following exercises have been loaded: ' + ', '.join(loadedList) + '. Which would you like to grade?')
    menu()


main()

db.close()