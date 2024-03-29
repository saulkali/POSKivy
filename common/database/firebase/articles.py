from common.firebase.firebase import FireBase
from common.firebase import constants as firebaseConstants
from common.entities.article_entity import ArticleEntity


firebase = FireBase()

def getAllArticles()->list[ArticleEntity]:
    '''get all articles ->list type ArticleEntity'''
    listArticles = []
    articlesJson = firebase.db.child(firebaseConstants.referenceArticle).get()
    if  articlesJson != None:
        for key, value in articlesJson.items():
            articleEntity = ArticleEntity.parse_obj(value)
            articleEntity.id = key
            listArticles.append(articleEntity)
    return listArticles

def saveArticle(article:ArticleEntity):
    '''set new article'''
    firebase.db.child(firebaseConstants.referenceArticle).child(article.id).set(article.dict())

def updateArticle(article:ArticleEntity)->bool:
    try:
        firebase.db.child(firebaseConstants.referenceArticle).child(article.id).update(article.dict())
        return True
    except:
        return False
def deleteArticle(article:ArticleEntity)->bool:
    try:
        firebase.db.child(firebaseConstants.referenceArticle).child(article.id).delete()
        return True
    except:
        return False
def getArticleById(codeBar:str) -> ArticleEntity:
    articleJson = firebase.db.child(firebaseConstants.referenceArticle).child(codeBar).get()
    if articleJson != None:
        article = ArticleEntity.parse_obj(articleJson)
        return article
    return None

def deleteAmountArticle(codeBar:str,amount:float) -> bool: 
    try:
        articleJson = firebase.db.child(firebaseConstants.referenceArticle).child(codeBar).get()
        if articleJson != None:
            article = ArticleEntity.parse_obj(articleJson)
            article.amount -= amount
            firebase.db.child(firebaseConstants.referenceArticle).child(article.id).update({"amount":article.amount})
            return True
        return False
    except:
        return False
def existsArticle(codeBar:str)->bool:
    article = firebase.db.child(firebaseConstants.referenceArticle).child(codeBar).get()
    if article == None:
        return False
    return True