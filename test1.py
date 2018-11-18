# questions.py
from questionnaire import Questionnaire
# q = Questionnaire()

# q.one('day', 'monday', 'friday', 'saturday', prompt='What day is it?')
# q.one('time', ('morning', 'in the morning'), ('night', 'at night'), prompt='What time is it?')

# q.run()
# print(q.format_answers())

from languages import every_language,language_name_list
from google.cloud import *

q = Questionnaire()
q.one("What is your language", 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')

q.run()
a = q.format_answers(fmt='plain');
a = a.split(" ")

abbreviated_language = language_name_list[every_language.index(a[-1])][0]

# Instantiates a client
translate_client = translate.Client() 


# Translates Quetionire into desired language
# translation = translate_client.translate(text,target_language=abbreviated_language)


print(translate_client.translate('What is your First Name?',target_language=abbreviated_language)['translatedText'])

q = Questionnaire()
q.raw(translate_client.translate('First Name',target_language=abbreviated_language)['translatedText'], prompt= translate_client.translate('What is your First Name?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate('Last Name',target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your Last Name?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Email",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your email? ',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("City",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What city?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Phone",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your phone number?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Street address",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your street address?',target_language=abbreviated_language)['translatedText'])
q.one(translate_client.translate("Highest level of Education?",target_language=abbreviated_language)['translatedText'], translate_client.translate('Degree',target_language=abbreviated_language)['translatedText'], translate_client.translate('Certificate',target_language=abbreviated_language)['translatedText'],translate_client.translate("Diploma",target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("City",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What city is your Education from?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Year Attended",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What year did you attend?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Year Graduated",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What year did you Graduate?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Experience",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('Give a short description of what you learned',target_language=abbreviated_language)['translatedText'])
q.one(translate_client.translate("Do you have volunteer experience?",target_language=abbreviated_language)['translatedText'], translate_client.translate("yes",target_language=abbreviated_language)['translatedText'], translate_client.translate("no",target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("Name of organization?",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What year did you Graduate?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("City/province/country",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('City, province, country where you volunteered ?',target_language=abbreviated_language)['translatedText'])

q.run()
print(q.format_answers(fmt='array'))

# q.raw("Number of degrees","Name of learning institution? ")

# q.run()
# print(q.format_answers(fmt='array'))

# q.many('activities', 'tacos de pastor', 'go to cantina', 'write code').condition(('time', 'night'))
# q.many('activities', 'barbacoa', 'watch footy', 'walk dog').condition(('day', 'saturday'), ('time', 'morning'))
# q.many('activities', 'eat granola', 'get dressed', 'go to work').condition(('time', 'morning'))

# q.run()
# print(q.format_answers(fmt='array'))
# q = Questionnaire(show_answers=False, can_go_back=False)
# q.raw('What is your name', prompt='Username:')

# q.run()
# print(q.format_answers(fmt='array'))
