# Example files based upon some archival metadata managed by the University of Strathclyde Archives (Glasgow, Scotland, United Kingdom)

Examples prepared by: Victoria Peters and Florence Clavaud, members of ICA EGAD

Date of this example set: January 26, 2023

Language(s) used: English

These example files are under CC BY 4.0 license ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

For any question, please contact: Victoria Peters (
[victoria.peters@strath.ac.uk](mailto:victoria.peters@strath.ac.uk)) and Florence Clavaud ([florence.clavaud@culture.gouv.fr](mailto:florence.clavaud@culture.gouv.fr)).

**The 'src' folder contains** :

- **6 authority records that conform to ICA ISAAR(CPF) standard and are encoded in XML/EAC-CPF**. The names of these files end with "Agent". Each of the authority records describes a person or a corporate body which created some archival resources held by the University of Strathclyde Archives.

- **4 finding aids that conform to ICA ISAD(G) standard and are encoded in XML/EAD2002**. They describe record sets created by the persons or corporate bodies mentioned above.

- the EAD 2002 DTD ('ead.dtd' file) and the EAC-CPF XML schema ('cpf.xsd' file).

These source files were downloaded from the online 
[Catalogue of the University of Strathclyde Archives and Special Collections](https://atom.lib.strath.ac.uk/) on Jan. 24, 2023. The authority records have been slightly modified. The 'George_Wyllie_papers_reduced.xml file' is a significantly reduced version of the [original finding aid](https://atom.lib.strath.ac.uk/george-wyllie-papers): most of the subcomponents of the 13 series that constitute the collection have been removed. The only complete, official, uptodate version of the source files is to be found there.

**The 'rdf-xml' folder contains the RDF files generated from the 'examples_v-1-0/University-of-Strathclyde-Archives_Scotland/rdf-xml' folder, and conforming to RiC-O v1.0 ontology**. Each EAC-CPF or EAD file corresponds to one RDF/RiC-O source file.
Apart from these RDF files, the folder also contains one more file, about the University of Strathclyde Archives and Special Collections, which holds the archival reosurces described and created their descriptions. There is also one file that includes the RDF output from the subject EAD elements (things.rdf), one file that includes the RDF output from the geogname EAD elements (places.rdf), and a file that includes the RDF output from the associative relationships found in some EAC-CPF files (agentToAgentRelations.rdf).

**The base URI defined for the RDF resources is: http://data.archives.strath.ac.uk/. It is fictitious**: the URIs are not dereferencable. The RDF dataset is provided only as an example RiC-O archival dataset.

You will also find  a JPEG image in the folder. It is **a screenshot from a visual graph generated from the RDF dataset**, by a GraphDB Free local instance, about the following URI:
http://data.archives.strath.ac.uk/recordResource/greater-manchester-asbestos-victims-support-group-oral-history-project.
This URI identifies the Greater Manchester Asbestos Victims Support Group oral history project in the dataset. This collection is described by the GMAVSG_oral_history_project.xml EAD file, whose RDF version is the GMAVSG_oral_history_project.rdf file.



