profile = {
        # default value
        'name': 'N/A',
        'email': 'N/A',
        'phone': 'N/A',
}

user_input = {
        'name': 'Take',
        'phone': '123-456-789',
}

profile |= user_input
print(profile)

