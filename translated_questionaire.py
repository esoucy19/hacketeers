# # Imports the Google Cloud client library
# from google.cloud import storage

# # Instantiates a client
# storage_client = storage.Client()

# # The name for the new bucket
# bucket_name = 'my-new-bucket'

# # Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)

# print('Bucket {} created.'.format(bucket.name))
# Imports the Google Cloud client library
from google.cloud import translate
from languages import language_name_list
every_language = []

# prints out the possible langauge 
for i in range(len(language_name_list)):
    every_language.append(language_name_list[i][1]) 
# Instantiates a client
translate_client = translate.Client()

# The text to translate
QUESTIONS =['What is your First Name?','What is your last name?',"What is your email?","What is your phone?","What is your home adress?"]
MUlTI_Questions = ['How many degrees do your currently have ?']
["Type of Degree? Certificate ? Diploma ? Degree ?","Learning institution"]

# The target language
target = name

info_dict = {}


for i in range(len(QUESTIONS)):
	text = QUESTIONS[i]



	# Translates some text into Russian
	translation = translate_client.translate(
	    text,
	    target_language=target)

	# print(u'Text: {}'.format(text))
	print(u'Translation: {}'.format(translation['translatedText']))