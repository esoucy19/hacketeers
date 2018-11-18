# questions.py

from questionnaire import Questionnaire
from languages import every_language, language_name_list
from google.cloud import *
from generator import generate

q = Questionnaire()
q.one("What is your language", 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
q.run()
a = q.format_answers(fmt='plain');
a = a.split(" ")

#language of choice
abbreviated_language = language_name_list[every_language.index(a[-1])][0]

# Instantiates a client
translate_client = translate.Client() 


# Translates Quetionire into desired language
# translation = translate_client.translate(text,target_language=abbreviated_language)

q = Questionnaire()
q.raw(translate_client.translate('first_name',target_language=abbreviated_language)['translatedText'], prompt= translate_client.translate('What is your First Name?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate('last_name',target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your Last Name?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("email",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your email? ',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("phone_number",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your phone number?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("address_line_1",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is your street address?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("city",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What city?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("country",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What country?',target_language=abbreviated_language)['translatedText'])
q.raw(translate_client.translate("postal_code",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('postal code?',target_language=abbreviated_language)['translatedText'])
q.run()

PART_ONE = q.format_answers(fmt='array')
PART_ONE = "PART_ONE = " + q.format_answers(fmt='array')
exec(PART_ONE)


qu = Questionnaire()
qu.raw(translate_client.translate("schools",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('Number of schools attended?',target_language=abbreviated_language)['translatedText'])
qu.run()

PART_TWO = "PART_TWO = " + qu.format_answers(fmt='array')
exec(PART_TWO)

try:
    num1 = int(PART_TWO[0][1])
    que = Questionnaire()
    for i in range(num1):
        que.one(translate_client.translate("degree",target_language=abbreviated_language)['translatedText'], translate_client.translate('Certificate',target_language=abbreviated_language)['translatedText'], translate_client.translate('Diploma',target_language=abbreviated_language)['translatedText'],translate_client.translate("Bachelors",target_language=abbreviated_language)['translatedText'],translate_client.translate("Masters",target_language=abbreviated_language)['translatedText'],translate_client.translate("PhD",target_language=abbreviated_language)['translatedText'])
        que.raw(translate_client.translate("name",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('Name of institute?',target_language=abbreviated_language)['translatedText'])
        que.raw(translate_client.translate("start_year",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What year did you attend?',target_language=abbreviated_language)['translatedText'])
        que.raw(translate_client.translate("end_year",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What year did you Graduate?',target_language=abbreviated_language)['translatedText'])
        que.raw(translate_client.translate("department",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is the program of study?',target_language=abbreviated_language)['translatedText'])

except:
    print("Number only, " + translate_client.translate('number only',target_language=abbreviated_language)['translatedText'])

que.run()
PART_THREE = "PART_THREE = " + que.format_answers(fmt='array')
exec(PART_THREE)



ques = Questionnaire()
ques.raw(translate_client.translate("Numbers of Jobs Previously Held",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('Number of jobs previously Held?',target_language=abbreviated_language)['translatedText'])
ques.run()
PART_FOUR = "PART_FOUR = " + ques.format_answers(fmt='array')
exec(PART_FOUR)


try:
    PART_FOUR = int(PART_FOUR[0][1])
    quest = Questionnaire()
    for i in range(PART_FOUR):
        quest.raw(translate_client.translate("position",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('what is the job title? ',target_language=abbreviated_language)['translatedText'])
        quest.raw(translate_client.translate("start_date",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('what is the start year?',target_language=abbreviated_language)['translatedText'])
        quest.raw(translate_client.translate("end_date",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('what is the end year?',target_language=abbreviated_language)['translatedText'])
        quest.raw(translate_client.translate("institution",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is the company name?',target_language=abbreviated_language)['translatedText'])
        quest.raw(translate_client.translate("task",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('give a brief description of your responsibilities',target_language=abbreviated_language)['translatedText'])

except:
    print("Number only, " + translate_client.translate('number only',target_language=abbreviated_language)['translatedText'])


quest.run()
quest.format_answers(fmt='array')
PART_FIVE = "PART_FIVE = " + quest.format_answers(fmt='array')
exec(PART_FIVE)

questi = Questionnaire()
questi.many("Choose the languages you speak", 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')

questi.run()
PART_SIX = questi.format_answers(fmt='array')
PART_SIX = "PART_SIX = " + questi.format_answers(fmt='array')
exec(PART_SIX)






questio = Questionnaire()
questio.raw(translate_client.translate("Numbers of Volunteer Experiences Previously Held",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('Number of Volunteer Positions previously Held?',target_language=abbreviated_language)['translatedText'])
questio.run()
PART_SEVEN = "PART_SEVEN = " + questio.format_answers(fmt='array')
exec(PART_SEVEN)




try:
    PART_SEVEN = int(PART_SEVEN[0][1])
    question = Questionnaire()
    for i in range(PART_SEVEN):
        question.raw(translate_client.translate("date",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('what are the years?',target_language=abbreviated_language)['translatedText'])
        question.raw(translate_client.translate("institution",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('What is the company name?',target_language=abbreviated_language)['translatedText'])
        question.raw(translate_client.translate("role",target_language=abbreviated_language)['translatedText'],prompt=translate_client.translate('what is the your role?',target_language=abbreviated_language)['translatedText'])

except:
    print("Number only, " + translate_client.translate('number only',target_language=abbreviated_language)['translatedText'])


question.run()
PART_EIGHT = "PART_EIGHT = " + question.format_answers(fmt='array')
exec(PART_EIGHT)


ALL = dict(PART_ONE)  # + PART_THREE + PART_FIVE
ALL["languages"] = PART_SIX[0][1]
ALL['schools'] = [dict(PART_THREE)]
ALL['jobs'] = [dict(PART_FIVE)]
ALL['jobs'][0]['tasks'] = [ALL['jobs'][0]['task']]
ALL['volunteer_experiences'] = [dict(PART_EIGHT)]

print(ALL)

# generate(ALL)
