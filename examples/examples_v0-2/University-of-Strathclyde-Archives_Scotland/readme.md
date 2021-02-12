# Example files based upon some archival metadata managed by the University of Strathclyde Archives (Glasgow, Scotland, United Kingdom)

Examples prepared by: Victoria Peters and Florence Clavaud, members of ICA EGAD

Date of this example set: February 12, 2021

Language(s) used: English

These example files are under CC BY 4.0 license ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

For any question, please contact: Victoria Peters (
[victoria.peters@strath.ac.uk](mailto:victoria.peters@strath.ac.uk)) and Florence Clavaud ([florence.clavaud@culture.gouv.fr](mailto:florence.clavaud@culture.gouv.fr)).

**The 'src' folder contains** :

- **5 authority records that conform to ICA ISAAR(CPF) standard and are encoded in XML/EAC-CPF**. The names of these files end with "Agent". Each of the authority records describes a person or a corporate body which created some archival resources held by the University of Strathclyde Archives.

- **4 small finding aids that conform to ICA ISAD(G) standard and are encoded in XML/EAD2002**. They describe record sets created by the persons or corporate bodies mentioned above.

- the EAD 2002 DTD ('ead.dtd' file) and the EAC-CPF XML schema ('cpf.xsd' file).

These source files are exactly the same as in the 'examples_v0-1/University-of-Strathclyde-Archives_Scotland/src' folder. They have been published online. You can access an HTML version of these files at 
[https://atom.lib.strath.ac.uk/](https://atom.lib.strath.ac.uk/). The only official, uptodate version of the source files is to be found there.

**The 'rdf-xml' folder contains the RDF files generated from the 'examples_v0-1/University-of-Strathclyde-Archives_Scotland/rdf-xml' folder, and conforming to RiC-O v0.2 ontology (its public official release, dated Feb. 12, 2021)**. Each EAC-CPF or EAD file corresponds to one RDF/RiC-O source file.
The differences between these RDF/XML files and the files available in the 'examples_v0-1/University-of-Strathclyde-Archives_Scotland/rdf-xml' folder mainly concern the **IRIs of some object properties** (that changed from RiC-O 0.1 to RiC-O 0.2) and **some properties used for instances of Record Set class** (hasLanguage replaced by hasOrHadAllMembersWithLanguage; hasDocumentaryFormType replaced by hasOrHadAllMembersWithDocumentaryFormType).
Apart from these RDF files, the folder also contains two files about two agents whose description is included in the EAC-CPF source files (the University of Strathclyde Archives and Special Collections, which holds the archival resources described, and the University of Strathclyde Scottish Oral History Centre). There is also one file that includes the RDF output from the subject EAD elements (things.rdf), one file that includes the RDF output from the geogname EAD elements (places.rdf), and a file that includes the RDF output from the associative relationships found in some EAC-CPF files (agentToAgentRelations.rdf).

**The base URI defined for the RDF resources is: http://data.archives.strath.ac.uk/. It is fictitious**: the URIs are not dereferencable. The RDF dataset is provided only as an example RiC-O archival dataset.

You will also find  a JPEG image in the folder. It is **a screenshot from a visual graph generated from the RDF dataset**, by a GraphDB Free local instance, about the following URI:
http://data.archives.strath.ac.uk/recordResource/greater-manchester-asbestos-victims-support-group-oral-history-project.
This URI identifies the Greater Manchester Asbestos Victims Support Group oral history project in the dataset. This collection is described by the GMAVSG_oral_history_project.xml EAD file, whose RDF version is the GMAVSG_oral_history_project.rdf file.



