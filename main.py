from dotenv import load_dotenv
from app.services.classifier import Classifier

if __name__ == "__main__":
    load_dotenv()
    possible_classifications = ["positive", "negative", "neutral"]

    classifier = Classifier(possible_classifications)

    input_string = "I had a great day today!"
    classification_result = classifier.classify(input_string)
    print(classification_result)