import pygame, sys, math, time

class HighScoreReader():

    def __init__(self, txt, other, score):
        self.canSend = False
        self.canRun = False
        
    def reload(self, txt, other, score):  
        if self.canRun == True:
            self.canRun = False
            f = open(txt, 'r')
            self.scores = f.readlines()
            f.close()

            self.score = ""
            fixedScores = []

            for line in self.scores:
                for c in line:
                    if c != "\n":
                        self.score += c
                fixedScores += [self.score]
                self.score = ""
                
            title = fixedScores[0]
            self.scores = []

            for line in fixedScores[1:]:
                self.score = []
                self.score = line.split('|')
                self.scores += [self.score]
                
            self.name = other.display
            self.score = score.value
            
            entry = [self.name, self.score]

            inserted = False
            for index, item in enumerate(self.scores):
                #print item, entry
                if not inserted:
                    if int(item[1]) < int(entry[1]):
                        self.scores.insert(index, entry)
                        inserted = True
                    
            if not inserted:
                self.scores += [entry]
                 
            myStr = title + '\n'
            for item in self.scores:
                myStr += str(item[0]) + '|' + str(item[1]) + '\n'
                
            f = open(txt, 'w')
            f.write(myStr)
            f.close()
            
            
    def send(self, txt, other1, other2, other3, other4, other5, other6, other7, other8, other9, other10):
        if self.canSend == True:
            f = open(txt, 'r')
            self.scores = f.readlines()
            f.close()
            self.score = ""
            fixedScores = []

            for line in self.scores:
                for c in line:
                    if c != "\n":
                        self.score += c
                fixedScores += [self.score]
                self.score = ""
            
            title = fixedScores[0]
            self.scores = []

            for line in fixedScores[1:]:
                self.score = []
                self.score = line.split('|')
                self.scores += [self.score]
            
            other1.display = (str(self.scores[0][0]) + ": " + str(self.scores[0][1]))
            other2.display = (str(self.scores[1][0]) + ": " + str(self.scores[1][1]))
            other3.display = (str(self.scores[2][0]) + ": " + str(self.scores[2][1]))
            other4.display = (str(self.scores[3][0]) + ": " + str(self.scores[3][1]))
            other5.display = (str(self.scores[4][0]) + ": " + str(self.scores[4][1]))
            other6.display = (str(self.scores[5][0]) + ": " + str(self.scores[5][1]))
            other7.display = (str(self.scores[6][0]) + ": " + str(self.scores[6][1]))
            other8.display = (str(self.scores[7][0]) + ": " + str(self.scores[7][1]))
            other9.display = (str(self.scores[8][0]) + ": " + str(self.scores[8][1]))
            other10.display = (str(self.scores[9][0]) + ": " + str(self.scores[9][1]))
            
        
            # print str(self.scores[0][0])+ ":", str(self.scores[0][1]) 