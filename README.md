# Text Summarization Flask App with OpenAI API

## Project Overview
This Flask application offers a web-based interface to summarize text utilizing the OpenAI API. Users can submit text through a web form, and receive a concise summary back, leveraging the power of OpenAI's GPT-3.5 model.

## Dependencies
- Python 3.8+
- Flask
- openai (OpenAI Python client library)

## Installation

1. Clone the repository: 

```
git clone https://github.com/nogibjj/ids706-individual-project-4
```


2. Navigate to the folder:

```
cd ids706-individual-project-4
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Set your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY='your-api-key-here
```

5. Run the application:

```export FLASK_APP=main.py```
```flask run --host=0.0.0.0 --port=8085```

The application will be available at http://localhost:8085/.

## Usage

1. Visit the main page and input the text you want to summarize.
2. Submit the form to see the summary on the results page.

## Conclusion and Recommendations to Management

The deployment of this summarization tool promises to streamline workflows by condensing extensive texts. For maximum impact, management should:

* Integrate with internal systems to facilitate rapid information synthesis.
* Encourage interdepartmental use to improve overall efficiency.
* Monitor usage and gather user feedback for iterative improvement.

## Future Enhancements

* Implement secure user sessions for personalized experiences.
* Allow bulk processing for high-volume summarization needs.
* Offer adjustable summary lengths to cater to different user requirements.

*Note: Refer to the templates directory for index.html and result.html. Use the provided Dockerfile for deployment. The main.py script contains the Flask application logic.*


