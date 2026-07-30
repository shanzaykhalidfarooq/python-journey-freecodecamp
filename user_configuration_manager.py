test_settings = {'theme': 'dark'}


def add_setting(settings_dict, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
        
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_dict, target_key):
    key = target_key.lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'


def view_settings(settings_dict):
    if not settings_dict:
        return 'No settings available.'
        
    output = ["Current User Settings:"]
    for key, value in settings_dict.items():
        output.append(f"{key.capitalize()}: {value}")
        
    return "\n".join(output) + "\n"