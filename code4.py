import pyttsx3
engine = pyttsx3.init()
a=("NIELIT offers a variety of formal courses in  "
   "different fields, with a duration of 3 years for its Diploma  "
   "courses. Admission to these courses is based on the candidate’s "
   " academic merit in their previous qualifying examination. For Diploma "
   "in Engineering and BCA, candidates have to apply online or"
   " offline with their academic details and submit the N...")
engine.say("a")
print(type(a))
engine.runAndWait()


