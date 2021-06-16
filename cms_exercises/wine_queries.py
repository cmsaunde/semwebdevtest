"""
Description
This code reads in the wine ontology and interogates it

Created by Carla Saunders
15 June 2021
"""

def load_wines():
    """
    Create an graph and load in the wine ontology
    """
    import rdflib
    g = rdflib.Graph()
    g.parse("../src/resources/wine.owl", format="xml")
    wine = rdflib.Namespace("http://www.semanticweb.org/davidos/ontologies/2020/9/untitled-ontology-21#")
    owl = rdflib.Namespace("http://www.w3.org/2002/07/owl#")
    rdfs = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
    
    return g, wine, owl, rdfs

def query_single_class(ont_class, g, wine, rdfs):
    """
    Takes a class, graph, and two namespaces and resturns a SPARQLResult object with all subclasses in that class
    """

    qres = g.query(
        """SELECT DISTINCT ?subclass
           WHERE {
             ?subclass rdfs:subClassOf wine:ont_class .
           }""".replace('ont_class', ont_class), initNs={ 'wine': wine })
    return qres

def qres_to_list(qres):
    """
    Takes a SPARQLResult object and resturns a list, removing the IRI
    """
    wine_str = "http://www.semanticweb.org/davidos/ontologies/2020/9/untitled-ontology-21#"
    result_list = []

    for row in qres:
        IRI = "%s" % row
        result = IRI.replace(wine_str," ")
        result_list.append(result)

    result_list = sorted(result_list)
 
    return result_list

def list_regions():
    """
    Returns a list of all instances of :region within wine.owl
    """
    # Load in the graph and namespaces
    g, wine, owl, rdfs = load_wines()
    
    qres = g.query(
        """SELECT DISTINCT ?region
           WHERE {
             ?region a wine:region .
           }""", initNs={ 'wine': wine })

    result_list = qres_to_list(qres)
    return result_list

def list_varietals():
    """
    Returns a list of all subclasses of :varietal within wine.owl
    """
    # Load in the graph and namespaces
    g, wine, owl, rdfs = load_wines()
    
    qres = query_single_class('varietal', g, wine, rdfs)
    result_list = qres_to_list(qres)
    return result_list

def list_classes_of_wines():
    """
    Returns a list of all subclasses of :wine within wine.owl
    """
    # Load in the graph and namespaces
    g, wine, owl, rdfs = load_wines()
    
    qres = query_single_class('wine', g, wine, rdfs)
    result_list = qres_to_list(qres)
    return result_list

def query_wines(colour=None, varietal=None, region=None):
    """
    Takes three optional agrments or the wine color, grape the wine was made from, and region the wine was produced in. Queries the ontology for any subclasses of wine which match the inputs. Returns a list of these wine subclasses and any instances within them.
    """
    # Load in the graph and namespaces
    g, wine, owl, rdfs = load_wines()

    query_string = """SELECT ?x
	   WHERE { 
       	     ?x rdfs:subClassOf wine:wine"""

    if colour != None:
        new_str = """,
                            [ owl:onProperty wine:has_color ;
                              owl:someValuesFrom wine:C
                            ]""".replace('C',colour)
        query_string = query_string + new_str 
    if varietal != None:
        new_str = """,
                            [ owl:onProperty wine:made_from ;
                              owl:someValuesFrom wine:Var
                            ]""".replace('Var',varietal)
        query_string = query_string + new_str 
    if region != None:
        new_str = """,
                            [ owl:onProperty wine:grown_in ;
                              owl:hasValue wine:R
                            ]""".replace('R',region)
        query_string = query_string + new_str 
    
    query_string = query_string + """
}"""
    
    qres = g.query(
        query_string, initNs={ 'wine': wine , 'owl': owl, 'rdfs': rdfs})

    result_list = qres_to_list(qres)

    if len(result_list) > 0:  
        for wineClass in result_list:
            wineClass = wineClass.replace(' ','')

            query_string = """SELECT ?wineIndividual
                   WHERE {
                     ?wineIndividual ?x wine:wineClass .
               }""".replace('wineClass', wineClass)

            qres = g.query(
                query_string, initNs={ 'wine': wine })

            new_wine = qres_to_list(qres)

            if len(new_wine) > 0:
                result_list  = result_list + new_wine

        return result_list
