# Modularized version of RiC-O 1.0.2: rationale, warning and use cases

This folder contains **five files, which, when they are used together, are equivalent to the [RiC-O_1-0-2.rdf file](../RiC-O_1-0-2.rdf)**:

- the *RiC-O_1-0-2_main.rdf* file. This file contains the metadata and introduction of the ontology, and the declarations of the classes and properties used in RiC-O but defined by other ontologies and vocabularies, e.g. SKOS. It also includes, at lines 21-24, four owl:imports whose objects are the four other files:
```
<owl:imports rdf:resource="RiC-O_1-0-2_core.rdf"/>
<owl:imports rdf:resource="RiC-O_1-0-2_relations.rdf"/>
<owl:imports rdf:resource="RiC_DocumentaryFormTypes_vocabulary.rdf"/>
<owl:imports rdf:resource="RiC_RecordSetTypes_vocabulary.rdf"/>
```

- the *RiC-O_1-0-2_core.rdf* file. This file contains the specifications of all the RiC-O 1.0.2 components, except what concerns the n-ary Relation classes and the SKOS vocabularies and concepts.
- the *RiC-O_1-0-2_relations.rdf* file. This file contains the specifications of the 48 RiC-O 1.0.2 n-ary Relation classes, of the three datatype properties which have domain these classes, of the object properties which have domain or range these classes, and the declarations of the property chain axioms of the 84 shortcut object properties, in addition to their specification in the core file.
- the *RiC_DocumentaryFormTypes_vocabulary.rdf* and the *RiC_RecordSetTypes_vocabulary.rdf* files, which define the SKOS vocabulary and a few SKOS concepts describing respectively Documentary Form Types and Record Set types.


This set of files has been generated from the RiC-O_1-0-2.rdf file. They may be in the future the reference files for RiC-O, since EGAD may consider easier to maintain the ontology this way. RiC-O is already a very dense ontology, whose size is about 1,5 Mo. If the ontology is further enriched with new components, or new assertions, such as mappings, or complete translations of its documentation, or new concepts for the vocabularies, it could prove much more practical to manage it in the form of a set of specialized files.


However, **for now, the reference version of RiC-O remains the RiC-O_1-0-2.rdf file**. Besides, the modularized version is more difficult to use. **It is therefore strongly recommended to use the RiC-O_1-0-2.rdf file in preference to the modularized version**.

In some implementations, **expert users may nevertheless consider interesting to use the modular version of RiC-O, since they may only need some of the files provided**.

For now we can imagine two use cases of the kind:

- **use case 1**: **you have already analyzed your needs and you came to the conclusion that you do not want to use the Relation classes**. 
As a consequence, you do not need either the datatype or object properties whose domain or range is a Relation class, nor the property chain axioms that are defined in RiC-O 1.0.2 and specify, for some object properties, the complex path, involving a Relation class, of which that object property is a shortcut.
In such a case, if you would rather handle a simpler and shorter file than the reference file, **you could use the RiC-O_1-0-2_main.rdf and the RiC-O_1-0-2_core.rdf files only, and if you need them, the vocabulary files.** 
In order to do so, you would first have to open the RiC-O_1-0-2_main.rdf file in an XML editor, and comment line 22, as shown below:
```
<!-- <owl:imports rdf:resource="RiC-O_1-0-2_relations.rdf"/>-->
```
Then, you can open the *RiC-O_1-0-2_main.rdf* file in an OWL 2 ontology editor like Protégé Desktop, and resolve the imports by locating the three needed files on your local system. An ontology editor like Protégé Desktop will then display the content of the four files just as is they were in a single file.

- **use case 2**: **you are just working on vocabularies and would like to use and extend the RiC-O vocabularies**. In such a case, just use the vocabulary files.





