### Exercise 1:

*Please explain, in a few clear sentences, why the reasoner classifies Barolo as an Italian wine.

Barolo is a subclass of Wine, and is `grown_in` Piedmont.
Piedmont is a Region, with the object property `region_of` Italy
The relation `grown_in` is a property chain axiom, such that given grown_in(a,b) and region_of(b,c), grown_in(a,c) is derived.
Therefore, Barolo is a subclass of Wine, and is also `grown_in` Italy. 
Italian wine is defined as a subclass of Wine in which instances are both subclasses of Wine and are `grown_in` Italy.

*Compare the original OWL representation of the wine ontology and its representation as a Neo4j labelled property graph and document the transformation in your own words. How do the representations differ? How was the OWL representation mapped into the Neo4j representation?

I could not get docker working.

### Exercise 2: 

Please see [queries_and_testing.md](queries_and_testing.md)

### Exercise 3: 
Write a couple of paragraphs on how you might extend the OWL modelling and content to build a knowledge base of individual wines that would be useful to consumers trying to decide what wine to buy.

As I am not a wine expert, my initial step would be to speak to an expert in the realm of helping consumers decide which wine to buy (or some consumers of wine), to see what information is most useful in making that decision. In lieu of this, I will assume the following criteria are the most important factors for deciding which wine to buy:
 1. Price of the wine
 2. Where the wine is avalilible to purchase
 3. Flavor traits of the wine
 4. A 'similar wines' suggestion

The first point requires a small expansion of the current ontology. I would implement this by adding a data property `has_price` to relate wines to the value of the price of the wine.

For now I will ignore the 2nd point, as this would involve determining which wines stores stock, and is more complex. 

Points 4 and 5 both rely on point 3, so I will expand on these three points together. All three require additions to the current ontology. In order to describe the flavor traits of the wine, one could either define a set of flavor traits and add an objec property between wines and the tasting notes, or one could add a data property and allow any string to be used as a tasting note. The second option gives more flexibility, but because we want to use these flavor traits to infer the answers to other questions (i.e. for point 4), the first option is preferable. In reality both can be done simultaneously, but for now I will only discuss the first option.

A quick online search suggests that the main wine tasting points are:
 - Body
 - Sweetness
 - Acidity
 - Tannin
 - Alcohol
Each is traditionally given a score from 1 (low) to 5 (high). Because this is a commonly used description of wine, I believe it would be a good structure to use. I would create a set of new functional data properties called `has_body`, `has_sweetness`, `has_acidity`, `has_tannins`, and `has_alcohol`. Each instance of Wine would then be given values of integers from 1 to 5 for each tasting point.

To suggest similar wines, I would query for wines that have the same values for each tasting note as the wine selected.
