# custom action file for Rasa with webview example

from rasa_sdk import Action, Tracker

from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_core_sdk.executor import CollectingDispatcher
import yaml
import pickle
import logging
#

# set up logging
logging.getLogger().setLevel(logging.WARNING)
logging.warning("logging check")

# define config file
current_path = os.getcwd()
directory_symbol = "\\"

path_to_yaml = current_path+directory_symbol+"custom_action_config.yml"
logging.warning("path_to_yaml "+path_to_yaml)
try: 
    with open (path_to_yaml, 'r') as file:
       config = yaml.safe_load(file)
except Exception as e:
    print('Error reading the config file')
wv_URL = 

class ActionHelloWorld(Action):
#
     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        target_URL = wv_URL
            #target_URL = "https://cbc.ca"
            logging.warning("target_URL is "+str(target_URL))
            # want to make call to build display object here
            # TODO post demo 1, generalize this to be any key_slot rather than just original_title
            wv_payload = get_wv_payload('original_title',raw_movie)
            for wv_payload_index in wv_payload:
                logging.warning("wv_payload index is "+str(wv_payload_index))
                logging.warning("display content is "+str(wv_payload[wv_payload_index].display_content))
                logging.warning("display type is "+str(wv_payload[wv_payload_index].display_type))
                logging.warning("return type is "+str(wv_payload[wv_payload_index].return_type))
                logging.warning("return payload is "+str(wv_payload[wv_payload_index].return_payload))
            # pass wv_payload to flask
            load_wv_payload(wv_payload)
            message1 = {
               "attachment": {
                    "type": "template",
                    "payload": {
                      "template_type": "button",
                      "text": "Test URL button for webview",
                      "buttons": [
                        {
                           "type":"web_url",
                           "url":target_URL,
                           "title":"URL Button",
                           "messenger_extensions": "true",
                           "webview_height_ratio": "tall"
                        }
                     ]
                  }
               }
            }

         dispatcher.utter_message("Hello World!")

         return []
