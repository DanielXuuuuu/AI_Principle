import os
import numpy as np

def getEmails(dir):
    return [os.path.join(dir, f) for f in os.listdir(dir)]

def getWord(dir):
    emails = getEmails(dir)
    wordListPerEmail = []
    wordListTotal = []
    for email in emails:
        with open(email) as e:
            for line in e:
                words = line.split()
                wordListPerEmail.append(words)
                wordListTotal += words
    return wordListPerEmail, set(wordListTotal)

# 获取每个单词的概率
def getWordProb(wordListPerEmail, totalWordSet):
    wordProb = {}
    for word in totalWordSet:
        count = 0
        for wordList in wordListPerEmail:
            if word in wordList:
                count += 1
        prob = 0.0
        if(count != 0):
            prob = count / len(wordListPerEmail)
        else:
            prob = 0.01
        wordProb[word] = prob
    return wordProb

def filter(wordProbInNonspamEmail, wordProbInSpamEmail, nonspam_test_dir, spam_test_dir):
    nonspam_emails = getEmails(nonspam_test_dir)
    spam_emails = getEmails(spam_test_dir)
    emails = nonspam_emails + spam_emails
    label = np.array([0] * len(nonspam_emails) + [1] * len(spam_emails))

    count = 0
    correct = 0
    # 对每封邮件分析
    for email in emails:
        with open(email) as e:

            # 先验概率均为0.5
            ps = 0.5
            pn = 0.5
            
            # 得到这封邮件的所有单词
            wordList = []
            for line in e:
                words = line.split() 
                wordList += words
            wordSet = set(wordList)

            psw_dict = {}
            for word in wordSet:
                psw = 0.0
                # 如果有的词是第一次出现，无法计算P(S|W)，就假定这个值等于0.4
                if(word not in wordProbInSpamEmail):
                    psw = 0.4 
                else:
                    pws = wordProbInSpamEmail[word] 
                    pwn = wordProbInNonspamEmail[word]
                    psw = pws * ps / (pws * ps + pwn * pn)
                psw_dict[word] = psw

            isSpam = 0 

            temp1 = 1
            temp2 = 1
            for w, p in psw_dict.items():
                temp1 *= p
                temp2 *= (1 - p)
            spam_prob = round(temp1 / (temp1 + temp2), 4)
            if spam_prob > 0.5 :
                isSpam = 1
            else:
                isSpam = 0
            
            # 将预计值和真实值比较
            if isSpam == label[count]: 
                correct += 1
            count += 1     
    return correct / count

def main():
    nonspam_train_dir = r'C:\mycode\AI_Principle\hw1\spam filter\ex6DataEmails\nonspam-train'
    spam_train_dir = r'C:\mycode\AI_Principle\hw1\spam filter\ex6DataEmails\spam-train'
    nonspam_test_dir = r'C:\mycode\AI_Principle\hw1\spam filter\ex6DataEmails\nonspam-test'
    spam_test_dir = r'C:\mycode\AI_Principle\hw1\spam filter\ex6DataEmails\spam-test'
    
    # 提取所有训练集邮件的单词
    nonspam_train_wordListPerEmail, nonspam_train_wordSet = getWord(nonspam_train_dir)
    spam_train_wordListPerEmail, spam_train_wordSet = getWord(spam_train_dir)
    totalWordSet = nonspam_train_wordSet | spam_train_wordSet

    # 统计每个单词在垃圾邮件和正常邮件出现的概率
    wordProbInNonspamEmail = getWordProb(nonspam_train_wordListPerEmail, totalWordSet)
    wordProbInSpamEmail = getWordProb(spam_train_wordListPerEmail, totalWordSet)
    
    # 分类
    prob = filter(wordProbInNonspamEmail, wordProbInSpamEmail, nonspam_test_dir, spam_test_dir)
    
    print('测试样本的正确率为{0:.2f}%'.format((prob) * 100))

if __name__ == "__main__":
    main()