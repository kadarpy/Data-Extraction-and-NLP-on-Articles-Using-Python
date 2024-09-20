# Web Scraping and Text Analysis on Articles Using Python
This project automates the extraction of article content from URLs and performs text analysis, including sentiment and readability scoring.
The output data is intended for use in understanding the complexity and sentiment of the content for various analytical purposes.

## Project Structure

- **extract_articles.py**: Script for scraping article titles and content from a list of URLs.
- **text_analysis.py**: Script for performing sentiment analysis, readability, and other text-based metrics on the extracted articles.
- **Input URL.xlsx**: Excel file containing the list of URLs to scrape.
- **Output Data Structure.xlsx**: Defines the structure of the output data with metrics and analysis results.

## Features

### 1. Article Extraction (`extract_articles.py`)
- Loads URLs from `Input URL.xlsx`.
- Extracts article titles and content using web scraping (BeautifulSoup).
- Saves the extracted content in text files under a directory called `articles extracted`.

### 2. Text Analysis (`text_analysis.py`)
- Analyzes the extracted articles for:
  - **Sentiment**: Positive and negative word counts, polarity, and subjectivity scores.
  - **Readability**: Flesch-Kincaid metrics like average sentence length, percentage of complex words, and Fog index.
  - **Other Metrics**: Word count, complex word count, syllable count, and usage of personal pronouns.

## How to Run

### 1. Install Required Libraries
Before running the scripts, install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```
### Make sure the following Python libraries are installed:

- **requests**
- **beautifulsoup4**
- **nltk**
- **pandas**
- **openpyxl**

### 2. Prepare the Input File
The input file should be an Excel file named `Input URL.xlsx` with the following structure:
#### URL_ID	URL
```bash
uniqueID	https://example.com/article1
uniqueID	https://example.com/article2
```
### 3. Run the Article Extraction
To extract articles from the URLs, run the following command:
```bash
python extract_articles.py
```
This will create a folder called `articles extracted` where the article content is saved.

### 4. Run the Text Analysis
Once articles are extracted, run the text analysis:
```bash
python text_analysis.py
```
This will process the text files in `articles extracted` and output various sentiment and readability metrics.

### Folder Structure
```bash
├── extract_articles.py           # Script for extracting articles
├── text_analysis.py              # Script for analyzing text
├── Input URL.xlsx                # Input file with URLs
├── Output Data Structure.xlsx    # Defines output data structure
├── articles extracted/           # Directory where extracted articles are saved
```
## Future Improvements
- **Add support for more complex NLP techniques (e.g., Named Entity Recognition).**
- **Improve error handling for failed URL requests.**
- **Expand sentiment lexicon for more nuanced analysis.**
