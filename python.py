from flask import Flask, render_template, request
from searchingMethods import * 

app = Flask(__name__)

pageNum = 0
query = ""

@app.route('/')
def welcome():
  return render_template('index.html')

@app.route('/settings', methods=['GET'])
def settings():
  return render_template('settings.html')
  
@app.route('/about-me', methods=['GET'])
def aboutMe():
  return render_template('about-me.html')
     
@app.route('/search_results', methods=['GET']) 
def searchFunction(): 

  global query 
  global pageNum
  pageNum = 0
  query = request.args.get('query')
  
  results = searchLink(query, pageNum)
  resultsTitles = searchTitles(query, pageNum)
  resultsMinorText = searchMinorText(query, pageNum)
  resultsAuthors = searchAuthor(query, pageNum)

#if results.len() == 0
##
#attempt_a_solve()
##
#results = searchLink(query, pageNum)


  return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum, resultsAuthors=resultsAuthors)
    
@app.route('/next_page', methods=['GET']) 
def nextPage():

  global pageNum

  pageNum += 10

  results = searchLink(query, pageNum)
  resultsTitles = searchTitles(query, pageNum)
  resultsMinorText = searchMinorText(query, pageNum)
  resultsAuthors = searchAuthor(query, pageNum)


  return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum, resultsAuthors=resultsAuthors)

@app.route('/last_page', methods=["GET"])
def previousPage():
  global pageNum
  
  if (pageNum - 10) >= 0:

    pageNum -= 10
    results = searchLink(query, pageNum)
    resultsTitles = searchTitles(query, pageNum)
    resultsMinorText = searchMinorText(query, pageNum)
    resultsAuthors = searchAuthor(query, pageNum)

    return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum, resultsAuthors=resultsAuthors)
  """else:
    results = searchLink(query, pageNum)
    resultsTitles = searchTitles(query, pageNum)
    resultsMinorText = searchMinorText(query, pageNum)
    return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum)"""



if __name__ == '__main__':

  app.run(debug=True)