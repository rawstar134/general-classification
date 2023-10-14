
class response():
    def __init__(self, response_object):
        self.status = ""
        self.error_message = ""
        self.response = response_object
        self.final_response = []

    def __call__(self, *args, **kwargs):

        if not self.response:
            self.status = "Success"
            self.error_message = ""
            self.final_response.append(self.status)
            self.final_response.append(self.error_message)
            self.final_response.append(self.response)
        else:
            self.status = "Failed"
            self.error_message = "Failed to fetch news"
            self.final_response.append(self.status)
            self.final_response.append(self.error_message)

        return self.final_response

