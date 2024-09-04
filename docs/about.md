# About RiC-O



* [Home](index.html)
* **About RiC-O**
* [Why use RiC-O?](why-use-RiC-O.html)
* [Diagrams](diagrams.html)
* [Examples](examples.html)
* [Migrating data from RiC-O 0.2 to RiC-O 1.0](migrating-data-from-RIC-O-v0.2-to-v1.0.html)
* [Events and presentations](events.html)
* [Projects, tools, and resources](projects-tools-resources.html)
* [Next steps](next-steps.html)



Last updated on September 4<sup>th</sup>, 2024


RiC-O (Records in Contexts-Ontology) is **an OWL 2 ontology for describing archival record resources**, whose IRI is [https://www.ica.org/standards/RiC/ontology](https://www.ica.org/standards/RiC/ontology). As **the third part of Records in Contexts (RiC) standard**, it is a formal representation of Records in Contexts Conceptual Model (RiC-CM).

The **latest public release of RiC-O, RiC-O 1.0.2, was published in September 2024**. **Version 1.0.2 follows the release of RiC-O 1.0.1, dated May 2024, and the release of the first stable and complete version of this ontology, thus a major milestone, RiC-O 1.0**. 

Version 1.0.1 modified a few details in the introduction, fixed a few typos in the documentation of RiC-O 1.0, and brought one change only, fixing the IRI of 'hasOrHadSomeMemberswithDocumentaryFormType' object property (changed to [rico:hasOrHadSomeMembersWithDocumentaryFormType](https://www.ica.org/standards/RiC/ontology#hasOrHadSomeMembersWithDocumentaryFormType)). 

Version 1.0.2 fixes an inconsistency bug in RiC-O 1.0, removing global reflexivity from the 48 rolification object properties. It also fixes the French labels of six object properties. Finally, a version IRI (owl:versionIRI) has been added to this 1.0.2 version, in order to make RiC-O fully compliant with the OWL 2 specification as concerns ontology documents.

Version 1.0.2 is fully documented in English and available in the RiC-O GitHub repository, in the [current-version](https://github.com/ICA-EGAD/RiC-O/tree/master/ontology/current-version) folder. It comes with some [examples](examples.html) and [diagrams](diagrams.html). 

**RiC-O 1.0.2 is compliant with the latest version of Records in Contexts-Conceptual Model (RiC-CM), RiC-CM 1.0, which was released in November 2023** and is available for download is available for download  [here](https://github.com/ICA-EGAD/RiC-CM/releases/tag/v1.0.1), or [from the ICA website](https://www.ica.org/app/uploads/2023/12/RiC-CM-1.0.pdf).

The version 1.0 of RiC-FAD, RiC-CM, and RiC-O marks **the first stable and complete version of the first three parts of RiC, and thus a major milestone in the development of the standard**. 

RiC standard is developed by the [International Council on Archives Expert Group on Archival Description (ICA EGAD)](https://www.ica.org/ica-network/expert-groups/egad/).

RiC makes it possible to describe archival records and the multiple layers of contexts in which they are inscribed through time, from their creation to their curation in an archival institution. 
It enables archivists and records managers to move forward, from the four previous ICA description standards (ISAD(G), ISAAR(CPF), ISDF and ISDIAH), which it replaces, to a more accurate, more nuanced, easier to process, multidimensional description.

RiC-O provides a generic vocabulary and formal rules for creating RDF datasets (or generating them from existing archival metadata) that describe in a consistent way any kind of archival record resource and its contextual entities. It is therefore a reference model for publishing archival metadata sets as Linked Data, querying them using SPARQL, and making inferences using the logic of the ontology.



**If you want to contact us, or send comments and questions, use the new [Records in Contexts users Google group](https://groups.google.com/g/Records_in_Contexts_users)**. Or directly create issues, or comments to existing issues, on GitHub.

