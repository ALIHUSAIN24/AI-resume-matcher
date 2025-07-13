import re

def clean_description(text):
    text = re.sub(r'\s+',' ', text)
    text = re.sub(r'[^\w\s\.,()-/+]', '',text)
    return text.strip()

if __name__ =="__main__":
    samplid = '''
    we are looking for python developer &&&& with experience in machine learning, react.js and cloud deployment.
    Skills required are: python, react, mysql, git, flask or django, APIs.
    '''
    clnd = clean_description(samplid)
    print("cleaned JD:\n", clnd)