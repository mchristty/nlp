import json
import requests
from datetime import datetime
from typing import Dict, Text, Any, List, Optional
import logging
from rasa_sdk.interfaces import Action
from rasa_sdk.events import (
    SlotSet,
    EventType,
)
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher


logger = logging.getLogger(__name__)

class ActionSports(Action):

    def name(self) -> Text:
        return "get_sport_info"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        response = requests.request("GET", "http://api.weatherapi.com/v1/sports.json?key=78c0462537864acd8a6191108212105&q=London", params={"q": "London"})
        result = ""

        json_data = response.json()

        for game in json_data['football']:
            result += f"Match {game['match']} in {game['tournament']} tournament in {game['country']} at {game['stadium']} will start in {game['start']}\n"

        dispatcher.utter_message(text=result)
        return []

class ActionAnimals(Action):

    def name(self) -> Text:
        return "get_fact_about_animal"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        url = ''
        if tracker.get_slot("animals_type") == "dog":
            url = 'https://dog-api.kinduff.com/api/facts?number=5'
        else:
            url = 'https://catfact.ninja/fact'
        response = requests.request("GET", url)
        result = ""

        json_data = response.json()
        if tracker.get_slot("animals_type") == "dog":
            for fact in json_data['facts']:
                result += f"{fact} \n "
        else:
            result += f"{json_data['fact']} \n "

        dispatcher.utter_message(text=result)
        return []


class ActionCountyByCityForm(Action):

    def name(self) -> Text:
        return "action_country_by_city"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        city_name = tracker.get_slot("city")

        dt = datetime.today().strftime('%Y-%m-%d')
        response = requests.request("GET", "http://api.weatherapi.com/v1/astronomy.json?key=78c0462537864acd8a6191108212105", params={"q": city_name, "dt": dt })
        result = ""

        json_data = response.json()

        result += f"City {json_data['location']['name']} is located in {json_data['location'] ['country']}:\n"
        dispatcher.utter_message(text=result)

        reset_slots = ["city"]
        return [SlotSet(slot, None) for slot in reset_slots]

class ActionAnimalPic(Action):

    def name(self) -> Text:
        return "action_animal_pic"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        animal_type = tracker.get_slot("animal_pic_type")

        if animal_type == "dog":
            response = requests.request("GET", "https://random.dog/woof.json")
            json_data = response.json()
            dispatcher.utter_message(image=json_data['url'])
        elif animal_type == "fox":
            response = requests.request("GET", "https://randomfox.ca/floof/")
            json_data = response.json()
            dispatcher.utter_message(image=json_data['image'])
        else:
            response = requests.request("GET", "https://aws.random.cat/meow")
            json_data = response.json()
            dispatcher.utter_message(image=json_data['file'])
        reset_slots = ["animal_pic_type"]
        return [SlotSet(slot, None) for slot in reset_slots]

