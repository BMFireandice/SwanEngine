from flask import Flask, render_template, request
from searchingMethods import * 

app = Flask(__name__) 

pageNum = 0
query = ""

@app.route('/')
def welcome():
  return render_template('index.html') # loads the main menu

@app.route('/settings', methods=['GET'])
def settings():
  return render_template('settings.html') # loads the settings page
  
@app.route('/about-me', methods=['GET'])
def aboutMe():
  return render_template('about-me.html') # loads the page describing my project
     
@app.route('/search_results', methods=['GET']) 
def searchFunction(): 

  global query 
  global pageNum
  pageNum = 0
  query = request.args.get('query') # saves the query entered by the user
  
  results = searchLink(query, pageNum)
  resultsTitles = searchTitles(query, pageNum)
  resultsMinorText = searchMinorText(query, pageNum)
  resultsAuthors = searchAuthor(query, pageNum) # runs the functions to scrape Scholar for the results 


  return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum, resultsAuthors=resultsAuthors) # loads the search results page
    
@app.route('/next_page', methods=['GET']) 
def nextPage():

  global pageNum

  pageNum += 10

  results = searchLink(query, pageNum)
  resultsTitles = searchTitles(query, pageNum)
  resultsMinorText = searchMinorText(query, pageNum)
  resultsAuthors = searchAuthor(query, pageNum) # runs the functions to scrape Scholar for the results 


  return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum, resultsAuthors=resultsAuthors) # loads the search results page 

@app.route('/last_page', methods=["GET"])
def previousPage():
  global pageNum
  
  if (pageNum - 10) >= 0: # the page number cannot be negative, so this checks to see if the page number is not 0 or less

    pageNum -= 10
    results = searchLink(query, pageNum)
    resultsTitles = searchTitles(query, pageNum)
    resultsMinorText = searchMinorText(query, pageNum)
    resultsAuthors = searchAuthor(query, pageNum) # runs the functions to scrape Scholar for the results 

    return render_template('searchResults.html', query=query, results=results, resultsTitles=resultsTitles, resultsMinorText=resultsMinorText, pageNum=pageNum, resultsAuthors=resultsAuthors) # loads the search results page

if __name__ == '__main__':

  app.run(debug=True) # starts the server
