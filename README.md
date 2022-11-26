# Project title

Testing framework (Talent Engine 2.0)

## About

This project is a testing framework that utilizes Pytest.

## Dependencies

Required modules are specified in requirements.txt

```
pip install -r requirements.txt
```

## Running the tests

To run the tests run `pytest` from the root folder.

To run the test using a specific (supported) browser:

```
pytest --browser <browser name: chrome, firefox, edge>
```

## Structure of the framework

**/conftest.py** - provides Pytest fixtures for the framework  
**/envs_configs** - stores configuration data  
**/tests** - stores the tests  
**/pytest.ini** - Pytest configuration file  
**/src/applications** - stores classes for applications  
**/src/config** - sets up configuration for the framework (connection with providers, location of test data etc.).  

- config.py: contains Config class. When instantiated, it creates the config dictionary (_'conf_dict'_) and using the _'\_register'_ method receives the data from the providers and stores it in the config dictionary (raising ValueError if the item is not present in any of the providers). The _'\_\_getattr\_\_'_ method retrieves the data stored in config dictionary. When creating an instance of the Config class, config providers must be passed in as a list in a hierarchical order:

```

config = Config([JSONConfigProvider(), OSConfigProvider()])

```

In the above example, the _'\_register'_ method called during instantiation will first look for the item in JSONConfigProvider, and if it's not present, it will look in OSConfigProvider.

All config data **must** be registered using the _'\_register'_ method before it can be used.

**/src/data** - contains test data, json schemas, URLs etc.  
**/src/models** - contains models  
**/src/providers** - contains providers for config and browsers   

- base_provider.py: contains a BaseProviderClass, which raises an exception if _'\_\_getitem\_\_'_ method is not implemented in the child class. **All config provider classes must inherit from BaseProviderClass.**
- os_config_provider.py: - contains an OSConfigProvider class. method _'\_\_getitem\_\_'_ returns the value of specified environment variable (or None if it doesn't exist).
- json_config_provider.py: - contains a JSONConfigProvider class. method _'\_read_config'_ returns a dictionary with the contents of JSON file with path 'config_path' - _'\_\_getitem\_\_'_ returns the value of specified item in dictionary received from _'\_read_config'_. The JSON file should be located in the /envs_configs directory. **Absolute path** to JSON file needs to be passed in:

```

value = JSONConfigProvider.\_read_config(insert_absolute_path_to_json_file_here)

```

**/src/providers/browsers/library** - contains classes for supported browsers

To add support for a **new browser**, create a new class for it (copy-paste one of the other browser classes and adjust for the new browser), add the class to the MAPPER inside src/providers/browsers/browsers_provider.py and add the browser name to the "choices" parameter in pytest_addoption (located inside /conftest.py).

## Author

Tobiasz Biliński - tobiasz.bilinski@globallogic.com

