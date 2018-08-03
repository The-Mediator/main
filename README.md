# Mediator : Text Summarization Research and Example

## Language:
* **Python3**
____________________

## Getting Started: (Based on Windows....Email me if you need Linux Help)

1) Installing venv. The venv is used so that you can have multiple versions of
the install without effecting other projects. It is not recommended to use it
for Production but it is great for testing and environments where there are
multiple projects.

``bash
  python -m venv venv
``

2) Creating venv

``bash
  virtualenv venv
``

3) Activate venv

``bash
  venv\Scripts\activate
``

4) Installing necessary tools. The main one for this example is GENSIM,
but in the requirment.txt will show which packages will be needed or are
installed due to another package.

``bash
  pip install -r requirements.txt
``


use .gitignore so you do not push the venv in the repo. Also to get out of venv mode uses deactivate

___________________________

## Description

The idea of this example and a little bit of this research is to understand an effective way to summarize articles on the web when pointed to a places to get text. One is a fully txt file on the web and another is a wiki page. If you run the application it does show a brief summary of the content in a decent manner. We may want to increase the number of lines to give back to the user but that can be simply be changed in the summarized function.

The algorithm that is being used is based on the page ranking used in google. The idea is the text is ranked to different depending on the content of the information. More specifically the text ranking has two different way... Extractive or Abstractive
I personally prefer Abstractive because it does give you more detail which is why I use GENSIM.

"
Extractive summarization consists in scoring words/sentences a using it as summary. You can see hit as highlighting a text or cutting/pasting in that you don’t actually produce a new text, you just select (extract) some parts.

Abstractive summarization techniques aims to produce a whole new text from it “understanding” of the input. It implies to be able to actually generate a syntactically/grammatically correct text and a semantically relevant one.
"


The idea of text summarization is based on Natural Language Processing which is Machine Learning (ML). This time of ML we use is called unsupervised learning meaning we do not have to give it a training or additional training before or during the process to understand the material. It comes as is and send out the information.



#### Resources

https://rare-technologies.com/text-summarization-in-python-extractive-vs-abstractive-techniques-revisited/
https://rare-technologies.com/text-summarization-with-gensim/
https://radimrehurek.com/gensim/index.html
https://www.quora.com/Natural-Language-Processing-What-is-the-difference-between-extractive-and-abstractive-summarization
https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf (Nice Read but not really a need.)
https://radimrehurek.com/gensim/
https://rare-technologies.com/text-summarization-in-python-extractive-vs-abstractive-techniques-revisited/
