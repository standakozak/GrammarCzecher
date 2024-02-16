# GECCC dataset

This README provides a description of the attached files for the GECCC dataset.

The [data](data) folder comprises three subfolders: *train*, *dev* and *test*, each storing files of the particular set. In each folder, eight files can be found:
- *sentence.m2* – sentences in the M2 format
- *paragraph.m2* – paragraphs in the M2 format
- *sentence.input*, *sentence.gold* – aligned detokenized sentences (input with original noisy sentences and gold with one or two of their [alternative] corrections [tab-separated])
- *paragraph.input*, *paragraph.gold* – aligned detokenized paragraphs (input with original noisy paragraphs and gold with one or two of their [alternative] corrections [tab-separated])
- *sentence.meta* – each line in this file specifies a pointer to the meta-description file that contains metadata such as the user domain of the sentence writer or the original document the sentence belongs to. Specifically, i-th line of this file stores the pointer for the i-th line of sentence.input and sentence.gold, and i-th record in sentence.m2
- *paragraph.meta* – same as sentence.meta but for the paragraph-level data. Note that both sentences and paragraphs are in their files in original order and that paragraphs can be joined into documents using information from the paragraph.meta file (all paragraphs belonging to the same document have the same ID).

Note that paragraph-level data contain special character ࿄, which represents the newline. It originates in the fact that while annotating the dataset, annotators were allowed to join two paragraphs into one or split a paragraph into two paragraphs if such change leads to a better text. Also note that we do not include document-level aligned data as they can be easily reconstructed from paragraph-level data and their meta-information.

The meta-description file *meta.tsv* (located in [data](data)) is a tab-separated file that stores meta-information about each record. Specifically, it has these columns:
- Filename – ID of the record that is used for linking from the .meta files
- Domain – one of 4 user domains (*Natives Formal*, *Natives Web Informal*, *Romani* and *Second Learners*)
- Age – either a 1- or 2-digit string specifying the age of the writer, or 4-digit string indicating writer age range (e.g. 1519 stays for age between 15 and 19) or *Unknown*
- Sex – either *F* (female), *M* (male) or *Unknown*
- isSlavic – either *Yes* if the writer comes from a Slavic language group, *No* if he does not or Unknown
- Source – name of the corpus the original noisy document comes from.
- OriginalName – ID of the document storing the original sentences regarding the Source. The main purpose of this is to allow linking the GECCC dataset records to their original records that sometimes provide more metadata than Age, Sex and isSlavic that we chose.
- NewlyAnnotated – whether the document is annotated with new annotations or the annotation were not newly created and come from the original source

We are also attaching the slightly modified Moses detokenizer script *detokenizer.perl* that we used to detokenize original texts that were provided only as tokenized variants (e.g. source texts from AKCES-GEC).

# Citation

The dataset was introduced in the paper [Czech Grammar Error Correction with a Large and Diverse Corpus](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00470/110536).

Please cite the following publication:

```
@article{10.1162/tacl_a_00470,
    author = {Náplava, Jakub and Straka, Milan and Straková, Jana and Rosen, Alexandr},
    title = "{Czech Grammar Error Correction with a Large and Diverse Corpus}",
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {10},
    pages = {452-467},
    year = {2022},
    month = {04},
    issn = {2307-387X},
    doi = {10.1162/tacl_a_00470},
    url = {https://doi.org/10.1162/tacl\_a\_00470},
    eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00470/2008050/tacl\_a\_00470.pdf},
}
```
