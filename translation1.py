import os
from google.cloud import translate_v3beta1 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r"D:\HDD APPS\CODE\Google Stuf\TranslationAPI\cloudKey.json"

#print(type(translate.Client()))

# translateClient=translate.Client()

# text="こんにちは世界"
# target='en'

# output= translateClient.translate(
#     text,
#     target_language=target
# )

# print(output)


def translate_document(project_id: str,file_path: str):

    client = translate.TranslationServiceClient()

    location = "us-central1"

    parent = f"projects/{project_id}/locations/{location}"

    # Supported file types: https://cloud.google.com/translate/docs/supported-formats
    with open(file_path, "rb") as document:
        document_content = document.read()
    
    # with open("output.txt",'wb') as outDocument:
    # #f = open('D:\HDD APPS\CODE\Google Stuf\TranslationAPI\output', 'wb')
    #     document_output=outDocument.write()
    

    document_input_config = {
        "content": document_content,
        "mime_type": "application/pdf",
    }
    document_output_config = {
        "mime_type": "application/pdf",
    }

    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": "fr-FR",
            "document_input_config": document_input_config,
            "document_output_config":document_output_config,
        }
    )
    
    # To output the translated document, uncomment the code below.
    f = open('result.pdf', 'wb')
    f.write(response.document_translation.byte_stream_outputs[0])
    f.close()

    # If not provided in the TranslationRequest, the translated file will only be returned through a byte-stream
    # and its output mime type will be the same as the input file's mime type
    print("Response: Detected Language Code - {}".format(response.document_translation.detected_language_code))
    byteResponce=response.document_translation.byte_stream_outputs
    print(type(byteResponce))

translate_document("translation-test-356706","test3.pdf")