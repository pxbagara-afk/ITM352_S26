responses = [5, 7, 3, 8]
responses_ids = (1012, 1035, 1021, 1053)

survey_dict = dict(zip(responses_ids, responses))

print(f"Respond (response_id[2]): {survey_dict[responses_ids[2]]}")  # Accessing the response for the third respondent