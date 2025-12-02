import requests


class SkyengApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_events(self) -> dict:
        path = f"{self.base_url}/v2/schedule/events"
        headers = {"Cookie": f"token_global={self.token}"}
        body = {
            "from": "2025-12-01T00:00:00+03:00",
            "till": "2025-12-08T00:00:00+03:00",
            "onlyTypes": [],
        }
        resp = requests.post(path, json=body, headers=headers)
        return resp.json()

    def create_event(self, title, color="#FAC641") -> dict:
        path = f"{self.base_url}/v2/schedule/createPersonal"
        headers = {"Cookie": f"token_global={self.token}"}
        body = {
            "backgroundColor": "#FFF7C7",
            "color": color,
            "description": "Описание события",
            "title": title,
            "startAt": "2025-12-01T19:00:00+03:00",
            "endAt": "2025-12-01T19:30:00+03:00",
        }
        resp = requests.post(path, json=body, headers=headers)
        return resp.json()

    def delete_event(self, id, startAt) -> dict:
        path = f"{self.base_url}/v2/schedule/removePersonal"
        headers = {"Cookie": f"token_global={self.token}"}
        body = {"id": id, "startAt": startAt}
        resp = requests.post(path, json=body, headers=headers)
        return resp.json()

    def update_event(self, id, startAt, newTitle) -> dict:
        path = f"{self.base_url}/v2/schedule/updatePersonal"
        headers = {"Cookie": f"token_global={self.token}"}
        body = {
            "id": id,
            "oldStartAt": startAt,
            "description": "Обновленное описание",
            "title": newTitle,
            "startAt": "2025-12-01T19:00:00+03:00",
            "endAt": "2025-12-01T19:30:00+03:00",
            "backgroundColor": "#FFF7C7",
            "color": "#FAC641",
        }
        resp = requests.post(path, json=body, headers=headers)
        return resp.json()

    def update_event_description(self, id, startAt, newDescription) -> dict:
        path = f"{self.base_url}/v2/schedule/updatePersonal"
        headers = {"Cookie": f"token_global={self.token}"}
        body = {
            "id": id,
            "oldStartAt": startAt,
            "description": newDescription,
            "title": "title",
            "startAt": "2025-12-01T19:00:00+03:00",
            "endAt": "2025-12-01T19:30:00+03:00",
            "backgroundColor": "#FFF7C7",
            "color": "#FAC641",
        }
        resp = requests.post(path, json=body, headers=headers)
        return resp.json()

    def update_event_color(self, id, startAt, newColor) -> dict:
        path = f"{self.base_url}/v2/schedule/updatePersonal"
        headers = {"Cookie": f"token_global={self.token}"}
        body = {
            "id": id,
            "oldStartAt": startAt,
            "description": "description",
            "title": "title",
            "startAt": "2025-12-01T19:00:00+03:00",
            "endAt": "2025-12-01T19:30:00+03:00",
            "backgroundColor": "#FFF7C7",
            "color": newColor,
        }
        resp = requests.post(path, json=body, headers=headers)
        return resp.json()
