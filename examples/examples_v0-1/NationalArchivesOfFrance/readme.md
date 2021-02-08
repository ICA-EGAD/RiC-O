# Example files based upon some archival metadata managed by the Archives nationales de France (ANF)

Examples prepared by: Florence Clavaud, member of ICA EGAD

Date of this example set: March 13, 2020

Language(s) used: French

These example files are under CC BY 4.0 license ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

For any question, please contact: Florence Clavaud ([florence.clavaud@culture.gouv.fr](mailto:florence.clavaud@culture.gouv.fr)).

**The 'src' folder contains** :

- in an 'eac-cpf' folder, **101 authority records that conform to ICA ISAAR(CPF) standard and are encoded in XML/EAC-CPF**. Each of the authority records describes a person, a corporate body or a family which created some archival resources held by the ANF. You will also find in this folder a tsv file that provides a list of these authority records.
 
- in an 'ead' subdfolder, **15 finding aids that conform to ICA ISAD(G) standard and are encoded in XML/EAD2002**. They describe record sets created by the agents mentioned above.

These source files have been published online. You can access an HTML version of these files at 
[https://www.siv.archives-nationales.culture.gouv.fr](https://www.siv.archives-nationales.culture.gouv.fr). The only official, uptodate version of the source files is to be found there.

If you want to access an HTML version (then a PDF version, + the latest version of the EAD source file) of one of the findig aids, type its permalink, using the following pattern:
https://www.siv.archives-nationales.culture.gouv.fr/siv/IR/{FA_Id}, where '{FA_Id]' is the name of the EAD file (and the value of the ead/eadheader/eadid element in the file).

If you want to access an HTML version (then a PDF version) of one of the authority records, type its permalink, using the following pattern:
https://www.siv.archives-nationales.culture.gouv.fr/siv/NP/{AR_Id}, where '{AR_id}' is the name of the EAC-CPF file (and the value of the eac-cpf/control/recordId element in the file).

**These source files are provided as example files but do not represent the variety of the 28000 finding aids and 15000 authority records that the ANF hold**. They have been chosen because they are linked to each other, and because an earlier version of them was used for the French RDF/RiC proof of concept released in February 2018 ([https://piaaf.demo.logilab.fr](https://piaaf.demo.logilab.fr)). **They do not either always conform to the local best practice as recommended in the application guidelines used in the ANF**.

**The 'rdf-xml' folder contains the RDF files generated from the src folder, and conforming to RiC-O v0.2 ontology (as it is on March 13, 2020)**. Each EAC-CPF or EAD file corresponds to one RDF/RiC-O source file. These files are stored in several folders, depending on the type of the RDF resource.
The 'vocabularies' subfolder contains a first, most often quite poor and not complete, RDF/RiC-O version of some of the controlled vocabularies used in the ANF, for indexing the EAD and EAC-CPF files. Though the RDF files refer to some instances of RiC-O Place, the ANF authority records on places are not provided in this folder; they are under development.

**The base URI defined for these RDF resources is: http://data.archives-nationales.culture.gouv.fr/. It is fictitious**: the URIs are not dereferencable. The RDF dataset is provided only as an example RiC-O archival dataset.

You will also find three JPEG images in the folder. These are **screenshots from visual graphs generated from the RDF dataset, by a GraphDB Free local instance, about some of the agents and record resources described**.


