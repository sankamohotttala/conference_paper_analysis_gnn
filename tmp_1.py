import re


keywords = ['graph','a mathematical disability,']

text = 'this paper aims to diagnose childrens with specific learning disabilities and provide treatments via a mobile game. learning disabilities are neurological disorders that affect the brain. children with learning disabilities have trouble with learning compared to their fellow peers and quite often fall back academically since a majority of them go undiagnosed. the specific learning disabilities for which this paper provides screening are dyslexia a reading disability, dyscalculia a mathematical disability, letter dysgraphia and numeric dysgraphia are both writing disabilities. deep learning and machine learning techniques are used in the screening process of these specific learning disabilities. trained convolutional neural networks are used to detect the spoken letter/word, detect the written letter/word and detect the written number on the mobile application. outputs from the convolutional neural network are fed into the models used for screening learning disabilities. the machine learning algorithms used in building the models include k-nearest neighbors, random forest and support vector machine. screening results from the models built in this research provided an accuracy of 89%, 90%, 92%, 92% for dyslexia, letter dysgraphia, dyscalculia and numeric dysgraphia respectively. this is the first game based screening and intervention tool for dyslexia, letter dysgraphia, dyscalculia and numeric dysgraphia.'
for keyword in keywords:
    pattern = r'\b' + re.escape(keyword) + r'\b' 
    if re.search(pattern, text):
        print(f"The word '{keyword}' exists in the string.")
    else:
        print(f"The word '{keyword}' does not exist in the string.")
