# CuriousMyth

A system to organize and to link entities of information or entities of given facts and build 
a knowledge graph from it and explore this knowledge graph. This project slightly differs from
project CheapLithium - CheapLithium builds an executable knowledge graph, where CuriousMyth 
tries to model factuals and linking them with sources.

## Use Cases

lets provide some possible use cases, which may or may not be for what this system could potentially be used.

* Use Cases
  * maybe we want to investigate and research for a book 
  * maybe we want to research a scientific topic
  * we may need to keep references and sources for a given information or a given fact
  * maybe we want to arrange and preserve knowledge
  * maybe we want to exchange our information with others
  * maybe we want to investigate some untested/contested theories
  * maybe we want to learn about complex systems (biology, feedback systems etc.)
  * maybe we have a research project and develop new throries, weher we have facts and we want to model how we dereived a a certain conclusion
* Build Archive
  *  Upload Information / Upload Facts / to keep a copy of them / a.k.a. Caching
  *  Retrieve Information
  *  URL archiving / Data Crawling
  *  History of the graph

## Data Labelling

* Data Entities
  * infromation
  * facts
  * entities (persons, companies)
  * historic events
* Facts should be added labels to them
  * Date
  * Position (country, GPS, ...)
  * Topic
  * URLs
  * URIs to other databases / tools
  * Book/Conference/ etc. references (Citations)
* relationshipts between information and facts by having triple grammars (fact/information, annotated arrow (with fact or information), fact/information)

## Diagramming

* we want to explore and diagram these relation ships
  * Notices
  * Timelines
  * (interactive) Diagrams
  * retrieve information
  * have certain queries to select entities for a certain diagram
  * cretae info graphics from selected enteties

## Tech?

* Some kind of GraphDB?
  * make or buy (Neo4J)?
* provide history for graph changes (GIT/SVN?)
