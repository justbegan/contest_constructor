
class Error400:
    """
    {
        "status": False,
        "data": "user_oid user_oid must be mandatory"
    }, status_code=400
    """
    def __init__(self, data) -> None:
        self.data = data

    def error400(self):
        return "asdasd"
