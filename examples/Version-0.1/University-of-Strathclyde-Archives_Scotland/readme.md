# Example files based upon some archival metadata managed by the University of Strathclyde Archives (Glasgow, Scotland, United Kingdom)

Examples prepared by: Victoria Peters and Florence Clavaud, members of ICA EGAD

Date of this example set: February 28, 2020

Language(s) used: English

These example files are under CC BY 4.0 license ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

For any question, please contact: Victoria Peters (
[victoria.peters@strath.ac.uk](mailto:victoria.peters@strath.ac.uk)) and Florence Clavaud ([florence.clavaud@culture.gouv.fr](mailto:florence.clavaud@culture.gouv.fr)).

**The 'src' folder contains** :

- **5 authority records that conform to ICA ISAAR(CPF) standard and are encoded in XML/EAC-CPF**. The names of these files end with "Agent". Each of the authority records describes a person or a corporate body which created some archival resources held by the University of Strathclyde Archives.

- **4 small finding aids that conform to ICA ISAD(G) standard and are encoded in XML/EAD2002**. They describe record sets created by the persons or corporate bodies mentioned above.

- the EAD 2002 DTD ('ead.dtd' file) and the EAC-CPF XML schema ('cpf.xsd' file).

These source files have been published online. You can access an HTML version of these files at 
[https://atom.lib.strath.ac.uk/](https://atom.lib.strath.ac.uk/). The only official, uptodate version of the source files is to be found there.

**The 'rdf-xml' folder contains the RDF files generated semi-automatically from the src folder, and conforming to RiC-O v0.1 ontology**. Each EAC-CPF or EAD file corresponds to one RDF/RiC-O source file.
Apart from these RDF files, the folder also contains two files about two agents whose description is included in the EAC-CPF source files (the University of Strathclyde Archives and Special Collections, which holds the archival resources described, and the University of Strathclyde Scottish Oral History Centre). There is also one file that includes the RDF output from the subject EAD elements (things.rdf), one file that includes the RDF output from the geogname EAD elements (places.rdf), and a file that includes the RDF output from the associative relationships found in some EAC-CPF files (agentToAgentRelations.rdf).

**The base URI defined for the RDF resources is: http://data.archives.strath.ac.uk/. It is fictitious**: the URIs are not dereferencable. The RDF dataset is provided only as an example RiC-O archival dataset.

You will also find  a JPEG image in the folder. It is **a screenshot from a visual graph generated from the RDF dataset**, by a GraphDB Free local instance, about the following URI:
http://data.archives.strath.ac.uk/recordResource/greater-manchester-asbestos-victims-support-group-oral-history-project.
This URI identifies the Greater Manchester Asbestos Victims Support Group oral history project in the dataset. This collection is described by the GMAVSG_oral_history_project.xml EAD file, whose RDF version is the GMAVSG_oral_history_project.rdf file.



