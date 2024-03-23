import os
import openai
from openai import OpenAI
import json

class Classifier:
    def __init__(self, possible_classifications):
        self.client = OpenAI()
        self.possible_classifications = possible_classifications

    def classify(self, input_string):

        sys_prompt = """You are an advanced text classification model designed to output JSON. 
        Your task is to analyze the given text and assign one or more relevant labels from the 
        provided list of potential labels. If you believe that multiple labels apply, you should 
        assign all of them. If none of the provided labels seem appropriate, you should apply the label "none". 
        The JSON response should have a key named "classifications" which holds an array of classification labels. 
        Each classification label should be a JSON object with the following structure:

        {
        "classifications": [
            {
            "label": "string",
            "confidence": float
            },
            ...
        ]
        }
        label (string): This is the name or category of the classification.
        confidence (float): This is a value between 0 and 1 that represents the confidence or probability of the classification being correct. Higher values indicate higher confidence.
        E
        Example 1:
        {
        "classifications": [
            {
            "label": "dog",
            "confidence": 0.98
            },
            {
            "label": "animal",
            "confidence": 0.92
            }
        ]
        }
        In this example, the response indicates that the text is classified as "dog" with a high confidence of 0.98, and also as an "animal" with a confidence of 0.92.

        Example 2:
        {
        "classifications": [
            {
            "label": "landscape",
            "confidence": 0.75
            },
            {
            "label": "mountain",
            "confidence": 0.68
            },
            {
            "label": "nature",
            "confidence": 0.82
            }
        ]
        }
        Here, the response classifies the text as a "landscape" with a confidence of 0.75, a "mountain" with a confidence of 0.68, and "nature" with a confidence of 0.82.

        Example 3:
        {
        "classifications": [
            {
            "label": "car",
            "confidence": 0.91
            },
            {
            "label": "vehicle",
            "confidence": 0.87
            },
            {
            "label": "sedan",
            "confidence": 0.79
            }
        ]
        }
        In this case, the response identifies the text as a "car" with a confidence of 0.91, a "vehicle" with a confidence of 0.87, and a "sedan" with a confidence of 0.79.
        """

        prompt = f"Classify the following text into one of these categories: {', '.join(self.possible_classifications)}\n\nText: {input_string}\n\nClassification:"

        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        classification = response.choices[0].message.content.strip()

        result = {"classification": classification}
        
        return json.dumps(result, indent=4)
