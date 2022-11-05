# Assignment 2 Reflection | Maria Herwagen

## 1. Project Overview

For this project, I chose to analyze the Wikipedia pages for Johnny Depp and Amber heard using Levenshtein's Distance comparison and sentiment analysis. Generally, Wikipedia and other encyclopedia entries are supposed to be objective. I wanted to see if in light of the recent trials, the information about these celebrities was similar in wording, and if the sentiment about them was similar between the two articles. In the perfect world, there would be some similarities in content, and similarly neutral sentiment in these two articles, given the fact that they are dictionary entries.

## 2. Implementation

I loaded the data into two text files, and then extracted strings from them. Since both the NLTK and The Fuzz libraries use strings as inputs, I could keep the data as such. I then focused in on specific sections to perform my analysis using the full thefuzz.fuzz library and the Sentiment Intensity Analyzer function from NLTK. For my results, I leveraged f strings to explain the numbers to the user.

With more time, I also counted the words in each article to support my analysis. Additionally, I was able to work on removing irrelevant stopwords from the strings that I was comparing in order to allow for comparison of the meaning of the articles without artificially inflating the results.

One decision I had to make for my design was whether to make my functions specific to the content I was working with or to make them more general. Using specific functions would have required more of them and used more computational power, however, it would make my main() function much neater. Using general functions would require more variable defintions in the docstrings and more code in my main() function, but it would allow for a repeatable process for the user to be able to leverage my code for other similar projects. In the end, I chose to make my text file function specific to the project at the start of my code, and then use general functions for the rest of it, as I leveraged them more than once for different articles and sections in my main() function. This allowed me to have an easier time with the initial text file creation, but then I was able to save computational power, even if my main() function has a lot of code inside of it. This approach would also let the end user make only minor changes to the first function as well as to the main() function at the end to be able to use this code for another Wikipedia article analysis.

Another decision I made in the second iteration of this assignment was to reorganize my functions into three separate documents. The functions in ```access.py``` write the articles into text files and allows to choose a part that returns as a string. ```text_analyze.py``` contains all the functions for the analysis, and ```main.py``` presents the information back to the user, using functions from the other two files. I believe that separating the functions into different files allows for more flexibility for a wider range of uses. For example, someone could leverage my ```text_analyze.py``` file to perform a similar analysis on other text data without having to change the input or the output of my existing project.

## 3. Result

I found that the career sections for Johnny Depp and Amber Heard are fairly similar, but still have many differences. This was expected given the fact that they have had very different careers, but are both actors working in the same field.

The sentiment analysis of the career sections shows that overall, there's more positive **and** more negative sentiment associated with Johnny Depp's career than with Amber Heard's. This may be because of the larger amount of words in his section, but it looks like overall, Johnny Depp's section has more sentiment-indicative words. This may suggest more polarized sentiment associated with this actor.


As for their personal life sections, I found those to be even more similar than the career sections. This makes sense because both actors have descriptions of the trials in these sections, which should contain most of the same information.

The sentiment analysis of the personal life sections shows that overall, there's more positive and less negaitve sentiment associated with Johnny Depp than with Amber Heard. This again may be because the section is longer for Depp, but it could also point to positive-sentiment bias towards the male actor.

## 4. Reflection.

I wasn't sure how big the scope of this project should be, so I went for two simpler analysis techniques and tried to leverage them together. I think that having two things like similiarty and sentiment analysis side by side allowed me to really focus on the content of these articles, especially once I figured out how to cut into specific sections. I think the layout went well for me, and I'm glad I though of making more general functions rather than creating more individual functions that were repetitive. I tested each one of my functions as I went along, and I didn't find much difficulty with any of them except the setup of the text files and the extraction function. With more time, I was able to add word counts and remove stopwords, which, as expected, yielded lower number results for the comparison index.

From this experience, I have learned how to set up a full project in Python and how to work through the challenges, changes, and edits. It was difficult to scrap some of the work that I had done in order to resturcture the project, but I'm glad I worked towards simplicity and clarity. When I came back to this assignment, I was able to leverage what I learned from doing the project the first time and work on more relevant analysis and restructure the organization again. This is probably the first time that I've spent a significant portion of coding on the design of the document, and I think it's helping me understand programming and problem solving in a new way. I now think not only about the user's experience with the output, but also about another programmer's experience with the code. I'm glad I got the chance to spend time on design.


