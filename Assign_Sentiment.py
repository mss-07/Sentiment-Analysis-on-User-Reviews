import xlsxwriter
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#This function writes the sentiment score for each text review in a excel file
#Prints the individual counts for each sentiment categories
def evaluate_sentence_sentiment(readFile, writeFile):
    read_path = "Cleaned Data\Sentiment\\"+ readFile
    write_path = "Cleaned Data\Sentiment\\"+ writeFile
    df = pd.read_excel(read_path)
    wb = xlsxwriter.Workbook(write_path)
    ws = wb.add_worksheet()
    
    sentiment = SentimentIntensityAnalyzer()
    i = 1
    neg = pos = neu = 0

    for text in df['Text']:
        #calculate the compound score
        compound_score = sentiment.polarity_scores(text)['compound']
        if(compound_score <= -0.05):
            sentiment_score = '-1'
            neg += 1
        elif(compound_score > -0.05 and compound_score < 0.05):
            sentiment_score = '0'
            neu += 1
        else:
            sentiment_score = '1'
            pos += 1            
        ws.write(i,0,text) #write the textual review in the write file
        ws.write(i,1,sentiment_score) #write the sentiment score of the review in the write file
        i += 1

    print("Neg: ",neg, "Neu: ",neu, "Pos: ",pos)
    wb.close()  

evaluate_sentence_sentiment('cleaned_data.xlsx','polarized_data.xlsx')
