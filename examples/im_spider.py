#import urllib2
#from datatime import datatime
from SPARQLWrapper import SPARQLWrapper, JSON
from openpyxl import Workbook
import json




sparql = SPARQLWrapper("http://dbpedia.org/sparql")
def book_f(a_name):
    book_sel="""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    
    select distinct ?bookURI ?bookName ?authorName 
                         ?authorMovement ?bookGenre ?bookAbstract 
                         where { ?bookURI rdf:type dbo:Book . 
                                ?bookURI  dbo:author ?author .
                                ?bookURI  dbo:abstract ?bookAbstract .  
                                ?bookURI rdfs:label ?bookName .
                                ?author rdfs:label ?authorName . 
                          FILTER (lang(?authorName) = \"en\"  && lang(?bookName) = \"en\" && 
            lang(?bookAbstract) = \"en\" && regex((?authorName),"%s")).
                           }
                        """%(a_name)
    return book_sel
def film_f(a_name):
    film_sel="""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    select distinct ?bookURI ?bookName ?authorName 
                          ?bookAbstract 
                         where { ?bookURI rdf:type dbo:Film . 
                                ?bookURI  dbo:director ?author .
                                ?author rdfs:label ?authorName .
                                ?bookURI  dbo:abstract ?bookAbstract . 
                                ?bookURI rdfs:label ?bookName .
                                                                 
                           FILTER (lang(?authorName) = \"en\"  && lang(?bookName) = \"en\" && 
            lang(?bookAbstract) = \"en\" && regex((?authorName),"%s")).
                           }
                        """%(a_name)
    return  film_sel
def game_f(a_name):
    game_sel = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    select distinct ?bookURI ?bookName ?authorName 
                          ?bookAbstract 
                         where { ?bookURI rdf:type dbo:Game . 
                                ?bookURI  dbo:genre ?author .
                                ?author rdfs:label ?authorName .
                                ?bookURI  dbo:abstract ?bookAbstract . 
                                ?bookURI rdfs:label ?bookName .

            FILTER (lang(?authorName) = \"en\"  && lang(?bookName) = \"en\" && 
            lang(?bookAbstract) = \"en\" && regex((?authorName),"%s")).
                           }
                        """%(a_name)
    return  game_sel
#英语的过滤语言的简写是EN,在这里中文语言是ZH,FILTER是一个过滤器
def spider( kind,name):
    aa_sel=""
    return_list=[]
    if kind!=None:
        if kind=="1":
            aa_sel=film_f(name)
        elif kind=="2":
            aa_sel=game_f(name)
        elif kind=="3":
            aa_sel=book_f(name)
    print(aa_sel)
    sparql.setQuery(aa_sel)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    #result_1=JSON.dumps(results)
   # with open("results.txt","w",encoding="utf-8") as f:
    #    f.write(str(results))
   # print(results)
   # URI_list=[]
    #name_list=[]
    #author_name_list=[]
   # author_movement_list=[]
   # genre_list=[]#语言
   # abst_list=[]
    for result in results["results"]["bindings"]:

       # URI_list .append(result["bookURI"]["value"])
       # name_list.append(result["bookName"]["value"])
       # author_name_list.append(result["authorName"]["value"])
       # author_movement_list.append(result["authorMovement"]["value"])
       # genre_list.append(result["genre"]["value"])
       # abst_list.append(result["bookAbstract"]["value"])
        cell = {}
        cell['Urll']=result["bookURI"]["value"]
        cell['TiteName'] = result["bookName"]["value"]
        cell['authorName'] = result["authorName"]["value"]
        cell['bookAbstract']=result["bookAbstract"]["value"]
        #cell['authorMovement'] = result["authorMovement"]["value"]
        #cell['genre'] = result["genre"]["value"]
        print("TiteName:"+ cell['TiteName']+'****authorName'+cell['authorName']+'****Url'+cell['Urll']+'****abstract'+cell["bookAbstract"])
        return_list.append(cell)
    json_str = json.dumps(return_list)
    print(json_str)
    return json_str
    #wb = Workbook()
    #sheet = wb.active
   # sheet.title = "filmdatabase"
   # sheet['A1'] = "uri"
  #  sheet['B1'] = "name"
   # sheet['C1'] = "author_name"
   # sheet["D1"]="author_movement"
  #  sheet["E1"]="genre"
  #  sheet["F1"]="abstract"
   # for i in range(1, len(URI_list) + 1):
   #     sheet["A%d" % (i + 1)].value = str(URI_list[i - 1])
  #      sheet["B%d" % (i + 1)].value = str(name_list[i - 1])
  #      sheet["C%d" % (i + 1)].value = str(author_name_list[i - 1])
   #     sheet["D%d" % (i + 1)].value = str(author_movement_list[i-1])
  #      sheet["E%d" % (i + 1)].value = str(genre_list[i - 1])
   #     sheet["F%d" % (i + 1)].value = str(abst_list[i - 1])
   # wb.save('filmdatabase.xlsx')
