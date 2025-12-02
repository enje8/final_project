#api_board_test.py
from api.SkyengApi import SkyengApi
import uuid


def test_add_event(api):
        events_before = api.get_events()

        new_name = str(uuid.uuid4())
        api.create_event(new_name)


        events_after = api.get_events()
        assert len(events_after["data"]["events"]) - len(events_before["data"]["events"]) == 1

def test_delete_event(api):

        new_name = str(uuid.uuid4())
        created_event = api.create_event(new_name)

        events_before = api.get_events()
        
        api.delete_event(created_event["data"]["payload"]["id"], created_event["data"]["startAt"])      

        events_after = api.get_events()
        assert len(events_before["data"]["events"]) - len(events_after["data"]["events"]) == 1

def test_update_event(api):

        title = str(uuid.uuid4())
        created_event = api.create_event(title)

        new_title = str(uuid.uuid4())
        api.update_event(created_event["data"]["payload"]["id"], created_event["data"]["startAt"], new_title)      
        
        events = api.get_events()["data"]["events"]
        for event in events:
                payload = event.get("payload", {})
                if payload.get("id") == created_event["data"]["payload"]["id"]:
                        found_title = payload.get("payload", {}).get("title")
                        break

        assert found_title == found_title

        
def test_update_event_description(api):

        title = str(uuid.uuid4())
        created_event = api.create_event(title)

        new_description = str(uuid.uuid4())
        api.update_event_description(created_event["data"]["payload"]["id"], created_event["data"]["startAt"], new_description)

        events = api.get_events()["data"]["events"]
        for event in events:
                payload = event.get("payload", {})
                if payload.get("id") == created_event["data"]["payload"]["id"]:
                        found_description = payload.get("payload", {}).get("description")
                        break

        assert new_description == found_description


def test_update_event_color(api):

        title = str(uuid.uuid4())
        old_color = "#FFF7C7"
        created_event = api.create_event(title, old_color)

        new_color = "#D478F1"
        api.update_event_color(created_event["data"]["payload"]["id"], created_event["data"]["startAt"], new_color)

        events = api.get_events()["data"]["events"]
        for event in events:
                payload = event.get("payload", {})
                if payload.get("id") == created_event["data"]["payload"]["id"]:
                        found_color = payload.get("payload", {}).get("color")
                        break

        assert new_color == found_color