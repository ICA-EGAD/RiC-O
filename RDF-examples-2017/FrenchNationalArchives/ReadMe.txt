- Example of using RiC-O -

- RDF files generated from XML/EAC and XML/EAD files created by the Archives nationales de France -

The examples are taken from an ongoing project, lead by the ANF, which, as a proof of concept, aims to prove:
- it is possible to convert "real world" sets of archival metadata coming from several distinct institutions, and obtain RDF triples having a high level of granularity and representing accurately the concepts and relations conveyed by these metadata
In this project RiC-O is the reference ontology (it has been very slightly extended)
The institutions involved are : the ANF, the French National Library and the Service ministériel des Archives de France (a subdivision of the Department of Culture)
- it is possible to connect the three RDF resulting datasets between each other, aligning some resources ; and to enrich the datasets by reasoning (creating SPARQL inference rules), including using some external datasets 
- it is possible to provide a web interface that helps the end user to browse the graph, to visualise the nodes and arcs (data visualisation), to query the triplesytore

The RDFisation has been done by the ANF (F. Clavaud). 
A private company is currently working on the 2 next steps; a first version of the web interface will be showable soon.

Selected source files:
- about 300 XML/EAC-CPF files describing persons or corporate bodies
- about 50 XML/EAD 2002 files describing archival records created by these entities 

RDF output :
Generated automatically using a suite of XSLT2 scripts, that will be released under GPL licence when the project is over (by the end of 2017)
RiC-O classes used : 
- Agent, Person, CorporateBody
- GroupType
- LegalStatus
- RecordSetType
- AgentName
- Position, FunctionAbstract
- Event, Place
- Mandate
- Record
- RecordSet
- Proxy
- a quite important number of Relation subclasses (DenominationRelation, TypeRelation, LocationRelation, RecordsProvenanceRelation, AgentHierarchicalRelation and subclasses, AgentMembershipRelation, AgentLeadershipRelation, AgentControlRelation, AgentWholePartRelation, BusinessRelation, TemporalRelation)

The files that you can find in this folder are samples of the source and of the RDF files.
I can provide a lot more.

THESE FILES ARE PROVIDED FOR YOUR PERSONAL USE ONLY FOR THE MOMENT. PLEASE KEEP THEM FOR YOURSELVES !


